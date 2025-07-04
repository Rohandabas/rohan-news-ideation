import React from 'react';
import { TrendingUp, Search, Settings, Bell, User, RefreshCw } from 'lucide-react';

interface HeaderProps {
  onSearch: (query: string) => void;
  onRefresh?: () => void;
  isRefreshing?: boolean;
  lastUpdated?: string | null;
}

export default function Header({ onSearch, onRefresh, isRefreshing, lastUpdated }: HeaderProps) {
  const formatLastUpdated = (timestamp: string | null) => {
    if (!timestamp) return 'Never';
    
    const date = new Date(timestamp);
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    
    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    
    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `${diffHours}h ago`;
    
    return date.toLocaleDateString();
  };

  return (
    <header className="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-700 px-6 py-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <div className="p-2 bg-blue-600 rounded-lg">
              <TrendingUp className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-gray-900 dark:text-white">TrendScout</h1>
              <p className="text-sm text-gray-500 dark:text-gray-400">
                Live Reddit Content Analysis
              </p>
            </div>
          </div>
          
          {/* Live Status Indicator */}
          <div className="flex items-center space-x-2 px-3 py-1 bg-green-50 dark:bg-green-900/20 rounded-full">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            <span className="text-xs font-medium text-green-700 dark:text-green-300">
              LIVE
            </span>
          </div>
        </div>

        <div className="flex-1 max-w-2xl mx-8">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
            <input
              type="text"
              placeholder="Search trending topics, subreddits, or keywords..."
              className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
              onChange={(e) => onSearch(e.target.value)}
            />
          </div>
        </div>

        <div className="flex items-center space-x-4">
          {/* Last Updated Info */}
          <div className="text-xs text-gray-500 dark:text-gray-400">
            Updated: {formatLastUpdated(lastUpdated)}
          </div>
          
          {/* Refresh Button */}
          {onRefresh && (
            <button
              onClick={onRefresh}
              disabled={isRefreshing}
              className="p-2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors duration-200 disabled:opacity-50"
              title="Refresh data"
            >
              <RefreshCw className={`w-5 h-5 ${isRefreshing ? 'animate-spin' : ''}`} />
            </button>
          )}
          
          <button className="p-2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors duration-200">
            <Bell className="w-5 h-5" />
          </button>
          <button className="p-2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors duration-200">
            <Settings className="w-5 h-5" />
          </button>
          <div className="p-2 bg-gray-100 dark:bg-gray-700 rounded-full">
            <User className="w-5 h-5 text-gray-600 dark:text-gray-300" />
          </div>
        </div>
      </div>
    </header>
  );
}