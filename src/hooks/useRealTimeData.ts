import { useState, useEffect, useCallback } from 'react';
import { apiService } from '../services/api';
import { TrendingTopic, StoryIdea, AnalyticsData, Reference } from '../types';

interface UseRealTimeDataReturn {
  trendingTopics: TrendingTopic[];
  storyIdeas: StoryIdea[];
  analytics: AnalyticsData;
  references: Reference[];
  loading: boolean;
  error: string | null;
  lastUpdated: string | null;
  refreshData: () => Promise<void>;
}

export function useRealTimeData(): UseRealTimeDataReturn {
  const [trendingTopics, setTrendingTopics] = useState<TrendingTopic[]>([]);
  const [storyIdeas, setStoryIdeas] = useState<StoryIdea[]>([]);
  const [analytics, setAnalytics] = useState<AnalyticsData>({
    trending_topics_count: 0,
    total_engagement: 0,
    top_performing_subreddits: [],
    sentiment_distribution: { positive: 0, negative: 0, neutral: 0 },
    hourly_activity: []
  });
  const [references, setReferences] = useState<Reference[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdated, setLastUpdated] = useState<string | null>(null);

  const fetchAllData = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);

      // Fetch all data in parallel
      const [topicsData, storiesData, analyticsData, referencesData] = await Promise.all([
        apiService.getTrendingTopics(),
        apiService.getStoryIdeas(),
        apiService.getAnalytics(),
        apiService.getReferences()
      ]);

      setTrendingTopics(topicsData);
      setStoryIdeas(storiesData);
      setAnalytics(analyticsData);
      setReferences(referencesData);
      setLastUpdated(new Date().toISOString());

    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch data');
      console.error('Error fetching real-time data:', err);
    } finally {
      setLoading(false);
    }
  }, []);

  const refreshData = useCallback(async () => {
    try {
      setLoading(true);
      const result = await apiService.refreshData();
      
      if (result.success) {
        // Fetch updated data after refresh
        await fetchAllData();
      } else {
        setError(result.message || 'Failed to refresh data');
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to refresh data');
    } finally {
      setLoading(false);
    }
  }, [fetchAllData]);

  // Initial data fetch
  useEffect(() => {
    fetchAllData();
  }, [fetchAllData]);

  // Set up polling for real-time updates (every 5 minutes)
  useEffect(() => {
    const interval = setInterval(() => {
      fetchAllData();
    }, 5 * 60 * 1000); // 5 minutes

    return () => clearInterval(interval);
  }, [fetchAllData]);

  return {
    trendingTopics,
    storyIdeas,
    analytics,
    references,
    loading,
    error,
    lastUpdated,
    refreshData
  };
}