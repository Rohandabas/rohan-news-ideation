# import random
# from datetime import datetime
# from textblob import TextBlob

# class StoryGenerator:
#     def __init__(self):
#         self.story_angles = {
#             'Technology': [
#                 'How this technology could impact local businesses',
#                 'What this means for job markets in the region',
#                 'Privacy and security implications for consumers',
#                 'Economic opportunities and challenges ahead'
#             ],
#             'Politics': [
#                 'Local political implications and reactions',
#                 'How this affects upcoming elections',
#                 'Economic impact on different demographics',
#                 'Historical context and precedent analysis'
#             ],
#             'Science': [
#                 'Practical applications in everyday life',
#                 'Funding and research implications',
#                 'Ethical considerations and public debate',
#                 'Timeline for real-world implementation'
#             ],
#             'Business': [
#                 'Market disruption and competitive landscape',
#                 'Consumer behavior and spending patterns',
#                 'Regulatory challenges and opportunities',
#                 'Investment and growth potential analysis'
#             ],
#             'Health': [
#                 'Public health policy implications',
#                 'Healthcare system impact and costs',
#                 'Patient advocacy and access issues',
#                 'Prevention and treatment innovations'
#             ],
#             'Environment': [
#                 'Climate change mitigation strategies',
#                 'Economic costs of environmental action',
#                 'Community and lifestyle impacts',
#                 'Policy and regulatory responses needed'
#             ]
#         }
        
#         self.target_audiences = {
#             'Technology': ['Tech professionals', 'Business leaders', 'General consumers'],
#             'Politics': ['Voters', 'Policy makers', 'Political activists'],
#             'Science': ['Researchers', 'Students', 'General public'],
#             'Business': ['Investors', 'Entrepreneurs', 'Business owners'],
#             'Health': ['Patients', 'Healthcare workers', 'Policy makers'],
#             'Environment': ['Environmental advocates', 'Policy makers', 'General public']
#         }
        
#         self.source_types = {
#             'Technology': ['Tech industry experts', 'Academic researchers', 'Company executives', 'Consumer advocates'],
#             'Politics': ['Political analysts', 'Elected officials', 'Policy experts', 'Affected constituents'],
#             'Science': ['Research scientists', 'University professors', 'Industry experts', 'Ethics specialists'],
#             'Business': ['Industry analysts', 'Company executives', 'Economic experts', 'Market researchers'],
#             'Health': ['Medical professionals', 'Public health experts', 'Patient advocates', 'Healthcare administrators'],
#             'Environment': ['Environmental scientists', 'Policy experts', 'Community leaders', 'Industry representatives']
#         }
    
#     def generate_story_ideas(self, trending_topics):
#         """Generate story ideas from trending topics"""
#         story_ideas = []
        
#         for topic in trending_topics[:10]:  # Top 10 topics
#             story_idea = self._create_story_from_topic(topic)
#             if story_idea:
#                 story_ideas.append(story_idea)
        
#         return story_ideas
    
#     def _create_story_from_topic(self, topic):
#         """Create a story idea from a trending topic"""
#         category = topic['category']
#         main_post = max(topic['posts'], key=lambda x: x['engagement_score'])
        
#         # Generate headline variations
#         headlines = self._generate_headlines(main_post, topic)
#         selected_headline = random.choice(headlines)
        
#         # Select story angle
#         angles = self.story_angles.get(category, self.story_angles['Technology'])
#         selected_angle = random.choice(angles)
        
#         # Calculate news value scores
#         news_value = self._calculate_detailed_news_value(topic, main_post)
        
#         # Determine urgency
#         urgency = self._determine_urgency(topic, news_value)
        
#         # Get suggested sources
#         sources = self.source_types.get(category, self.source_types['Technology'])
#         suggested_sources = random.sample(sources, min(4, len(sources)))
        
#         # Get target audience
#         audiences = self.target_audiences.get(category, self.target_audiences['Technology'])
        
#         # Estimate reach based on engagement
#         base_reach = sum(post['engagement_score'] for post in topic['posts']) * 100
#         estimated_reach = min(500000, max(10000, base_reach))
        
#         return {
#             'id': f"story-{topic['id']}",
#             'topic_id': topic['id'],
#             'headline': selected_headline,
#             'angle': selected_angle,
#             'news_value': news_value,
#             'suggested_sources': suggested_sources,
#             'target_audience': audiences,
#             'estimated_reach': estimated_reach,
#             'urgency': urgency,
#             'references': self._generate_references(topic)
#         }
    
#     def _generate_headlines(self, main_post, topic):
#         """Generate multiple headline options"""
#         original_title = main_post['title']
#         category = topic['category']
        
#         headlines = [original_title]
        
#         # Question-based headlines
#         if category == 'Technology':
#             headlines.append(f"Is {original_title.split()[0]} the Future of Technology?")
#             headlines.append(f"What {original_title} Means for Your Digital Life")
#         elif category == 'Politics':
#             headlines.append(f"How {original_title} Could Change Everything")
#             headlines.append(f"The Political Implications of {original_title}")
#         elif category == 'Business':
#             headlines.append(f"Why {original_title} Matters to Your Wallet")
#             headlines.append(f"The Economic Impact of {original_title}")
        
#         # Impact-focused headlines
#         headlines.append(f"Breaking Down {original_title}: What You Need to Know")
#         headlines.append(f"The Real Story Behind {original_title}")
        
#         return headlines[:3]  # Return top 3 options
    
#     def _calculate_detailed_news_value(self, topic, main_post):
#         """Calculate detailed news value scores"""
#         # Timeliness - how recent is the story
#         hours_old = (datetime.now().timestamp() - main_post['created_utc']) / 3600
#         timeliness = max(20, 100 - (hours_old * 2))
        
