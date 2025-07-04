import React from 'react';
import { 
  BarChart3, 
  FileText, 
  Bookmark, 
  Target, 
  Globe, 
  Calendar,
  TrendingUp,
  Users,
  Settings
} from 'lucide-react';
import clsx from 'clsx';

interface SidebarProps {
  activeTab: string;
  onTabChange: (tab: string) => void;
}

const menuItems = [
  { id: 'dashboard', label: 'Dashboard', icon: BarChart3 },
  { id: 'trending', label: 'Trending Topics', icon: TrendingUp },
  { id: 'stories', label: 'Story Ideas', icon: FileText },
  { id: 'references', label: 'References', icon: Bookmark },
  // { id: 'subreddits', label: 'Subreddits', icon: Globe },
  // { id: 'calendar', label: 'Content Calendar', icon: Calendar },
  // { id: 'audience', label: 'Audience Insights', icon: Users },
  // { id: 'targets', label: 'Target Metrics', icon: Target },
];

export default function Sidebar({ activeTab, onTabChange }: SidebarProps) {
  return (
    <aside className="w-64 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-700 h-full">
      <nav className="p-4 space-y-2">
        {menuItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          
          return (
            <button
              key={item.id}
              onClick={() => onTabChange(item.id)}
              className={clsx(
                'w-full flex items-center space-x-3 px-3 py-2.5 rounded-lg text-left transition-all duration-200',
                isActive
                  ? 'bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800'
                  : 'text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-gray-900 dark:hover:text-gray-200'
              )}
            >
              <Icon className={clsx('w-5 h-5', isActive ? 'text-blue-600 dark:text-blue-400' : '')} />
              <span className="font-medium">{item.label}</span>
            </button>
          );
        })}
      </nav>
      
      <div className="absolute bottom-4 left-4 right-4">
        <button className="w-full flex items-center space-x-3 px-3 py-2.5 rounded-lg text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-gray-900 dark:hover:text-gray-200 transition-all duration-200">
          <Settings className="w-5 h-5" />
          <span className="font-medium">Settings</span>
        </button>
      </div>
    </aside>
  );
}