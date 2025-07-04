import React from 'react';

interface TrendChartProps {
  title: string;
  data: Array<{ hour: number; posts: number; engagement: number }>;
}

export default function TrendChart({ title, data }: TrendChartProps) {
  const maxEngagement = Math.max(...data.map(d => d.engagement));
  
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm border border-gray-200 dark:border-gray-700">
      <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-6">{title}</h3>
      
      <div className="space-y-4">
        <div className="flex justify-between text-sm text-gray-500 dark:text-gray-400">
          <span>12 AM</span>
          <span>6 AM</span>
          <span>12 PM</span>
          <span>6 PM</span>
          <span>11 PM</span>
        </div>
        
        <div className="relative h-32 flex items-end space-x-1">
          {data.map((point, index) => (
            <div
              key={index}
              className="bg-gradient-to-t from-blue-500 to-blue-400 rounded-t flex-1 min-w-0 hover:from-blue-600 hover:to-blue-500 transition-all duration-200 cursor-pointer group"
              style={{ 
                height: `${(point.engagement / maxEngagement) * 100}%`,
                minHeight: '4px'
              }}
            >
              <div className="opacity-0 group-hover:opacity-100 absolute -top-8 left-1/2 transform -translate-x-1/2 bg-gray-900 text-white text-xs px-2 py-1 rounded transition-opacity duration-200">
                {point.engagement.toLocaleString()}
              </div>
            </div>
          ))}
        </div>
        
        <div className="flex justify-between items-center pt-4 border-t border-gray-200 dark:border-gray-700">
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-blue-500 rounded-full"></div>
              <span className="text-sm text-gray-600 dark:text-gray-400">Engagement</span>
            </div>
          </div>
          <div className="text-sm text-gray-500 dark:text-gray-400">
            Peak: {Math.max(...data.map(d => d.engagement)).toLocaleString()}
          </div>
        </div>
      </div>
    </div>
  );
}