#         # Impact - based on engagement and reach
#         impact = min(100, topic['engagement_score'])
        
#         # Prominence - based on subreddit and post score
#         prominence = min(100, main_post['score'] / 100)
        
#         # Proximity - assume moderate local relevance
#         proximity = random.randint(40, 80)
        
#         # Conflict - based on sentiment and comments
#         conflict_indicators = main_post['comments'] / max(1, main_post['score'])
#         conflict = min(100, conflict_indicators * 50)
        
#         # Human interest - based on story type and engagement
#         human_interest = random.randint(50, 90)
        
#         return {
#             'timeliness': int(timeliness),
#             'proximity': int(proximity),
#             'impact': int(impact),
#             'prominence': int(prominence),
#             'conflict': int(conflict),
#             'human_interest': int(human_interest)
#         }
    
#     def _determine_urgency(self, topic, news_value):
#         """Determine story urgency"""
#         avg_news_value = sum(news_value.values()) / len(news_value)
#         hours_old = (datetime.now().timestamp() - (topic['peak_time'] / 1000)) / 3600
        
#         if avg_news_value > 80 and hours_old < 6:
#             return 'breaking'
#         elif avg_news_value > 70 and hours_old < 12:
#             return 'high'
#         elif avg_news_value > 50:
#             return 'medium'
#         else:
#             return 'low'
    
#     def _generate_references(self, topic):
#         """Generate reference suggestions"""
#         references = []
        
#         # Use actual Reddit posts as references
#         for i, post in enumerate(topic['posts'][:3]):
#             ref_type = 'social_media' if post['subreddit'] in ['twitter', 'facebook'] else 'article'
            
#             reference = {
#                 'id': f"ref-{post['id']}",
#                 'title': post['title'],
#                 'url': f"https://reddit.com{post['permalink']}",
#                 'source': f"Reddit - r/{post['subreddit']}",
#                 'date': datetime.fromtimestamp(post['created_utc']).strftime('%Y-%m-%d'),
#                 'relevance_score': min(100, post['engagement_score']),
#                 'type': ref_type
#             }
#             references.append(reference)
        
#         return references



# import random
# from datetime import datetime
# from textblob import TextBlob
# import requests  # Added for Gemini API calls
# from config import Config  # Added to load Gemini API key

# class StoryGenerator:
#     def __init__(self):
#         self.story_angles = {
#             'Technology': [
#                 'How this technology could impact local businesses',
#                 'What this means for job markets in the region',
#                 'Privacy and security implications for consumers',
#                 'Economic opportunities and challenges ahead'
#             ],
#             'Politics': [
#                 'Local political implications and reactions',
#                 'How this affects upcoming elections',
#                 'Economic impact on different demographics',
#                 'Historical context and precedent analysis'
#             ],
#             'Science': [
#                 'Practical applications in everyday life',
#                 'Funding and research implications',
#                 'Ethical considerations and public debate',
#                 'Timeline for real-world implementation'
#             ],
#             'Business': [
#                 'Market disruption and competitive landscape',
#                 'Consumer behavior and spending patterns',
#                 'Regulatory challenges and opportunities',
#                 'Investment and growth potential analysis'
#             ],
#             'Health': [
#                 'Public health policy implications',
#                 'Healthcare system impact and costs',
#                 'Patient advocacy and access issues',
#                 'Prevention and treatment innovations'
#             ],
#             'Environment': [
#                 'Climate change mitigation strategies',
#                 'Economic costs of environmental action',
#                 'Community and lifestyle impacts',
#                 'Policy and regulatory responses needed'
#             ]
#         }
        
#         self.target_audiences = {
#             'Technology': ['Tech professionals', 'Business leaders', 'General consumers'],
#             'Politics': ['Voters', 'Policy makers', 'Political activists'],
#             'Science': ['Researchers', 'Students', 'General public'],
#             'Business': ['Investors', 'Entrepreneurs', 'Business owners'],
#             'Health': ['Patients', 'Healthcare workers', 'Policy makers'],
#             'Environment': ['Environmental advocates', 'Policy makers', 'General public']
#         }
        
#         self.source_types = {
#             'Technology': ['Tech industry experts', 'Academic researchers', 'Company executives', 'Consumer advocates'],
#             'Politics': ['Political analysts', 'Elected officials', 'Policy experts', 'Affected constituents'],
#             'Science': ['Research scientists', 'University professors', 'Industry experts', 'Ethics specialists'],
#             'Business': ['Industry analysts', 'Company executives', 'Economic experts', 'Market researchers'],
#             'Health': ['Medical professionals', 'Public health experts', 'Patient advocates', 'Healthcare administrators'],
#             'Environment': ['Environmental scientists', 'Policy experts', 'Community leaders', 'Industry representatives']
#         }
#         # Gemini API configuration
#         self.gemini_api_key = Config.GEMINI_API_KEY  # Load from config.py
#         self.gemini_api_url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"  # Correct endpoint

#     def _call_gemini_api(self, prompt):
#         """Call the Gemini API to generate reasons for newsroom coverage."""
#         headers = {
#             "Authorization": f"Bearer {self.gemini_api_key}",
#             "Content-Type": "application/json"
#         }
#         payload = {
#             "contents": [{"parts": [{"text": prompt}]}],
#             "generationConfig": {
#                 "maxOutputTokens": 200,
#                 "temperature": 0.7
#             }
#         }

