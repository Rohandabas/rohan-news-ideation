import React, { useState, useMemo } from 'react';
import Header from './components/Layout/Header';
import Sidebar from './components/Layout/Sidebar';
import StatsCard from './components/Dashboard/StatsCard';
import TrendChart from './components/Dashboard/TrendChart';
import TopSubreddits from './components/Dashboard/TopSubreddits';
import TrendCard from './components/Trending/TrendCard';
import StoryCard from './components/Stories/StoryCard';
import ReferenceCard from './components/References/ReferenceCard';
import Modal from './components/Common/Modal';
import LoadingSpinner from './components/Common/LoadingSpinner';
import ErrorMessage from './components/Common/ErrorMessage';
import {
  TrendingUp,
  FileText,
  Users,
  Target,
  Clock,
  MessageCircle,
  ThumbsUp,
  ExternalLink
} from 'lucide-react';
import { TrendingTopic, StoryIdea } from './types';
import { formatDistanceToNow } from 'date-fns';
import { useRealTimeData } from './hooks/useRealTimeData';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedTopic, setSelectedTopic] = useState<TrendingTopic | null>(null);
  const [selectedStory, setSelectedStory] = useState<StoryIdea | null>(null);

  const {
    trendingTopics,
    storyIdeas,
    analytics,
    references,
    loading,
    error,
    lastUpdated,
    refreshData
  } = useRealTimeData();

  const filteredTopics = useMemo(() => {
    if (!searchQuery) return trendingTopics;
    return trendingTopics.filter(topic =>
      topic.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      topic.keywords.some(keyword => keyword.toLowerCase().includes(searchQuery.toLowerCase())) ||
      topic.subreddits.some(subreddit => subreddit.toLowerCase().includes(searchQuery.toLowerCase()))
    );
  }, [searchQuery, trendingTopics]);

  const filteredStories = useMemo(() => {
    if (!searchQuery) return storyIdeas;
    return storyIdeas.filter(story =>
      story.headline.toLowerCase().includes(searchQuery.toLowerCase()) ||
      story.angle.toLowerCase().includes(searchQuery.toLowerCase())
    );
  }, [searchQuery, storyIdeas]);

  const filteredReferences = useMemo(() => {
    if (!searchQuery) return references;
    return references.filter(ref =>
      ref.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      ref.source.toLowerCase().includes(searchQuery.toLowerCase())
    );
  }, [searchQuery, references]);

  const renderDashboard = () => {
    if (loading && trendingTopics.length === 0) {
      return (
        <div className="flex items-center justify-center h-96">
          <LoadingSpinner size="lg" text="Fetching live data from Reddit..." />
        </div>
      );
    }

    if (error && trendingTopics.length === 0) {
      return <ErrorMessage message={error} onRetry={refreshData} />;
    }

    return (
      <div className="space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <StatsCard
            title="Trending Topics"
            value={analytics.trending_topics_count}
            change="+12%"
            trend="up"
            icon={TrendingUp}
            color="blue"
          />
          <StatsCard
            title="Story Ideas"
            value={storyIdeas.length}
            change="+8%"
            trend="up"
            icon={FileText}
            color="green"
          />
          <StatsCard
            // title="Total Engagement"
            // value={analytics.total_engagement.toLocaleString()}
            // change="+23%"
            // trend="up"
            // icon={Users}
            // color="purple"
            title="Total Engagement"
            value={
              analytics?.total_engagement !== undefined
                ? analytics.total_engagement.toLocaleString()
                : "Loading..."
            }
            change="+23%"
            trend="up"
            icon={Users}
            color="purple"
          />
          <StatsCard
            title="Active Subreddits"
            value={analytics.top_performing_subreddits?.length || 0}
            change="+5%"
            trend="up"
            icon={Target}
            color="orange"
          />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <TrendChart
            title="24-Hour Activity Trends"
            data={analytics.hourly_activity || []}
          />
          <TopSubreddits subreddits={analytics.top_performing_subreddits || []} />
        </div>

        <div>
          <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Latest Trending Topics</h2>
          {trendingTopics.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {trendingTopics.slice(0, 4).map((topic) => (
                <TrendCard key={topic.id} topic={topic} onClick={setSelectedTopic} />
              ))}
            </div>
          ) : (
            <div className="text-center py-8">
              <p className="text-gray-500 dark:text-gray-400">No trending topics available yet.</p>
            </div>
          )}
        </div>
      </div>
    );
  };

  const renderTrending = () => (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-semibold text-gray-900 dark:text-white">Live Trending Topics</h2>
        <div className="text-sm text-gray-500 dark:text-gray-400">
          {filteredTopics.length} topics found
        </div>
      </div>

      {loading && filteredTopics.length === 0 ? (
        <div className="flex items-center justify-center h-64">
          <LoadingSpinner size="lg" text="Loading trending topics..." />
        </div>
      ) : filteredTopics.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
          {filteredTopics.map((topic) => (
            <TrendCard key={topic.id} topic={topic} onClick={setSelectedTopic} />
          ))}
        </div>
      ) : (
        <div className="text-center py-12">
          <p className="text-gray-500 dark:text-gray-400">No trending topics match your search.</p>
        </div>
      )}
    </div>
  );

  const renderStories = () => (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-semibold text-gray-900 dark:text-white">AI-Generated Story Ideas</h2>
        <div className="text-sm text-gray-500 dark:text-gray-400">
          {filteredStories.length} stories generated
        </div>
      </div>

      {loading && filteredStories.length === 0 ? (
        <div className="flex items-center justify-center h-64">
          <LoadingSpinner size="lg" text="Generating story ideas..." />
        </div>
      ) : filteredStories.length > 0 ? (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {filteredStories.map((story) => (
            <StoryCard key={story.id} story={story} onClick={setSelectedStory} />
          ))}
        </div>
      ) : (
        <div className="text-center py-12">
          <p className="text-gray-500 dark:text-gray-400">No story ideas match your search.</p>
        </div>
      )}
    </div>
  );

  const renderReferences = () => (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-semibold text-gray-900 dark:text-white">Reference Library</h2>
        <div className="text-sm text-gray-500 dark:text-gray-400">
          {filteredReferences.length} references collected
        </div>
      </div>

      {loading && filteredReferences.length === 0 ? (
        <div className="flex items-center justify-center h-64">
          <LoadingSpinner size="lg" text="Loading references..." />
        </div>
      ) : filteredReferences.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {filteredReferences.map((reference) => (
            <ReferenceCard key={reference.id} reference={reference} />
          ))}
        </div>
      ) : (
        <div className="text-center py-12">
          <p className="text-gray-500 dark:text-gray-400">No references match your search.</p>
        </div>
      )}
    </div>
  );

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return renderDashboard();
      case 'trending':
        return renderTrending();
      case 'stories':
        return renderStories();
      case 'references':
        return renderReferences();
      default:
        return (
          <div className="flex items-center justify-center h-96">
            <div className="text-center">
              <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
                Coming Soon
              </h3>
              <p className="text-gray-500 dark:text-gray-400">
                This feature is currently in development.
              </p>
            </div>
          </div>
        );
    }
  };

  return (
    <div className="h-screen bg-gray-50 dark:bg-gray-900 flex flex-col">
      <Header
        onSearch={setSearchQuery}
        onRefresh={refreshData}
        isRefreshing={loading}
        lastUpdated={lastUpdated}
      />

      <div className="flex-1 flex overflow-hidden">
        <Sidebar activeTab={activeTab} onTabChange={setActiveTab} />

        <main className="flex-1 overflow-y-auto p-6">
          {renderContent()}
        </main>
      </div>

      {/* Topic Detail Modal */}
      <Modal
        isOpen={!!selectedTopic}
        onClose={() => setSelectedTopic(null)}
        title={selectedTopic?.title || ''}
        maxWidth="2xl"
      >
        {selectedTopic && (
          <div className="space-y-6">
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                  {selectedTopic.engagement_score}
                </div>
                <div className="text-sm text-gray-500 dark:text-gray-400">Engagement Score</div>
              </div>
              <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                <div className="text-2xl font-bold text-green-600 dark:text-green-400">
                  {selectedTopic.trend_velocity.toFixed(1)}%
                </div>
                <div className="text-sm text-gray-500 dark:text-gray-400">Trend Velocity</div>
              </div>
            </div>

            <div>
              <h4 className="font-semibold text-gray-900 dark:text-white mb-3">Related Posts</h4>
              <div className="space-y-3">
                {selectedTopic.posts.map((post) => (
                  <div key={post.id} className="p-4 border border-gray-200 dark:border-gray-600 rounded-lg">
                    <h5 className="font-medium text-gray-900 dark:text-white mb-2">{post.title}</h5>
                    <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400">
                      <span>r/{post.subreddit} • u/{post.author}</span>
                      <div className="flex items-center space-x-4">
                        <div className="flex items-center space-x-1">
                          <ThumbsUp className="w-4 h-4" />
                          <span>{post.score.toLocaleString()}</span>
                        </div>
                        <div className="flex items-center space-x-1">
                          <MessageCircle className="w-4 h-4" />
                          <span>{post.comments.toLocaleString()}</span>
                        </div>
                        <div className="flex items-center space-x-1">
                          <Clock className="w-4 h-4" />
                          <span>{formatDistanceToNow(new Date(post.created_utc * 1000), { addSuffix: true })}</span>
                        </div>
                        <a
                          href={`https://reddit.com${post.permalink}`}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="flex items-center space-x-1 text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300"
                        >
                          <ExternalLink className="w-4 h-4" />
                        </a>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <h4 className="font-semibold text-gray-900 dark:text-white mb-3">Keywords</h4>
              <div className="flex flex-wrap gap-2">
                {selectedTopic.keywords.map((keyword) => (
                  <span key={keyword} className="px-3 py-1 bg-blue-100 dark:bg-blue-900/20 text-blue-800 dark:text-blue-300 rounded-full text-sm">
                    {keyword}
                  </span>
                ))}
              </div>
            </div>
          </div>
        )}
      </Modal>

      {/* Story Detail Modal */}
      <Modal
        isOpen={!!selectedStory}
        onClose={() => setSelectedStory(null)}
        title={selectedStory?.headline || ''}
        maxWidth="2xl"
      >
        {selectedStory && (
          <div className="space-y-6">
            <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
              <h4 className="font-semibold text-gray-900 dark:text-white mb-2">Story Angle</h4>
              <p className="text-gray-600 dark:text-gray-400">{selectedStory.angle}</p>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
              {Object.entries(selectedStory.news_value).map(([key, value]) => (
                <div key={key} className="text-center p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                  <div className="text-xl font-bold text-blue-600 dark:text-blue-400">{value}</div>
                  <div className="text-xs text-gray-500 dark:text-gray-400 capitalize">
                    {key.replace('_', ' ')}
                  </div>
                </div>
              ))}
            </div>

            <div>
              <h4 className="font-semibold text-gray-900 dark:text-white mb-3">Suggested Sources</h4>
              <div className="space-y-2">
                {selectedStory.suggested_sources.map((source, index) => (
                  <div key={index} className="flex items-center space-x-2 p-2 bg-gray-50 dark:bg-gray-700 rounded">
                    <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                    <span className="text-gray-700 dark:text-gray-300">{source}</span>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <h4 className="font-semibold text-gray-900 dark:text-white mb-3">Target Audience</h4>
              <div className="flex flex-wrap gap-2">
                {selectedStory.target_audience.map((audience) => (
                  <span key={audience} className="px-3 py-1 bg-green-100 dark:bg-green-900/20 text-green-800 dark:text-green-300 rounded-full text-sm">
                    {audience}
                  </span>
                ))}
              </div>
            </div>

            <div className="flex items-center justify-between pt-4 border-t border-gray-200 dark:border-gray-600">
              <div className="text-sm text-gray-500 dark:text-gray-400">
                Estimated Reach: {selectedStory.estimated_reach.toLocaleString()}
              </div>
              <div className="text-sm font-medium text-gray-900 dark:text-white">
                Urgency: <span className="capitalize">{selectedStory.urgency}</span>
              </div>
            </div>
          </div>
        )}
      </Modal>
    </div>
  );
}

export default App;