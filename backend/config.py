import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
    REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
    REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')
    FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    # Subreddits to monitor
    MONITORED_SUBREDDITS = [
        'worldnews', 'technology', 'science', 'business', 'politics',
        'news', 'economics', 'environment', 'health', 'education',
        'space', 'artificial', 'programming', 'startups', 'investing'
    ]
    
    # News value keywords for scoring
    NEWS_KEYWORDS = {
        'breaking': 10,
        'urgent': 9,
        'exclusive': 8,
        'first': 7,
        'major': 6,
        'significant': 5,
        'important': 4,
        'new': 3,
        'update': 2,
        'report': 1
    }