#         try:
#             response = requests.post(self.gemini_api_url, json=payload, headers=headers)
#             response.raise_for_status()
#             result = response.json()
#             # Adjust based on actual response structure (e.g., result['candidates'][0]['content']['parts'][0]['text'])
#             reasons = result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "No reasons generated.")
#             return reasons.split("\n") if isinstance(reasons, str) else ["No reasons generated."]
#         except requests.exceptions.RequestException as e:
#             print(f"Error calling Gemini API: {e}")
#             return ["Unable to generate reasons due to API error."]

#     def generate_story_ideas(self, trending_topics):
#         """Generate story ideas from trending topics with newsroom reasons."""
#         story_ideas = []
        
#         for topic in trending_topics[:10]:  # Top 10 topics
#             story_idea = self._create_story_from_topic(topic)
#             if story_idea:
#                 # Generate reasons for newsroom coverage using Gemini
#                 prompt = f"Provide 2-3 concise reasons why a newsroom should write a story on the following trending topic: Title: {topic['title']}, Category: {topic['category']}, Engagement Score: {topic['engagement_score']}, Subreddits: {', '.join(topic['subreddits'])}, Sentiment: {topic['sentiment']}. Focus on public interest, timeliness, and market impact."
#                 reasons = self._call_gemini_api(prompt)
#                 story_idea['reasons_for_coverage'] = [r.strip() for r in reasons if r.strip()]
#                 story_ideas.append(story_idea)
        
#         return story_ideas
    
#     def _create_story_from_topic(self, topic):
#         """Create a story idea from a trending topic"""
#         category = topic['category']
#         main_post = max(topic['posts'], key=lambda x: x['engagement_score'])
        
#         # Generate headline variations
#         headlines = self._generate_headlines(main_post, topic)
#         selected_headline = random.choice(headlines)
        
#         # Select story angle
#         angles = self.story_angles.get(category, self.story_angles['Technology'])
#         selected_angle = random.choice(angles)
        
#         # Calculate news value scores
#         news_value = self._calculate_detailed_news_value(topic, main_post)
        
#         # Determine urgency
#         urgency = self._determine_urgency(topic, news_value)
        
#         # Get suggested sources
#         sources = self.source_types.get(category, self.source_types['Technology'])
#         suggested_sources = random.sample(sources, min(4, len(sources)))
        
#         # Get target audience
#         audiences = self.target_audiences.get(category, self.target_audiences['Technology'])
        
#         # Estimate reach based on engagement
#         base_reach = sum(post['engagement_score'] for post in topic['posts']) * 100
#         estimated_reach = min(500000, max(10000, base_reach))
        
#         return {
#             'id': f"story-{topic['id']}",
#             'topic_id': topic['id'],
#             'headline': selected_headline,
#             'angle': selected_angle,
#             'news_value': news_value,
#             'suggested_sources': suggested_sources,
#             'target_audience': audiences,
#             'estimated_reach': estimated_reach,
#             'urgency': urgency,
#             'references': self._generate_references(topic),
#             'reasons_for_coverage': []  # Initialize with empty list for Gemini reasons
#         }
    
#     def _generate_headlines(self, main_post, topic):
#         """Generate multiple headline options"""
#         original_title = main_post['title']
#         category = topic['category']
        
#         headlines = [original_title]
        
#         # Question-based headlines
#         if category == 'Technology':
#             headlines.append(f"Is {original_title.split()[0]} the Future of Technology?")
#             headlines.append(f"What {original_title} Means for Your Digital Life")
#         elif category == 'Politics':
#             headlines.append(f"How {original_title} Could Change Everything")
#             headlines.append(f"The Political Implications of {original_title}")
#         elif category == 'Business':
#             headlines.append(f"Why {original_title} Matters to Your Wallet")
#             headlines.append(f"The Economic Impact of {original_title}")
        
#         # Impact-focused headlines
#         headlines.append(f"Breaking Down {original_title}: What You Need to Know")
#         headlines.append(f"The Real Story Behind {original_title}")
        
#         return headlines[:3]  # Return top 3 options
    
#     def _calculate_detailed_news_value(self, topic, main_post):
#         """Calculate detailed news value scores"""
#         # Timeliness - how recent is the story
#         hours_old = (datetime.now().timestamp() - main_post['created_utc']) / 3600
#         timeliness = max(20, 100 - (hours_old * 2))
        
#         # Impact - based on engagement and reach
#         impact = min(100, topic['engagement_score'])
        
#         # Prominence - based on subreddit and post score
#         prominence = min(100, main_post['score'] / 100)
        
#         # Proximity - assume moderate local relevance
#         proximity = random.randint(40, 80)
        
#         # Conflict - based on sentiment and comments
#         conflict_indicators = main_post['comments'] / max(1, main_post['score'])
#         conflict = min(100, conflict_indicators * 50)
        
#         # Human interest - based on story type and engagement
#         human_interest = random.randint(50, 90)
        
#         return {
#             'timeliness': int(timeliness),
#             'proximity': int(proximity),
#             'impact': int(impact),
#             'prominence': int(prominence),
#             'conflict': int(conflict),
#             'human_interest': int(human_interest)
#         }
    
#     def _determine_urgency(self, topic, news_value):
#         """Determine story urgency"""
#         avg_news_value = sum(news_value.values()) / len(news_value)
#         hours_old = (datetime.now().timestamp() - (topic['peak_time'] / 1000)) / 3600
        
#         if avg_news_value > 80 and hours_old < 6:
#             return 'breaking'
#         elif avg_news_value > 70 and hours_old < 12:
#             return 'high'
#         elif avg_news_value > 50:
#             return 'medium'
#         else:
#             return 'low'
    
