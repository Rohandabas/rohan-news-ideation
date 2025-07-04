// import React from 'react';
// import { StoryIdea } from '../../types';
// import { 
//   Clock, 
//   Users, 
//   Target, 
//   AlertTriangle, 
//   CheckCircle, 
//   ExternalLink,
//   BookOpen
// } from 'lucide-react';

// interface StoryCardProps {
//   story: StoryIdea;
//   onClick: (story: StoryIdea) => void;
// }

// export default function StoryCard({ story, onClick }: StoryCardProps) {
//   const urgencyColors = {
//     low: 'bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-300',
//     medium: 'bg-yellow-100 dark:bg-yellow-900/20 text-yellow-800 dark:text-yellow-300',
//     high: 'bg-orange-100 dark:bg-orange-900/20 text-orange-800 dark:text-orange-300',
//     breaking: 'bg-red-100 dark:bg-red-900/20 text-red-800 dark:text-red-300'
//   };

//   const urgencyIcons = {
//     low: CheckCircle,
//     medium: Clock,
//     high: AlertTriangle,
//     breaking: AlertTriangle
//   };

//   const UrgencyIcon = urgencyIcons[story.urgency];
  
//   const newsValueAverage = Object.values(story.news_value).reduce((a, b) => a + b, 0) / Object.keys(story.news_value).length;

//   return (
//     <div 
//       className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm border border-gray-200 dark:border-gray-700 hover:shadow-md hover:border-blue-200 dark:hover:border-blue-700 transition-all duration-200 cursor-pointer group"
//       onClick={() => onClick(story)}
//     >
//       <div className="flex items-start justify-between mb-4">
//         <div className="flex-1">
//           <h3 className="text-xl font-semibold text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors duration-200 mb-2">
//             {story.headline}
//           </h3>
//           <p className="text-gray-600 dark:text-gray-400 mb-3">
//             {story.angle}
//           </p>
//         </div>
        
//         <div className="flex items-center space-x-2">
//           <span className={`px-3 py-1 rounded-full text-xs font-medium flex items-center space-x-1 ${urgencyColors[story.urgency]}`}>
//             <UrgencyIcon className="w-3 h-3" />
//             <span className="capitalize">{story.urgency}</span>
//           </span>
//         </div>
//       </div>

//       <div className="grid grid-cols-3 gap-4 mb-4">
//         <div className="text-center p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg">
//           <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">
//             {Math.round(newsValueAverage)}
//           </div>
//           <div className="text-xs text-gray-500 dark:text-gray-400">News Value</div>
//         </div>
        
//         <div className="text-center p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg">
//           <div className="text-2xl font-bold text-green-600 dark:text-green-400">
//             {(story.estimated_reach / 1000).toFixed(0)}K
//           </div>
//           <div className="text-xs text-gray-500 dark:text-gray-400">Est. Reach</div>
//         </div>
        
//         <div className="text-center p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg">
//           <div className="text-2xl font-bold text-purple-600 dark:text-purple-400">
//             {story.references.length}
//           </div>
//           <div className="text-xs text-gray-500 dark:text-gray-400">References</div>
//         </div>
//       </div>

//       <div className="space-y-3 mb-4">
//         <div>
//           <div className="flex items-center space-x-2 mb-2">
//             <Users className="w-4 h-4 text-gray-400" />
//             <span className="text-sm font-medium text-gray-700 dark:text-gray-300">Target Audience</span>
//           </div>
//           <div className="flex flex-wrap gap-2">
//             {story.target_audience.map((audience) => (
//               <span key={audience} className="px-2 py-1 bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300 text-xs rounded-full">
//                 {audience}
//               </span>
//             ))}
//           </div>
//         </div>

//         <div>
//           <div className="flex items-center space-x-2 mb-2">
//             <Target className="w-4 h-4 text-gray-400" />
//             <span className="text-sm font-medium text-gray-700 dark:text-gray-300">Suggested Sources</span>
//           </div>
//           <div className="space-y-1">
//             {story.suggested_sources.slice(0, 2).map((source, index) => (
//               <div key={index} className="flex items-center space-x-2 text-sm text-gray-600 dark:text-gray-400">
//                 <div className="w-1.5 h-1.5 bg-gray-400 rounded-full"></div>
//                 <span>{source}</span>
//               </div>
//             ))}
//             {story.suggested_sources.length > 2 && (
//               <div className="text-sm text-blue-600 dark:text-blue-400">
//                 +{story.suggested_sources.length - 2} more sources
//               </div>
//             )}
//           </div>
//         </div>
//       </div>

//       <div className="flex items-center justify-between pt-4 border-t border-gray-200 dark:border-gray-700">
//         <div className="flex items-center space-x-4">
//           <div className="flex items-center space-x-1 text-sm text-gray-500 dark:text-gray-400">
//             <BookOpen className="w-4 h-4" />
//             <span>{story.references.length} refs</span>
//           </div>
//         </div>
        
