import praw
import time
from datetime import datetime, timedelta
from textblob import TextBlob
from config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RedditClient:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=Config.REDDIT_CLIENT_ID,
            client_secret=Config.REDDIT_CLIENT_SECRET,
            user_agent=Config.REDDIT_USER_AGENT
        )
        logger.info("Reddit client initialized successfully")
    
    def get_trending_posts(self, subreddit_name, limit=50, time_filter='day'):
        """Fetch trending posts from a specific subreddit"""
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            posts = []
            
            for submission in subreddit.hot(limit=limit):
                # Skip stickied posts
                if submission.stickied:
                    continue
                
                # Calculate engagement score
                engagement_score = self._calculate_engagement_score(submission)
                
                # Analyze sentiment
                sentiment = self._analyze_sentiment(submission.title + " " + submission.selftext)
                
                post_data = {
                    'id': submission.id,
                    'title': submission.title,
                    'content': submission.selftext[:500] if submission.selftext else '',
                    'subreddit': submission.subreddit.display_name,
                    'author': str(submission.author) if submission.author else '[deleted]',
                    'score': submission.score,
                    'comments': submission.num_comments,
                    'created_utc': int(submission.created_utc),
                    'url': submission.url,
                    'permalink': submission.permalink,
                    'flair': submission.link_flair_text,
                    'is_video': submission.is_video,
                    'thumbnail': submission.thumbnail if hasattr(submission, 'thumbnail') else None,
                    'engagement_score': engagement_score,
                    'sentiment': sentiment,
                    'news_value': self._calculate_news_value(submission)
                }
                posts.append(post_data)
            
            return posts
        except Exception as e:
            logger.error(f"Error fetching posts from r/{subreddit_name}: {str(e)}")
            return []
    
    def get_all_trending_topics(self):
        """Fetch trending topics from all monitored subreddits"""
        all_posts = []
        
        for subreddit_name in Config.MONITORED_SUBREDDITS:
            posts = self.get_trending_posts(subreddit_name, limit=20)
            all_posts.extend(posts)
            time.sleep(1)  # Rate limiting
        
        # Group posts by similar topics
        trending_topics = self._group_posts_by_topic(all_posts)
        return trending_topics
    
    def _calculate_engagement_score(self, submission):
        """Calculate engagement score based on various metrics"""
        # Time decay factor (newer posts get higher scores)
        hours_old = (time.time() - submission.created_utc) / 3600
        time_decay = max(0.1, 1 - (hours_old / 24))
        
        # Base engagement calculation
        base_score = (submission.score * 0.7) + (submission.num_comments * 0.3)
        
        # Apply time decay
        engagement_score = int(base_score * time_decay)
        
        return min(100, max(1, engagement_score))
    
    def _analyze_sentiment(self, text):
        """Analyze sentiment of the text"""
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            
            if polarity > 0.1:
                return 'positive'
            elif polarity < -0.1:
                return 'negative'
            else:
                return 'neutral'
        except:
            return 'neutral'
    
    def _calculate_news_value(self, submission):
        """Calculate news value score based on content analysis"""
        title_lower = submission.title.lower()
        content_lower = submission.selftext.lower() if submission.selftext else ''
        combined_text = title_lower + ' ' + content_lower
        
        news_score = 0
        
        # Check for news keywords
        for keyword, score in Config.NEWS_KEYWORDS.items():
            if keyword in combined_text:
                news_score += score
        
        # Bonus for high engagement
        if submission.score > 1000:
            news_score += 5
        if submission.num_comments > 100:
            news_score += 3
        
        # Bonus for recent posts
        hours_old = (time.time() - submission.created_utc) / 3600
        if hours_old < 6:
            news_score += 5
        elif hours_old < 12:
            news_score += 3
        
        return min(100, news_score)
    
    def _group_posts_by_topic(self, posts):
        """Group similar posts into trending topics"""
        # Sort posts by engagement score
        posts.sort(key=lambda x: x['engagement_score'], reverse=True)
        
        topics = []
        used_posts = set()
        
        for post in posts:
            if post['id'] in used_posts:
                continue
            
            # Find similar posts
            similar_posts = [post]
            keywords = self._extract_keywords(post['title'])
            
            for other_post in posts:
                if (other_post['id'] != post['id'] and 
                    other_post['id'] not in used_posts and
                    self._posts_are_similar(post, other_post, keywords)):
                    similar_posts.append(other_post)
                    used_posts.add(other_post['id'])
            
            if len(similar_posts) >= 1:  # At least 1 post to form a topic
                topic = self._create_topic_from_posts(similar_posts)
                topics.append(topic)
                used_posts.add(post['id'])
        
        return sorted(topics, key=lambda x: x['engagement_score'], reverse=True)
    
    def _extract_keywords(self, title):
        """Extract keywords from title"""
        # Simple keyword extraction
        words = title.lower().split()
        # Filter out common words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
        keywords = [word for word in words if word not in stop_words and len(word) > 3]
        return keywords[:5]  # Top 5 keywords
    
    def _posts_are_similar(self, post1, post2, keywords):
        """Check if two posts are about similar topics"""
        title2_lower = post2['title'].lower()
        
        # Check if they share keywords
        shared_keywords = sum(1 for keyword in keywords if keyword in title2_lower)
        
        # Check if they're from related subreddits
        related_subreddits = {
            'worldnews': ['news', 'politics'],
            'technology': ['programming', 'artificial', 'startups'],
            'science': ['space', 'health', 'environment'],
            'business': ['economics', 'investing', 'startups']
        }
        
        subreddit1 = post1['subreddit'].lower()
        subreddit2 = post2['subreddit'].lower()
        
        subreddits_related = (
            subreddit1 == subreddit2 or
            subreddit2 in related_subreddits.get(subreddit1, []) or
            subreddit1 in related_subreddits.get(subreddit2, [])
        )
        
        return shared_keywords >= 2 or (shared_keywords >= 1 and subreddits_related)
    
    def _create_topic_from_posts(self, posts):
        """Create a trending topic from a group of posts"""
        # Use the highest scoring post's title as the topic title
        main_post = max(posts, key=lambda x: x['engagement_score'])
        
        # Calculate aggregate metrics
        total_engagement = sum(post['engagement_score'] for post in posts)
        avg_sentiment_score = self._calculate_avg_sentiment(posts)
        
        # Extract common keywords
        all_keywords = []
        for post in posts:
            all_keywords.extend(self._extract_keywords(post['title']))
        
        # Count keyword frequency
        keyword_counts = {}
        for keyword in all_keywords:
            keyword_counts[keyword] = keyword_counts.get(keyword, 0) + 1
        
        # Get top keywords
        top_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:8]
        keywords = [keyword for keyword, count in top_keywords]
        
        # Get unique subreddits
        subreddits = list(set(post['subreddit'] for post in posts))
        
        # Calculate trend velocity (simplified)
        recent_posts = [p for p in posts if (time.time() - p['created_utc']) < 21600]  # Last 6 hours
        trend_velocity = (len(recent_posts) / len(posts)) * 100 if posts else 0
        
        return {
            'id': f"topic-{main_post['id']}",
            'title': main_post['title'],
            'posts': posts,
            'engagement_score': min(100, total_engagement // len(posts)),
            'trend_velocity': round(trend_velocity, 1),
            'subreddits': subreddits,
            'keywords': keywords,
            'sentiment': avg_sentiment_score,
            'category': self._categorize_topic(main_post['subreddit']),
            'peak_time': max(post['created_utc'] for post in posts) * 1000  # Convert to milliseconds
        }
    
    def _calculate_avg_sentiment(self, posts):
        """Calculate average sentiment from posts"""
        sentiments = [post['sentiment'] for post in posts]
        sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for sentiment in sentiments:
            sentiment_counts[sentiment] += 1
        
        # Return the most common sentiment
        return max(sentiment_counts, key=sentiment_counts.get)
    
    def _categorize_topic(self, subreddit):
        """Categorize topic based on subreddit"""
        categories = {
            'worldnews': 'World News',
            'news': 'News',
            'politics': 'Politics',
            'technology': 'Technology',
            'science': 'Science',
            'business': 'Business',
            'economics': 'Economics',
            'health': 'Health',
            'environment': 'Environment',
            'space': 'Science',
            'artificial': 'Technology',
            'programming': 'Technology',
            'startups': 'Business',
            'investing': 'Business',
            'education': 'Education'
        }
        return categories.get(subreddit.lower(), 'General')