#     def _generate_references(self, topic):
#         """Generate reference suggestions"""
#         references = []
        
#         # Use actual Reddit posts as references
#         for i, post in enumerate(topic['posts'][:3]):
#             ref_type = 'social_media' if post['subreddit'] in ['twitter', 'facebook'] else 'article'
            
#             reference = {
#                 'id': f"ref-{post['id']}",
#                 'title': post['title'],
#                 'url': f"https://reddit.com{post['permalink']}",
#                 'source': f"Reddit - r/{post['subreddit']}",
#                 'date': datetime.fromtimestamp(post['created_utc']).strftime('%Y-%m-%d'),
#                 'relevance_score': min(100, post['engagement_score']),
#                 'type': ref_type
#             }
#             references.append(reference)
        
#         return references
























# import random
# from datetime import datetime
# from textblob import TextBlob
# import requests
# from config import Config  # Added to load Gemini API key
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class StoryGenerator:
#     def __init__(self):
#         self.story_angles = {
#             'Technology': [
#                 'How this technology could impact local businesses',
#                 'What this means for job markets in the region',
#                 'Privacy and security implications for consumers',
#                 'Economic opportunities and challenges ahead'
#             ],
#             'Politics': [
#                 'Local political implications and reactions',
#                 'How this affects upcoming elections',
#                 'Economic impact on different demographics',
#                 'Historical context and precedent analysis'
#             ],
#             'Science': [
#                 'Practical applications in everyday life',
#                 'Funding and research implications',
#                 'Ethical considerations and public debate',
#                 'Timeline for real-world implementation'
#             ],
#             'Business': [
#                 'Market disruption and competitive landscape',
#                 'Consumer behavior and spending patterns',
#                 'Regulatory challenges and opportunities',
#                 'Investment and growth potential analysis'
#             ],
#             'Health': [
#                 'Public health policy implications',
#                 'Healthcare system impact and costs',
#                 'Patient advocacy and access issues',
#                 'Prevention and treatment innovations'
#             ],
#             'Environment': [
#                 'Climate change mitigation strategies',
#                 'Economic costs of environmental action',
#                 'Community and lifestyle impacts',
#                 'Policy and regulatory responses needed'
#             ]
#         }
        
#         self.target_audiences = {
#             'Technology': ['Tech professionals', 'Business leaders', 'General consumers'],
#             'Politics': ['Voters', 'Policy makers', 'Political activists'],
#             'Science': ['Researchers', 'Students', 'General public'],
#             'Business': ['Investors', 'Entrepreneurs', 'Business owners'],
#             'Health': ['Patients', 'Healthcare workers', 'Policy makers'],
#             'Environment': ['Environmental advocates', 'Policy makers', 'General public']
#         }
        
#         self.source_types = {
#             'Technology': ['Tech industry experts', 'Academic researchers', 'Company executives', 'Consumer advocates'],
#             'Politics': ['Political analysts', 'Elected officials', 'Policy experts', 'Affected constituents'],
#             'Science': ['Research scientists', 'University professors', 'Industry experts', 'Ethics specialists'],
#             'Business': ['Industry analysts', 'Company executives', 'Economic experts', 'Market researchers'],
#             'Health': ['Medical professionals', 'Public health experts', 'Patient advocates', 'Healthcare administrators'],
#             'Environment': ['Environmental scientists', 'Policy experts', 'Community leaders', 'Industry representatives']
#         }
#         # Gemini API configuration
#         self.gemini_api_key = Config.GEMINI_API_KEY  # Load from config.py
#         self.gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"


#     # def _call_gemini_api(self, prompt):
#     #     """Call the Gemini API to generate reasons for newsroom coverage."""
#     #     headers = {
#     #         "Authorization": f"Bearer {self.gemini_api_key}",
#     #         "Content-Type": "application/json"
#     #     }
#     #     payload = {
#     #         "contents": [{"parts": [{"text": prompt}]}],
#     #         "generationConfig": {
#     #             "maxOutputTokens": 200,
#     #             "temperature": 0.7
#     #         }
#     #     }

#     #     try:
#     #         response = requests.post(self.gemini_api_url, json=payload, headers=headers)
#     #         response.raise_for_status()
#     #         result = response.json()
#     #         # Parse the response based on Gemini API structure
#     #         reasons = result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "No reasons generated.")
#     #         return reasons.split("\n") if isinstance(reasons, str) else ["No reasons generated."]
#     #     except requests.exceptions.RequestException as e:
#     #         logger.error(f"Gemini API error: {e}")
#     #         return ["Unable to generate reasons due to API error."]

# def _call_gemini_api(self, prompt):
#     """Call the Gemini API to generate reasons for newsroom coverage."""
#     headers = {
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "contents": [{"parts": [{"text": prompt}]}],
#         "generationConfig": {
#             "maxOutputTokens": 200,
#             "temperature": 0.7
#         }
#     }

#     # Include the API key in the URL query string
#     url = f"{self.gemini_api_url}?key={self.gemini_api_key}"

#     try:
#         response = requests.post(url, json=payload, headers=headers)
#         response.raise_for_status()
#         result = response.json()

#         # Parse the response based on Gemini API structure
#         reasons = result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "No reasons generated.")
#         return reasons.split("\n") if isinstance(reasons, str) else ["No reasons generated."]
#     except requests.exceptions.RequestException as e:
#         logger.error(f"Gemini API error: {e}")
#         return ["Unable to generate reasons due to API error."]




    

#     def generate_story_ideas(self, trending_topics):
#         """Generate story ideas from trending topics with newsroom reasons."""
#         story_ideas = []
        