//         <button className="flex items-center space-x-1 text-sm text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors duration-200">
//           <span>View Details</span>
//           <ExternalLink className="w-4 h-4" />
//         </button>
//       </div>
//     </div>
//   );
// }
import React from 'react';
import { StoryIdea } from '../../types';
import { 
  Clock, 
  Users, 
  Target, 
  AlertTriangle, 
  CheckCircle, 
  ExternalLink,
  BookOpen
} from 'lucide-react';

interface StoryCardProps {
  story: StoryIdea;
  onClick: (story: StoryIdea) => void;
}

export default function StoryCard({ story, onClick }: StoryCardProps) {
  const urgencyColors = {
    low: 'bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-300',
    medium: 'bg-yellow-100 dark:bg-yellow-900/20 text-yellow-800 dark:text-yellow-300',
    high: 'bg-orange-100 dark:bg-orange-900/20 text-orange-800 dark:text-orange-300',
    breaking: 'bg-red-100 dark:bg-red-900/20 text-red-800 dark:text-red-300'
  };

  const urgencyIcons = {
    low: CheckCircle,
    medium: Clock,
    high: AlertTriangle,
    breaking: AlertTriangle
  };

  const UrgencyIcon = urgencyIcons[story.urgency];
  
  const newsValueAverage = Object.values(story.news_value).reduce((a, b) => a + b, 0) / Object.keys(story.news_value).length;

  return (
    <div 
      className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm border border-gray-200 dark:border-gray-700 hover:shadow-md hover:border-blue-200 dark:hover:border-blue-700 transition-all duration-200 cursor-pointer group"
      onClick={() => onClick(story)}
    >
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <h3 className="text-xl font-semibold text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors duration-200 mb-2">
            {story.headline}
          </h3>
          <p className="text-gray-600 dark:text-gray-400 mb-3">
            {story.angle}
          </p>
        </div>
        
        <div className="flex items-center space-x-2">
          <span className={`px-3 py-1 rounded-full text-xs font-medium flex items-center space-x-1 ${urgencyColors[story.urgency]}`}>
            <UrgencyIcon className="w-3 h-3" />
            <span className="capitalize">{story.urgency}</span>
          </span>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-4 mb-4">
        <div className="text-center p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg">
          <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">
            {Math.round(newsValueAverage)}
          </div>
          <div className="text-xs text-gray-500 dark:text-gray-400">News Value</div>
        </div>
        
        <div className="text-center p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg">
          <div className="text-2xl font-bold text-green-600 dark:text-green-400">
            {(story.estimated_reach / 1000).toFixed(0)}K
          </div>
          <div className="text-xs text-gray-500 dark:text-gray-400">Est. Reach</div>
        </div>
        
        <div className="text-center p-3 bg-gray-50 dark:bg-gray-700/50 rounded-lg">
          <div className="text-2xl font-bold text-purple-600 dark:text-purple-400">
            {story.references.length}
          </div>
          <div className="text-xs text-gray-500 dark:text-gray-400">References</div>
        </div>
      </div>

      <div className="space-y-3 mb-4">
        <div>
          <div className="flex items-center space-x-2 mb-2">
            <Users className="w-4 h-4 text-gray-400" />
            <span className="text-sm font-medium text-gray-700 dark:text-gray-300">Target Audience</span>
          </div>
          <div className="flex flex-wrap gap-2">
            {story.target_audience.map((audience) => (
              <span key={audience} className="px-2 py-1 bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300 text-xs rounded-full">
                {audience}
              </span>
            ))}
          </div>
        </div>

        <div>
          <div className="flex items-center space-x-2 mb-2">
            <Target className="w-4 h-4 text-gray-400" />
            <span className="text-sm font-medium text-gray-700 dark:text-gray-300">Suggested Sources</span>
          </div>
          <div className="space-y-1">
            {story.suggested_sources.slice(0, 2).map((source, index) => (
              <div key={index} className="flex items-center space-x-2 text-sm text-gray-600 dark:text-gray-400">
                <div className="w-1.5 h-1.5 bg-gray-400 rounded-full"></div>
                <span>{source}</span>
              </div>
            ))}
            {story.suggested_sources.length > 2 && (
              <div className="text-sm text-blue-600 dark:text-blue-400">
                +{story.suggested_sources.length - 2} more sources
              </div>
            )}
          </div>
        </div>

        {/* New section for Reasons for Coverage */}
        {story.reasons_for_coverage.length > 0 && (
          <div>
            <div className="flex items-center space-x-2 mb-2">
              <BookOpen className="w-4 h-4 text-gray-400" /> {/* Using BookOpen icon for reasons */}
              <span className="text-sm font-medium text-gray-700 dark:text-gray-300">Reasons for Coverage</span>
            </div>
            <ul className="list-disc pl-5 text-sm text-gray-600 dark:text-gray-400">
              {story.reasons_for_coverage.map((reason, index) => (
                <li key={index}>{reason}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

      <div className="flex items-center justify-between pt-4 border-t border-gray-200 dark:border-gray-700">
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-1 text-sm text-gray-500 dark:text-gray-400">
            <BookOpen className="w-4 h-4" />
            <span>{story.references.length} refs</span>
          </div>
        </div>
        
        <button className="flex items-center space-x-1 text-sm text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors duration-200">
          <span>View Details</span>
          <ExternalLink className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}