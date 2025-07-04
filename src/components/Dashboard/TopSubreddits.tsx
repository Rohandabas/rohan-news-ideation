import React from 'react';
import { ExternalLink, Users } from 'lucide-react';

interface SubredditData {
  name: string;
  posts: number;
  engagement: number;
}

interface TopSubredditsProps {
  subreddits: SubredditData[];
}

export default function TopSubreddits({ subreddits }: TopSubredditsProps) {
  const maxEngagement = Math.max(...subreddits.map(s => s.engagement));
  
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm border border-gray-200 dark:border-gray-700">
      <div className="flex items-center justify-between mb-6">
        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Top Performing Subreddits</h3>
        <Users className="w-5 h-5 text-gray-400" />
      </div>
      
      <div className="space-y-4">
        {subreddits.map((subreddit, index) => (
          <div key={subreddit.name} className="group">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center space-x-3">
                <span className="text-sm font-medium text-gray-500 dark:text-gray-400 w-4">
                  #{index + 1}
                </span>
                <span className="font-medium text-gray-900 dark:text-white">
                  r/{subreddit.name}
                </span>
                <button className="opacity-0 group-hover:opacity-100 transition-opacity duration-200">
                  <ExternalLink className="w-4 h-4 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300" />
                </button>
              </div>
              <div className="text-right">
                <div className="text-sm font-medium text-gray-900 dark:text-white">
                  {subreddit.engagement.toLocaleString()}
                </div>
                <div className="text-xs text-gray-500 dark:text-gray-400">
                  {subreddit.posts} posts
                </div>
              </div>
            </div>
            
            <div className="relative h-2 bg-gray-100 dark:bg-gray-700 rounded-full overflow-hidden">
              <div
                className="absolute top-0 left-0 h-full bg-gradient-to-r from-blue-500 to-purple-500 rounded-full transition-all duration-500"
                style={{ width: `${(subreddit.engagement / maxEngagement) * 100}%` }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}