#         for topic in trending_topics[:10]:  # Top 10 topics
#             story_idea = self._create_story_from_topic(topic)
#             if story_idea:
#                 # Generate reasons for newsroom coverage using Gemini
#                 prompt = f"Provide 2-3 concise reasons why a newsroom should write a story on the following trending topic: Title: {topic['title']}, Category: {topic['category']}, Engagement Score: {topic['engagement_score']}, Subreddits: {', '.join(topic['subreddits'])}, Sentiment: {topic['sentiment']}. Focus on public interest, timeliness, and market impact."
#                 reasons = self._call_gemini_api(prompt)
#                 story_idea['reasons_for_coverage'] = [r.strip() for r in reasons if r.strip()]
#                 story_ideas.append(story_idea)
        
#         return story_ideas
    
#     def _create_story_from_topic(self, topic):
#         """Create a story idea from a trending topic"""
#         category = topic['category']
#         main_post = max(topic['posts'], key=lambda x: x['engagement_score'])
        
#         # Generate headline variations
#         headlines = self._generate_headlines(main_post, topic)
#         selected_headline = random.choice(headlines)
        
#         # Select story angle
#         angles = self.story_angles.get(category, self.story_angles['Technology'])
#         selected_angle = random.choice(angles)
        
#         # Calculate news value scores
#         news_value = self._calculate_detailed_news_value(topic, main_post)
        
#         # Determine urgency
#         urgency = self._determine_urgency(topic, news_value)
        
#         # Get suggested sources
#         sources = self.source_types.get(category, self.source_types['Technology'])
#         suggested_sources = random.sample(sources, min(4, len(sources)))
        
#         # Get target audience
#         audiences = self.target_audiences.get(category, self.target_audiences['Technology'])
        
#         # Estimate reach based on engagement
#         base_reach = sum(post['engagement_score'] for post in topic['posts']) * 100
#         estimated_reach = min(500000, max(10000, base_reach))
        
#         return {
#             'id': f"story-{topic['id']}",
#             'topic_id': topic['id'],
#             'headline': selected_headline,
#             'angle': selected_angle,
#             'news_value': news_value,
#             'suggested_sources': suggested_sources,
#             'target_audience': audiences,
#             'estimated_reach': estimated_reach,
#             'urgency': urgency,
#             'references': self._generate_references(topic),
#             'reasons_for_coverage': []  # Initialize with empty list for Gemini reasons
#         }
    
#     def _generate_headlines(self, main_post, topic):
#         """Generate multiple headline options"""
#         original_title = main_post['title']
#         category = topic['category']
        
#         headlines = [original_title]
        
#         # Question-based headlines
#         if category == 'Technology':
#             headlines.append(f"Is {original_title.split()[0]} the Future of Technology?")
#             headlines.append(f"What {original_title} Means for Your Digital Life")
#         elif category == 'Politics':
#             headlines.append(f"How {original_title} Could Change Everything")
#             headlines.append(f"The Political Implications of {original_title}")
#         elif category == 'Business':
#             headlines.append(f"Why {original_title} Matters to Your Wallet")
#             headlines.append(f"The Economic Impact of {original_title}")
        
#         # Impact-focused headlines
#         headlines.append(f"Breaking Down {original_title}: What You Need to Know")
#         headlines.append(f"The Real Story Behind {original_title}")
        
#         return headlines[:3]  # Return top 3 options
    
#     def _calculate_detailed_news_value(self, topic, main_post):
#         """Calculate detailed news value scores"""
#         # Timeliness - how recent is the story
#         hours_old = (datetime.now().timestamp() - main_post['created_utc']) / 3600
#         timeliness = max(20, 100 - (hours_old * 2))
        
#         # Impact - based on engagement and reach
#         impact = min(100, topic['engagement_score'])
        
#         # Prominence - based on subreddit and post score
#         prominence = min(100, main_post['score'] / 100)
        
#         # Proximity - assume moderate local relevance
#         proximity = random.randint(40, 80)
        
#         # Conflict - based on sentiment and comments
#         conflict_indicators = main_post['comments'] / max(1, main_post['score'])
#         conflict = min(100, conflict_indicators * 50)
        
#         # Human interest - based on story type and engagement
#         human_interest = random.randint(50, 90)
        
#         return {
#             'timeliness': int(timeliness),
#             'proximity': int(proximity),
#             'impact': int(impact),
#             'prominence': int(prominence),
#             'conflict': int(conflict),
#             'human_interest': int(human_interest)
#         }
    
#     def _determine_urgency(self, topic, news_value):
#         """Determine story urgency"""
#         avg_news_value = sum(news_value.values()) / len(news_value)
#         hours_old = (datetime.now().timestamp() - (topic['peak_time'] / 1000)) / 3600
        
#         if avg_news_value > 80 and hours_old < 6:
#             return 'breaking'
#         elif avg_news_value > 70 and hours_old < 12:
#             return 'high'
#         elif avg_news_value > 50:
#             return 'medium'
#         else:
#             return 'low'
    
#     def _generate_references(self, topic):
#         """Generate reference suggestions"""
#         references = []
        
#         # Use actual Reddit posts as references
#         for i, post in enumerate(topic['posts'][:3]):
#             ref_type = 'social_media' if post['subreddit'] in ['twitter', 'facebook'] else 'article'
            
#             reference = {
#                 'id': f"ref-{post['id']}",
#                 'title': post['title'],
#                 'url': f"https://reddit.com{post['permalink']}",
#                 'source': f"Reddit - r/{post['subreddit']}",
#                 'date': datetime.fromtimestamp(post['created_utc']).strftime('%Y-%m-%d'),
#                 'relevance_score': min(100, post['engagement_score']),
#                 'type': ref_type
#             }
#             references.append(reference)
        
