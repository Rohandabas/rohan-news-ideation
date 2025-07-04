import React from 'react';
import { TrendingTopic } from '../../types';
import { TrendingUp, MessageCircle, ThumbsUp, Clock, Tag } from 'lucide-react';
import { formatDistanceToNow } from 'date-fns';

interface TrendCardProps {
  topic: TrendingTopic;
  onClick: (topic: TrendingTopic) => void;
}

export default function TrendCard({ topic, onClick }: TrendCardProps) {
  const sentimentColors = {
    positive: 'bg-green-100 dark:bg-green-900/20 text-green-800 dark:text-green-300',
    negative: 'bg-red-100 dark:bg-red-900/20 text-red-800 dark:text-red-300',
    neutral: 'bg-gray-100 dark:bg-gray-900/20 text-gray-800 dark:text-gray-300'
  };

  return (
    <div 
      className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm border border-gray-200 dark:border-gray-700 hover:shadow-md hover:border-blue-200 dark:hover:border-blue-700 transition-all duration-200 cursor-pointer group"
      onClick={() => onClick(topic)}
    >
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors duration-200">
            {topic.title}
          </h3>
          <div className="flex items-center space-x-4 mt-2 text-sm text-gray-500 dark:text-gray-400">
            <div className="flex items-center space-x-1">
              <Clock className="w-4 h-4" />
              <span>{formatDistanceToNow(new Date(topic.peak_time), { addSuffix: true })}</span>
            </div>
            <div className="flex items-center space-x-1">
              <Tag className="w-4 h-4" />
              <span>{topic.category}</span>
            </div>
          </div>
        </div>
        
        <div className="flex items-center space-x-2">
          <span className={`px-2 py-1 rounded-full text-xs font-medium ${sentimentColors[topic.sentiment]}`}>
            {topic.sentiment}
          </span>
          <div className="flex items-center space-x-1 text-sm font-medium text-blue-600 dark:text-blue-400">
            <TrendingUp className="w-4 h-4" />
            <span>{topic.trend_velocity.toFixed(1)}%</span>
          </div>
        </div>
      </div>

      <div className="space-y-3 mb-4">
        {topic.posts.slice(0, 2).map((post) => (
          <div key={post.id} className="p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg">
            <h4 className="text-sm font-medium text-gray-900 dark:text-white mb-2 line-clamp-2">
              {post.title}
            </h4>
            <div className="flex items-center justify-between text-xs text-gray-500 dark:text-gray-400">
              <span>r/{post.subreddit}</span>
              <div className="flex items-center space-x-3">
                <div className="flex items-center space-x-1">
                  <ThumbsUp className="w-3 h-3" />
                  <span>{post.score.toLocaleString()}</span>
                </div>
                <div className="flex items-center space-x-1">
                  <MessageCircle className="w-3 h-3" />
                  <span>{post.comments.toLocaleString()}</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="flex items-center justify-between">
        <div className="flex flex-wrap gap-2">
          {topic.subreddits.slice(0, 3).map((subreddit) => (
            <span key={subreddit} className="px-2 py-1 bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300 text-xs rounded-full">
              r/{subreddit}
            </span>
          ))}
          {topic.subreddits.length > 3 && (
            <span className="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 text-xs rounded-full">
              +{topic.subreddits.length - 3} more
            </span>
          )}
        </div>
        
        <div className="text-right">
          <div className="text-sm font-medium text-gray-900 dark:text-white">
            Score: {topic.engagement_score}
          </div>
          <div className="text-xs text-gray-500 dark:text-gray-400">
            {topic.posts.length} posts
          </div>
        </div>
      </div>
    </div>
  );
}