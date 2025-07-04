# TrendScout - Real-time Reddit Content Ideation Platform

TrendScout is a comprehensive content ideation platform that analyzes real-time Reddit trends to help newsrooms identify story opportunities, generate content ideas, and track social media engagement.

Live at: https://trendscout-seven.vercel.app/

## 🚀 Features

### Frontend (React + TypeScript)
- **Real-time Dashboard** - Live analytics and trending topics
- **Trending Topics Analysis** - AI-powered topic identification and clustering
- **Story Idea Generation** - Automated story suggestions with news value scoring
- **Reference Management** - Curated source collection and relevance scoring
- **Advanced Search & Filtering** - Multi-parameter content discovery
- **Responsive Design** - Optimized for newsroom workflows
- **Dark/Light Theme** - Professional interface with accessibility features

### Backend (Python + PRAW)
- **Live Reddit Data Fetching** - Real-time post monitoring across 15+ subreddits
- **Sentiment Analysis** - TextBlob-powered emotion detection
- **Engagement Scoring** - Multi-factor trending algorithm
- **News Value Calculation** - Automated story worthiness assessment
- **Topic Clustering** - Smart grouping of related posts
- **RESTful API** - Complete data access endpoints
- **Auto-refresh** - Scheduled updates every 15 minutes

## 🛠 Installation & Setup

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- Reddit API credentials

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Reddit API credentials:**
   Create a `.env` file with your Reddit API credentials:
   ```env
   REDDIT_CLIENT_ID=WGvo1YkcGNns8ASALO7UZg
   REDDIT_CLIENT_SECRET=HPlJ_ZUXt-nUfusfbmthCoirTxUBMA
   REDDIT_USER_AGENT=trendfetcher by u/Recent-Accountant627
   FLASK_PORT=5000
   ```

4. **Start the backend server:**
   ```bash
   python run.py
   ```

   The backend will:
   - Install required packages automatically
   - Start fetching data from Reddit
   - Launch the API server on http://localhost:5000
   - Begin scheduled updates every 15 minutes

### Frontend Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Access the application:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:5000

## 📊 API Endpoints

### Core Data Endpoints
- `GET /api/trending` - Fetch trending topics
- `GET /api/stories` - Get AI-generated story ideas  
- `GET /api/analytics` - Retrieve engagement analytics
- `GET /api/references` - Access reference library

### Utility Endpoints
- `GET /api/subreddit/{name}` - Get posts from specific subreddit
- `POST /api/refresh` - Manually refresh data
- `GET /api/status` - Check system status

## 🎯 Monitored Subreddits

The system monitors these high-value subreddits for news content:
- worldnews, technology, science, business, politics
- news, economics, environment, health, education  
- space, artificial, programming, startups, investing

## 🧠 AI Features

### News Value Scoring
Stories are automatically scored across six journalism criteria:
- **Timeliness** - How recent and time-sensitive
- **Proximity** - Local relevance and geographic impact
- **Impact** - Scope of effect on audience
- **Prominence** - Involvement of notable figures/organizations
- **Conflict** - Controversy and debate potential
- **Human Interest** - Emotional connection and relatability

### Story Angle Generation
AI suggests multiple story approaches:
- Local impact analysis
- Economic implications
- Policy and regulatory angles
- Human interest perspectives
- Industry disruption analysis

### Engagement Prediction
Advanced algorithms predict story performance based on:
- Reddit engagement patterns
- Sentiment analysis
- Topic clustering
- Historical performance data

## 🔧 Configuration

### Backend Configuration (`config.py`)
- Monitored subreddits list
- News value keywords and weights
- API rate limiting settings
- Update frequency controls

### Frontend Configuration
- API endpoint URLs
- Polling intervals
- UI theme settings
- Search parameters

## 📈 Analytics & Insights

### Real-time Metrics
- Trending topic counts
- Total engagement scores
- Subreddit performance rankings
- Sentiment distribution analysis
- 24-hour activity patterns

### Story Intelligence
- News value breakdowns
- Audience targeting suggestions
- Source recommendation engine
- Urgency classification system
- Reach estimation algorithms

## 🚀 Production Deployment

### Backend Deployment
1. Set up Python environment with production WSGI server
2. Configure environment variables securely
3. Set up database for persistent storage (recommended)
4. Implement proper logging and monitoring
5. Configure reverse proxy (nginx recommended)

### Frontend Deployment
1. Build production bundle: `npm run build`
2. Deploy to static hosting (Netlify, Vercel, etc.)
3. Configure API endpoint URLs for production
4. Set up CDN for optimal performance

## 🔒 Security Considerations

- Reddit API credentials stored securely in environment variables
- CORS properly configured for cross-origin requests
- Rate limiting implemented to respect Reddit API limits
- Input validation on all API endpoints
- Error handling prevents sensitive data exposure

## 📝 Usage Tips

### For Newsroom Editors
- Monitor the dashboard for breaking trends
- Use story urgency indicators for editorial prioritization
- Leverage suggested sources for comprehensive coverage
- Track engagement predictions for content planning

### For Journalists
- Explore trending topics for story inspiration
- Use reference links for background research
- Follow suggested story angles for unique perspectives
- Monitor sentiment analysis for public opinion insights

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
1. Check the API status endpoint: `/api/status`
2. Review backend logs for Reddit API connectivity
3. Verify environment variables are properly configured
4. Ensure all dependencies are installed correctly

---

**TrendScout** - Transforming social media trends into newsroom opportunities through AI-powered content analysis.