#         return references










# import random
# from datetime import datetime
# from textblob import TextBlob
# import requests
# from config import Config  # Added to load Gemini API key
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class StoryGenerator:
#     def __init__(self):
#         self.story_angles = {
#             'Technology': [
#                 'How this technology could impact local businesses',
#                 'What this means for job markets in the region',
#                 'Privacy and security implications for consumers',
#                 'Economic opportunities and challenges ahead'
#             ],
#             'Politics': [
#                 'Local political implications and reactions',
#                 'How this affects upcoming elections',
#                 'Economic impact on different demographics',
#                 'Historical context and precedent analysis'
#             ],
#             'Science': [
#                 'Practical applications in everyday life',
#                 'Funding and research implications',
#                 'Ethical considerations and public debate',
#                 'Timeline for real-world implementation'
#             ],
#             'Business': [
#                 'Market disruption and competitive landscape',
#                 'Consumer behavior and spending patterns',
#                 'Regulatory challenges and opportunities',
#                 'Investment and growth potential analysis'
#             ],
#             'Health': [
#                 'Public health policy implications',
#                 'Healthcare system impact and costs',
#                 'Patient advocacy and access issues',
#                 'Prevention and treatment innovations'
#             ],
#             'Environment': [
#                 'Climate change mitigation strategies',
#                 'Economic costs of environmental action',
#                 'Community and lifestyle impacts',
#                 'Policy and regulatory responses needed'
#             ]
#         }

#         self.target_audiences = {
#             'Technology': ['Tech professionals', 'Business leaders', 'General consumers'],
#             'Politics': ['Voters', 'Policy makers', 'Political activists'],
#             'Science': ['Researchers', 'Students', 'General public'],
#             'Business': ['Investors', 'Entrepreneurs', 'Business owners'],
#             'Health': ['Patients', 'Healthcare workers', 'Policy makers'],
#             'Environment': ['Environmental advocates', 'Policy makers', 'General public']
#         }

#         self.source_types = {
#             'Technology': ['Tech industry experts', 'Academic researchers', 'Company executives', 'Consumer advocates'],
#             'Politics': ['Political analysts', 'Elected officials', 'Policy experts', 'Affected constituents'],
#             'Science': ['Research scientists', 'University professors', 'Industry experts', 'Ethics specialists'],
#             'Business': ['Industry analysts', 'Company executives', 'Economic experts', 'Market researchers'],
#             'Health': ['Medical professionals', 'Public health experts', 'Patient advocates', 'Healthcare administrators'],
#             'Environment': ['Environmental scientists', 'Policy experts', 'Community leaders', 'Industry representatives']
#         }

#         self.gemini_api_key = Config.GEMINI_API_KEY
#         self.gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

#     def _call_gemini_api(self, prompt):
#         headers = {
#             "Content-Type": "application/json"
#         }
#         payload = {
#             "contents": [{"parts": [{"text": prompt}]}],
#             "generationConfig": {
#                 "maxOutputTokens": 200,
#                 "temperature": 0.7
#             }
#         }
#         url = f"{self.gemini_api_url}?key={self.gemini_api_key}"

#         try:
#             response = requests.post(url, json=payload, headers=headers)
#             response.raise_for_status()
#             result = response.json()
#             reasons = result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "No reasons generated.")
#             return reasons.split("\n") if isinstance(reasons, str) else ["No reasons generated."]
#         except requests.exceptions.RequestException as e:
#             logger.error(f"Gemini API error: {e}")
#             return ["Unable to generate reasons due to API error."]

#     def generate_story_ideas(self, trending_topics):
#         story_ideas = []
#         for topic in trending_topics[:10]:
#             story_idea = self._create_story_from_topic(topic)
#             if story_idea:
#                 prompt = (
#                     f"Provide 2-3 concise reasons why a newsroom should write a story on the following trending topic: "
#                     f"Title: {topic['title']}, Category: {topic['category']}, Engagement Score: {topic['engagement_score']}, "
#                     f"Subreddits: {', '.join(topic.get('subreddits', []))}, Sentiment: {topic['sentiment']}. "
#                     f"Focus on public interest, timeliness, and market impact."
#                 )
#                 reasons = self._call_gemini_api(prompt)
#                 story_idea['reasons_for_coverage'] = [r.strip() for r in reasons if r.strip()]
#                 story_ideas.append(story_idea)
#         return story_ideas

#     def _create_story_from_topic(self, topic):
#         category = topic['category']
#         main_post = max(topic['posts'], key=lambda x: x['engagement_score'])

#         headlines = self._generate_headlines(main_post, topic)
#         selected_headline = random.choice(headlines)

#         angles = self.story_angles.get(category, self.story_angles['Technology'])
#         selected_angle = random.choice(angles)

#         news_value = self._calculate_detailed_news_value(topic, main_post)
#         urgency = self._determine_urgency(topic, news_value)

#         sources = self.source_types.get(category, self.source_types['Technology'])
#         suggested_sources = random.sample(sources, min(4, len(sources)))

#         audiences = self.target_audiences.get(category, self.target_audiences['Technology'])

#         base_reach = sum(post['engagement_score'] for post in topic['posts']) * 100
#         estimated_reach = min(500000, max(10000, base_reach))

#         return {
#             'id': f"story-{topic['id']}",
#             'topic_id': topic['id'],
#             'headline': selected_headline,
#             'angle': selected_angle,
#             'news_value': news_value,
#             'suggested_sources': suggested_sources,
#             'target_audience': audiences,
#             'estimated_reach': estimated_reach,
#             'urgency': urgency,
#             'references': self._generate_references(topic),
#             'reasons_for_coverage': []
#         }

