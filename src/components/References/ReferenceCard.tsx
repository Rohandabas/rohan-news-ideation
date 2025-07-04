import React from 'react';
import { Reference } from '../../types';
import { ExternalLink, Calendar, Star, FileText, User, Building, BookOpen } from 'lucide-react';
import { format } from 'date-fns';

interface ReferenceCardProps {
  reference: Reference;
}

export default function ReferenceCard({ reference }: ReferenceCardProps) {
  const typeIcons = {
    article: FileText,
    study: BookOpen,
    report: Building,
    social_media: User,
    expert: User,
    official: Building
  };

  const typeColors = {
    article: 'bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300',
    study: 'bg-purple-50 dark:bg-purple-900/20 text-purple-700 dark:text-purple-300',
    report: 'bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-300',
    social_media: 'bg-pink-50 dark:bg-pink-900/20 text-pink-700 dark:text-pink-300',
    expert: 'bg-orange-50 dark:bg-orange-900/20 text-orange-700 dark:text-orange-300',
    official: 'bg-gray-50 dark:bg-gray-900/20 text-gray-700 dark:text-gray-300'
  };

  const TypeIcon = typeIcons[reference.type];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm border border-gray-200 dark:border-gray-700 hover:shadow-md transition-all duration-200 group">
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <div className="flex items-center space-x-3 mb-2">
            <div className={`p-2 rounded-lg ${typeColors[reference.type]}`}>
              <TypeIcon className="w-4 h-4" />
            </div>
            <span className={`px-2 py-1 rounded-full text-xs font-medium capitalize ${typeColors[reference.type]}`}>
              {reference.type.replace('_', ' ')}
            </span>
          </div>
          
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors duration-200 mb-2">
            {reference.title}
          </h3>
          
          <div className="flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
            <span className="font-medium">{reference.source}</span>
            <div className="flex items-center space-x-1">
              <Calendar className="w-4 h-4" />
              <span>{format(new Date(reference.date), 'MMM dd, yyyy')}</span>
            </div>
          </div>
        </div>
        
        <div className="flex items-center space-x-3">
          <div className="flex items-center space-x-1">
            <Star className="w-4 h-4 text-yellow-500" />
            <span className="text-sm font-medium text-gray-900 dark:text-white">
              {reference.relevance_score}%
            </span>
          </div>
          
          <a
            href={reference.url}
            target="_blank"
            rel="noopener noreferrer"
            className="p-2 text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-200"
            onClick={(e) => e.stopPropagation()}
          >
            <ExternalLink className="w-5 h-5" />
          </a>
        </div>
      </div>

      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
            <div 
              className="bg-gradient-to-r from-blue-500 to-purple-500 h-2 rounded-full transition-all duration-500"
              style={{ width: `${reference.relevance_score}%` }}
            />
          </div>
        </div>
        
        <div className="text-xs text-gray-500 dark:text-gray-400 ml-4">
          Relevance Score
        </div>
      </div>
    </div>
  );
}