// import { TrendingTopic, StoryIdea, AnalyticsData, RedditPost, Reference } from '../types';

// export const mockRedditPosts: RedditPost[] = [
//   {
//     id: '1a2b3c',
//     title: 'Major breakthrough in renewable energy storage announced by MIT researchers',
//     content: 'Revolutionary battery technology could store renewable energy for weeks...',
//     subreddit: 'science',
//     author: 'sciencereporter',
//     score: 15420,
//     comments: 892,
//     created_utc: Date.now() - 3600000,
//     url: 'https://reddit.com/r/science/comments/1a2b3c',
//     permalink: '/r/science/comments/1a2b3c/major_breakthrough/',
//     flair: 'Energy',
//     is_video: false,
//     thumbnail: 'https://images.pexels.com/photos/159397/electric-power-high-voltage-flash-159397.jpeg?auto=compress&cs=tinysrgb&w=400'
//   },
//   {
//     id: '2b3c4d',
//     title: 'Tech workers report 40% productivity increase with 4-day work week pilot',
//     content: 'Several major tech companies are seeing unprecedented results...',
//     subreddit: 'technology',
//     author: 'techanalyst',
//     score: 12800,
//     comments: 654,
//     created_utc: Date.now() - 7200000,
//     url: 'https://reddit.com/r/technology/comments/2b3c4d',
//     permalink: '/r/technology/comments/2b3c4d/tech_workers_report/',
//     flair: 'Labor',
//     is_video: false
//   },
//   {
//     id: '3c4d5e',
//     title: 'Climate summit reaches historic agreement on carbon pricing',
//     content: 'World leaders commit to unified carbon tax framework...',
//     subreddit: 'worldnews',
//     author: 'climatewatch',
//     score: 18900,
//     comments: 1205,
//     created_utc: Date.now() - 1800000,
//     url: 'https://reddit.com/r/worldnews/comments/3c4d5e',
//     permalink: '/r/worldnews/comments/3c4d5e/climate_summit/',
//     flair: 'Politics',
//     is_video: false
//   }
// ];

// export const mockTrendingTopics: TrendingTopic[] = [
//   {
//     id: 'trend-1',
//     title: 'Renewable Energy Breakthroughs',
//     posts: mockRedditPosts.slice(0, 1),
//     engagement_score: 95,
//     trend_velocity: 12.5,
//     subreddits: ['science', 'technology', 'environment'],
//     keywords: ['renewable', 'energy', 'battery', 'MIT', 'storage'],
//     sentiment: 'positive',
//     category: 'Technology',
//     peak_time: Date.now() - 3600000
//   },
//   {
//     id: 'trend-2',
//     title: '4-Day Work Week Adoption',
//     posts: mockRedditPosts.slice(1, 2),
//     engagement_score: 87,
//     trend_velocity: 8.3,
//     subreddits: ['technology', 'jobs', 'business'],
//     keywords: ['work week', '4-day', 'productivity', 'tech workers'],
//     sentiment: 'positive',
//     category: 'Business',
//     peak_time: Date.now() - 7200000
//   },
//   {
//     id: 'trend-3',
//     title: 'Global Climate Policy',
//     posts: mockRedditPosts.slice(2, 3),
//     engagement_score: 92,
//     trend_velocity: 15.7,
//     subreddits: ['worldnews', 'politics', 'environment'],
//     keywords: ['climate', 'carbon tax', 'summit', 'agreement'],
//     sentiment: 'neutral',
//     category: 'Politics',
//     peak_time: Date.now() - 1800000
//   }
// ];

// export const mockReferences: Reference[] = [
//   {
//     id: 'ref-1',
//     title: 'MIT Energy Storage Research Paper',
//     url: 'https://example.com/mit-energy-paper',
//     source: 'MIT Technology Review',
//     date: '2024-01-15',
//     relevance_score: 95,
//     type: 'study'
//   },
//   {
//     id: 'ref-2',
//     title: 'Four-Day Work Week Global Report',
//     url: 'https://example.com/4day-report',
//     source: 'Harvard Business Review',
//     date: '2024-01-10',
//     relevance_score: 88,
//     type: 'report'
//   },
//   {
//     id: 'ref-3',
//     title: 'Climate Summit Official Declaration',
//     url: 'https://example.com/climate-declaration',
//     source: 'UN Climate Change',
//     date: '2024-01-16',
//     relevance_score: 92,
//     type: 'official'
//   }
// ];

// export const mockStoryIdeas: StoryIdea[] = [
//   {
//     id: 'story-1',
//     topic_id: 'trend-1',
//     headline: 'MIT\'s Revolutionary Battery Could End Energy Storage Crisis',
//     angle: 'Local Impact: How this breakthrough could affect regional energy costs and job market',
//     news_value: {
//       timeliness: 95,
//       proximity: 70,
//       impact: 90,
//       prominence: 85,
//       conflict: 30,
//       human_interest: 75
//     },
//     suggested_sources: [
//       'MIT researchers involved in the project',
//       'Local energy company executives',
//       'Environmental policy experts',
//       'Economics professor specializing in energy markets'
//     ],
//     target_audience: ['General public', 'Business leaders', 'Environmental advocates'],
//     estimated_reach: 150000,
//     urgency: 'high',
//     references: mockReferences.slice(0, 1)
//   },
//   {
//     id: 'story-2',
//     topic_id: 'trend-2',
//     headline: 'Is the 4-Day Work Week Coming to Your Industry?',
//     angle: 'Business Analysis: Which sectors are most likely to adopt shorter work weeks',
//     news_value: {
//       timeliness: 80,
//       proximity: 85,
//       impact: 80,
//       prominence: 60,
//       conflict: 45,
//       human_interest: 90
//     },
//     suggested_sources: [
//       'Local HR directors',
//       'Labor economists',
//       'Workers who have experienced 4-day weeks',
//       'Business productivity consultants'
//     ],
//     target_audience: ['Working professionals', 'HR managers', 'Business owners'],
//     estimated_reach: 120000,
//     urgency: 'medium',
//     references: mockReferences.slice(1, 2)
//   }
// ];

// export const mockAnalytics: AnalyticsData = {
//   trending_topics_count: 24,
//   total_engagement: 847520,
//   top_performing_subreddits: [
//     { name: 'worldnews', posts: 156, engagement: 234567 },
//     { name: 'technology', posts: 124, engagement: 198432 },
//     { name: 'science', posts: 98, engagement: 176543 },
//     { name: 'business', posts: 87, engagement: 134567 },
//     { name: 'politics', posts: 76, engagement: 103211 }
//   ],
//   sentiment_distribution: { positive: 45, negative: 25, neutral: 30 },
//   hourly_activity: Array.from({ length: 24 }, (_, hour) => ({
//     hour,
//     posts: Math.floor(Math.random() * 50) + 10,
//     engagement: Math.floor(Math.random() * 5000) + 1000
//   }))
// };