#     def _generate_headlines(self, main_post, topic):
#         original_title = main_post['title']
#         category = topic['category']
#         headlines = [original_title]

#         if category == 'Technology':
#             headlines.append(f"Is {original_title.split()[0]} the Future of Technology?")
#             headlines.append(f"What {original_title} Means for Your Digital Life")
#         elif category == 'Politics':
#             headlines.append(f"How {original_title} Could Change Everything")
#             headlines.append(f"The Political Implications of {original_title}")
#         elif category == 'Business':
#             headlines.append(f"Why {original_title} Matters to Your Wallet")
#             headlines.append(f"The Economic Impact of {original_title}")

#         headlines.append(f"Breaking Down {original_title}: What You Need to Know")
#         headlines.append(f"The Real Story Behind {original_title}")

#         return headlines[:3]

#     def _calculate_detailed_news_value(self, topic, main_post):
#         hours_old = (datetime.now().timestamp() - main_post['created_utc']) / 3600
#         timeliness = max(20, 100 - (hours_old * 2))
#         impact = min(100, topic['engagement_score'])
#         prominence = min(100, main_post['score'] / 100)
#         proximity = random.randint(40, 80)
#         conflict_indicators = main_post['comments'] / max(1, main_post['score'])
#         conflict = min(100, conflict_indicators * 50)
#         human_interest = random.randint(50, 90)

#         return {
#             'timeliness': int(timeliness),
#             'proximity': int(proximity),
#             'impact': int(impact),
#             'prominence': int(prominence),
#             'conflict': int(conflict),
#             'human_interest': int(human_interest)
#         }

#     def _determine_urgency(self, topic, news_value):
#         avg_news_value = sum(news_value.values()) / len(news_value)
#         hours_old = (datetime.now().timestamp() - (topic['peak_time'] / 1000)) / 3600

#         if avg_news_value > 80 and hours_old < 6:
#             return 'breaking'
#         elif avg_news_value > 70 and hours_old < 12:
#             return 'high'
#         elif avg_news_value > 50:
#             return 'medium'
#         else:
#             return 'low'

#     def _generate_references(self, topic):
#         references = []
#         for i, post in enumerate(topic['posts'][:3]):
#             ref_type = 'social_media' if post['subreddit'] in ['twitter', 'facebook'] else 'article'
#             reference = {
#                 'id': f"ref-{post['id']}",
#                 'title': post['title'],
#                 'url': f"https://reddit.com{post['permalink']}",
#                 'source': f"Reddit - r/{post['subreddit']}",
#                 'date': datetime.fromtimestamp(post['created_utc']).strftime('%Y-%m-%d'),
#                 'relevance_score': min(100, post['engagement_score']),
#                 'type': ref_type
#             }
#             references.append(reference)
#         return references





















import random
import json
import re
from datetime import datetime
import requests
from config import Config
import logging

