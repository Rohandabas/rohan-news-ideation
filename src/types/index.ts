export interface RedditPost {
  id: string;
  title: string;
  content: string;
  subreddit: string;
  author: string;
  score: number;
  comments: number;
  created_utc: number;
  url: string;
  permalink: string;
  flair?: string;
  is_video: boolean;
  thumbnail?: string;
}

export interface TrendingTopic {
  id: string;
  title: string;
  posts: RedditPost[];
  engagement_score: number;
  trend_velocity: number;
  subreddits: string[];
  keywords: string[];
  sentiment: 'positive' | 'negative' | 'neutral';
  category: string;
  peak_time: number;
}

export interface StoryIdea {
  id: string;
  topic_id: string;
  headline: string;
  angle: string;
  news_value: {
    timeliness: number;
    proximity: number;
    impact: number;
    prominence: number;
    conflict: number;
    human_interest: number;
  };
  suggested_sources: string[];
  target_audience: string[];
  estimated_reach: number;
  urgency: 'low' | 'medium' | 'high' | 'breaking';
  references: Reference[];
  reasons_for_coverage: string[];  // Added for Gemini-generated reasons

}

export interface Reference {
  id: string;
  title: string;
  url: string;
  source: string;
  date: string;
  relevance_score: number;
  type: 'article' | 'study' | 'report' | 'social_media' | 'expert' | 'official';
}

export interface AnalyticsData {
  trending_topics_count: number;
  total_engagement: number;
  top_performing_subreddits: Array<{ name: string; posts: number; engagement: number }>;
  sentiment_distribution: { positive: number; negative: number; neutral: number };
  hourly_activity: Array<{ hour: number; posts: number; engagement: number }>;
}