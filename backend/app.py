from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
import time
import schedule
from datetime import datetime
import logging

from reddit_client import RedditClient
from story_generator import StoryGenerator
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Global data storage (in production, use a proper database)
trending_data = {
    'topics': [],
    'stories': [],
    'analytics': {},
    'last_updated': None
}

# Initialize clients
reddit_client = RedditClient()
story_generator = StoryGenerator()

def update_trending_data():
    """Update trending data from Reddit"""
    try:
        logger.info("Fetching trending topics from Reddit...")
        
        # Fetch trending topics
        topics = reddit_client.get_all_trending_topics()
        
        # Generate story ideas
        stories = story_generator.generate_story_ideas(topics)
        
        # Calculate analytics
        analytics = calculate_analytics(topics, stories)
        
        # Update global data
        trending_data['topics'] = topics
        trending_data['stories'] = stories
        trending_data['analytics'] = analytics
        trending_data['last_updated'] = datetime.now().isoformat()
        
        logger.info(f"Updated data: {len(topics)} topics, {len(stories)} stories")
        
    except Exception as e:
        logger.error(f"Error updating trending data: {str(e)}")

def calculate_analytics(topics, stories):
    """Calculate analytics from topics and stories"""
    if not topics:
        # return {}
        return {
        'trending_topics_count': 0,
        'total_engagement': 0,
        'top_performing_subreddits': [],
        'sentiment_distribution': {'positive': 0, 'negative': 0, 'neutral': 0},
        'hourly_activity': [{'hour': h, 'posts': 0, 'engagement': 0} for h in range(24)]
    }
    
    # Count posts by subreddit
    subreddit_stats = {}
    total_engagement = 0
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    
    for topic in topics:
        total_engagement += topic['engagement_score']
        sentiment_counts[topic['sentiment']] += 1
        
        for post in topic['posts']:
            subreddit = post['subreddit']
            if subreddit not in subreddit_stats:
                subreddit_stats[subreddit] = {'posts': 0, 'engagement': 0}
            
            subreddit_stats[subreddit]['posts'] += 1
            subreddit_stats[subreddit]['engagement'] += post['engagement_score']
    
    # Top performing subreddits
    top_subreddits = sorted(
        [{'name': name, **stats} for name, stats in subreddit_stats.items()],
        key=lambda x: x['engagement'],
        reverse=True
    )[:5]
    
    # Generate hourly activity (simplified)
    hourly_activity = []
    for hour in range(24):
        posts_count = len([p for topic in topics for p in topic['posts'] 
                          if datetime.fromtimestamp(p['created_utc']).hour == hour])
        engagement = sum([p['engagement_score'] for topic in topics for p in topic['posts'] 
                         if datetime.fromtimestamp(p['created_utc']).hour == hour])
        
        hourly_activity.append({
            'hour': hour,
            'posts': posts_count,
            'engagement': engagement
        })
    
    return {
        'trending_topics_count': len(topics),
        'total_engagement': total_engagement,
        'top_performing_subreddits': top_subreddits,
        'sentiment_distribution': sentiment_counts,
        'hourly_activity': hourly_activity
    }

# API Routes
@app.route('/api/trending', methods=['GET'])
def get_trending_topics():
    """Get trending topics"""
    return jsonify({
        'topics': trending_data['topics'],
        'last_updated': trending_data['last_updated']
    })

@app.route('/api/stories', methods=['GET'])
def get_story_ideas():
    """Get story ideas"""
    return jsonify({
        'stories': trending_data['stories'],
        'last_updated': trending_data['last_updated']
    })

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    """Get analytics data"""
    return jsonify({
        'analytics': trending_data['analytics'],
        'last_updated': trending_data['last_updated']
    })

@app.route('/api/references', methods=['GET'])
def get_references():
    """Get all references from stories"""
    all_references = []
    for story in trending_data['stories']:
        all_references.extend(story.get('references', []))
    
    return jsonify({
        'references': all_references,
        'last_updated': trending_data['last_updated']
    })

@app.route('/api/subreddit/<subreddit_name>', methods=['GET'])
def get_subreddit_posts(subreddit_name):
    """Get posts from a specific subreddit"""
    limit = request.args.get('limit', 20, type=int)
    posts = reddit_client.get_trending_posts(subreddit_name, limit=limit)
    
    return jsonify({
        'subreddit': subreddit_name,
        'posts': posts,
        'count': len(posts)
    })

@app.route('/api/refresh', methods=['POST'])
def refresh_data():
    """Manually refresh data"""
    try:
        update_trending_data()
        return jsonify({
            'success': True,
            'message': 'Data refreshed successfully',
            'last_updated': trending_data['last_updated']
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error refreshing data: {str(e)}'
        }), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get API status"""
    return jsonify({
        'status': 'online',
        'last_updated': trending_data['last_updated'],
        'topics_count': len(trending_data['topics']),
        'stories_count': len(trending_data['stories']),
        'monitored_subreddits': Config.MONITORED_SUBREDDITS
    })

def run_scheduler():
    """Run the background scheduler"""
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    # Initial data fetch
    logger.info("Starting TrendScout Backend...")
    update_trending_data()
    
    # Schedule regular updates every 15 minutes
    schedule.every(15).minutes.do(update_trending_data)
    
    # Start scheduler in background thread
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    
    # Start Flask app
    logger.info(f"Starting Flask server on port {Config.FLASK_PORT}")
    app.run(host='0.0.0.0', port=Config.FLASK_PORT, debug=False)