# ------------- logging setup ---------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StoryGenerator:
    def __init__(self):
        # ---------- fallback headline‑angle templates ----------
        self.story_angles = {
            'Technology': [
                'How this technology could impact local businesses',
                'What this means for job markets in the region',
                'Privacy and security implications for consumers',
                'Economic opportunities and challenges ahead'
            ],
            'Politics': [
                'Local political implications and reactions',
                'How this affects upcoming elections',
                'Economic impact on different demographics',
                'Historical context and precedent analysis'
            ],
            'Science': [
                'Practical applications in everyday life',
                'Funding and research implications',
                'Ethical considerations and public debate',
                'Timeline for real‑world implementation'
            ],
            'Business': [
                'Market disruption and competitive landscape',
                'Consumer behavior and spending patterns',
                'Regulatory challenges and opportunities',
                'Investment and growth potential analysis'
            ],
            'Health': [
                'Public health policy implications',
                'Healthcare system impact and costs',
                'Patient advocacy and access issues',
                'Prevention and treatment innovations'
            ],
            'Environment': [
                'Climate change mitigation strategies',
                'Economic costs of environmental action',
                'Community and lifestyle impacts',
                'Policy and regulatory responses needed'
            ]
        }

        # ---------- audiences & sources -------------
        self.target_audiences = {
            'Technology': ['Tech professionals', 'Business leaders', 'General consumers'],
            'Politics': ['Voters', 'Policy makers', 'Political activists'],
            'Science': ['Researchers', 'Students', 'General public'],
            'Business': ['Investors', 'Entrepreneurs', 'Business owners'],
            'Health': ['Patients', 'Healthcare workers', 'Policy makers'],
            'Environment': ['Environmental advocates', 'Policy makers', 'General public']
        }

        self.source_types = {
            'Technology': ['Tech industry experts', 'Academic researchers', 'Company executives', 'Consumer advocates'],
            'Politics': ['Political analysts', 'Elected officials', 'Policy experts', 'Affected constituents'],
            'Science': ['Research scientists', 'University professors', 'Industry experts', 'Ethics specialists'],
            'Business': ['Industry analysts', 'Company executives', 'Economic experts', 'Market researchers'],
            'Health': ['Medical professionals', 'Public health experts', 'Patient advocates', 'Healthcare administrators'],
            'Environment': ['Environmental scientists', 'Policy experts', 'Community leaders', 'Industry representatives']
        }

        self.gemini_api_key = Config.GEMINI_API_KEY
        self.gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    def _call_gemini_api(self, prompt, max_tokens=200, temperature=0.7):
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "maxOutputTokens": max_tokens,
                "temperature": temperature
            }
        }
        url = f"{self.gemini_api_url}?key={self.gemini_api_key}"
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=60)
            res.raise_for_status()
            txt = (
                res.json()
                .get("candidates", [{}])[0]
                .get("content", {}).get("parts", [{}])[0]
                .get("text", "")
            )
            return [l.strip() for l in txt.split("\n") if l.strip()]
        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            return []

    def _extract_json_from_text(self, text):
        try:
            match = re.search(r'\{.*?\}', text, re.DOTALL)
            if match:
                return json.loads(match.group())
        except Exception as e:
            logger.warning(f"JSON parse error: {e}")
        return None

    def _gemini_headline_angle(self, topic, main_post):
        prompt = (
            "You are an experienced newsroom editor. "
            "Return VALID JSON with keys 'headline' (<=12 words) and 'angle' (<=15 words) "
            "for the Reddit trend below. Example:\n"
            '{"headline":"...", "angle":"..."}\n\n'
            f"Trend title: {topic['title']}\n"
            f"Category: {topic['category']}\n"
            f"Engagement score: {topic['engagement_score']}\n"
            f"Top post title: {main_post['title']}\n"
            f"Sentiment: {topic['sentiment']}\n"
        )
        raw = self._call_gemini_api(prompt)
        text = "\n".join(raw)
        parsed = self._extract_json_from_text(text)

        if parsed and "headline" in parsed and "angle" in parsed:
            return parsed["headline"], parsed["angle"]
        else:
            logger.warning("Gemini headline/angle fallback used.")
            headline = random.choice(self._generate_headlines(main_post, topic))
            angle = random.choice(self.story_angles.get(topic['category'], self.story_angles['Technology']))
            return headline, angle

    def generate_story_ideas(self, trending_topics):
        ideas = []
        for topic in trending_topics[:10]:
            story = self._create_story_from_topic(topic)
            if story:
                reasons_prompt = (
                    "Give 2‑3 bullet reasons why a newsroom should cover "
                    f"this topic: {topic['title']} (category {topic['category']}, "
                    f"engagement {topic['engagement_score']}, sentiment {topic['sentiment']})."
                )
                reasons = self._call_gemini_api(reasons_prompt)
                story["reasons_for_coverage"] = reasons or ["Newsworthy development."]
                ideas.append(story)
        return ideas

    def _create_story_from_topic(self, topic):
        main_post = max(topic['posts'], key=lambda p: p['engagement_score'])
        headline, angle = self._gemini_headline_angle(topic, main_post)
        news_value = self._calculate_news_value(topic, main_post)
        urgency = self._determine_urgency(topic, news_value)

        sources = random.sample(
            self.source_types.get(topic['category'], self.source_types['Technology']), 4
        )
        audience = self.target_audiences.get(
            topic['category'], self.target_audiences['Technology']
        )

        base_reach = sum(p['engagement_score'] for p in topic['posts']) * 100
        estimated_reach = min(500_000, max(10_000, base_reach))

        return {
            "id": f"story-{topic['id']}",
            "topic_id": topic['id'],
            "headline": headline,
            "angle": angle,
            "news_value": news_value,
            "suggested_sources": sources,
            "target_audience": audience,
            "estimated_reach": estimated_reach,
            "urgency": urgency,
            "references": self._generate_references(topic),
            "reasons_for_coverage": []
        }

    def _generate_headlines(self, main_post, topic):
        title = main_post['title']
        cat = topic['category']
        lines = [title]
        if cat == 'Technology':
            lines += [f"Is {title.split()[0]} the Future of Technology?", f"What {title} Means for Your Digital Life"]
        elif cat == 'Politics':
            lines += [f"How {title} Could Change Everything", f"The Political Implications of {title}"]
        elif cat == 'Business':
            lines += [f"Why {title} Matters to Your Wallet", f"The Economic Impact of {title}"]
        lines += [f"Breaking Down {title}: What You Need to Know", f"The Real Story Behind {title}"]
        return lines[:3]

    def _calculate_news_value(self, topic, main_post):
        hours_old = (datetime.now().timestamp() - main_post['created_utc']) / 3600
        timeliness = max(20, 100 - hours_old * 2)
        impact = min(100, topic['engagement_score'])
        prominence = min(100, main_post['score'] / 100)
        proximity = random.randint(40, 80)
        conflict = min(100, (main_post['comments'] / max(1, main_post['score'])) * 50)
        human_int = random.randint(50, 90)
        return {
            "timeliness": int(timeliness),
            "proximity": int(proximity),
            "impact": int(impact),
            "prominence": int(prominence),
            "conflict": int(conflict),
            "human_interest": int(human_int)
        }

    def _determine_urgency(self, topic, nv):
        avg = sum(nv.values()) / len(nv)
        hours_old = (datetime.now().timestamp() - topic['peak_time'] / 1000) / 3600
        if avg > 80 and hours_old < 6: return "breaking"
        if avg > 70 and hours_old < 12: return "high"
        if avg > 50: return "medium"
        return "low"

    def _generate_references(self, topic):
        references = []
        for i, post in enumerate(topic['posts'][:3]):
            ref_type = 'social_media' if post['subreddit'] in ['twitter', 'facebook'] else 'article'
            reference = {
                'id': f"ref-{post['id']}",
                'title': post['title'],
                'url': f"https://reddit.com{post['permalink']}",
                'source': f"Reddit - r/{post['subreddit']}",
                'date': datetime.fromtimestamp(post['created_utc']).strftime('%Y-%m-%d'),
                'relevance_score': min(100, post['engagement_score']),
                'type': ref_type
            }
            references.append(reference)
        return references
