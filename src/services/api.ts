const API_BASE_URL = 'http://localhost:5000/api';

export interface ApiResponse<T> {
  data?: T;
  error?: string;
  last_updated?: string;
}

class ApiService {
  private async fetchWithErrorHandling<T>(url: string): Promise<ApiResponse<T>> {
    try {
      const response = await fetch(`${API_BASE_URL}${url}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return { data, last_updated: data.last_updated };
    } catch (error) {
      console.error(`API Error for ${url}:`, error);
      return { 
        error: error instanceof Error ? error.message : 'Unknown error occurred' 
      };
    }
  }

  async getTrendingTopics() {
    const response = await this.fetchWithErrorHandling('/trending');
    return response.data?.topics || [];
  }

  async getStoryIdeas() {
    const response = await this.fetchWithErrorHandling('/stories');
    return response.data?.stories || [];
  }

  async getAnalytics() {
    const response = await this.fetchWithErrorHandling('/analytics');
    return response.data?.analytics || {};
  }

  async getReferences() {
    const response = await this.fetchWithErrorHandling('/references');
    return response.data?.references || [];
  }

  async getSubredditPosts(subreddit: string, limit: number = 20) {
    const response = await this.fetchWithErrorHandling(`/subreddit/${subreddit}?limit=${limit}`);
    return response.data?.posts || [];
  }

  async refreshData() {
    try {
      const response = await fetch(`${API_BASE_URL}/refresh`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error refreshing data:', error);
      return { success: false, message: 'Failed to refresh data' };
    }
  }

  async getStatus() {
    const response = await this.fetchWithErrorHandling('/status');
    return response.data || {};
  }
}

export const apiService = new ApiService();