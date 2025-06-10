import streamlit as st
import os
import json
import random
from typing import Dict, List, Any
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="CultureBot - Your AI Cultural Guide",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cultural Database Class
class CulturalDatabase:
    def __init__(self):
        self.cultural_facts = [
            {
                "country": "Japan",
                "fact": "In Japan, it's considered rude to blow your nose in public. People excuse themselves to do it privately.",
                "category": "etiquette",
                "source": "Japanese Cultural Studies"
            },
            {
                "country": "Japan",
                "fact": "Japanese business cards (meishi) are exchanged with both hands and should be received with respect and careful examination.",
                "category": "business",
                "source": "Japanese Business Etiquette Guide"
            },
            {
                "country": "India",
                "fact": "India has 22 official languages and over 1,600 spoken languages, making it one of the most linguistically diverse countries.",
                "category": "language",
                "source": "Indian Linguistic Survey"
            },
            {
                "country": "India",
                "fact": "In Indian culture, touching someone's feet is a sign of respect, especially for elders and teachers.",
                "category": "greeting",
                "source": "Indian Cultural Traditions"
            },
            {
                "country": "Brazil",
                "fact": "Brazilians typically hug and kiss on the cheek when greeting, even in business settings.",
                "category": "greeting",
                "source": "Brazilian Social Customs"
            },
            {
                "country": "Brazil",
                "fact": "In Brazil, the 'OK' hand gesture is considered offensive, similar to giving someone the middle finger.",
                "category": "etiquette",
                "source": "Brazilian Cultural Guide"
            },
            {
                "country": "Germany",
                "fact": "Germans value punctuality so much that being late is considered very disrespectful, even by a few minutes.",
                "category": "business",
                "source": "German Business Culture"
            },
            {
                "country": "Germany",
                "fact": "In Germany, it's customary to maintain eye contact during toasts and say 'Prost' or 'Zum Wohl'.",
                "category": "food",
                "source": "German Dining Etiquette"
            },
            {
                "country": "China",
                "fact": "In Chinese culture, the number 8 is considered extremely lucky because it sounds like the word for 'prosperity'.",
                "category": "beliefs",
                "source": "Chinese Numerology Studies"
            },
            {
                "country": "China",
                "fact": "When receiving a business card in China, accept it with both hands and take a moment to read it carefully.",
                "category": "business",
                "source": "Chinese Business Etiquette"
            },
            {
                "country": "France",
                "fact": "French people typically don't eat meals while walking or standing - dining is seen as a social ritual to be savored.",
                "category": "food",
                "source": "French Culinary Culture"
            },
            {
                "country": "France",
                "fact": "In France, it's polite to greet shopkeepers with 'Bonjour' when entering and 'Au revoir' when leaving.",
                "category": "etiquette",
                "source": "French Social Customs"
            },
            {
                "country": "South Korea",
                "fact": "In Korea, you should use both hands when giving or receiving business cards as a sign of respect.",
                "category": "business",
                "source": "Korean Business Protocol"
            },
            {
                "country": "South Korea",
                "fact": "Korean age calculation includes the time spent in the womb, so Koreans are typically 1-2 years older in 'Korean age'.",
                "category": "general",
                "source": "Korean Cultural Practices"
            },
            {
                "country": "Mexico",
                "fact": "Mexican families often have multiple generations living together, and family loyalty is highly valued.",
                "category": "family",
                "source": "Mexican Family Structures"
            },
            {
                "country": "Mexico",
                "fact": "In Mexico, personal space is smaller than in many Western cultures, and people stand closer during conversations.",
                "category": "etiquette",
                "source": "Mexican Social Norms"
            },
            {
                "country": "Egypt",
                "fact": "In Egypt, showing the sole of your foot to someone is considered offensive, so keep feet flat on the ground when sitting.",
                "category": "etiquette",
                "source": "Egyptian Cultural Guidelines"
            },
            {
                "country": "Egypt",
                "fact": "Egyptian hospitality is legendary - guests are often offered tea or coffee multiple times as a sign of welcome.",
                "category": "food",
                "source": "Egyptian Hospitality Traditions"
            },
            {
                "country": "Russia",
                "fact": "Russians believe that smiling without reason is insincere, so don't be surprised by serious expressions in public.",
                "category": "expression",
                "source": "Russian Social Behavior"
            },
            {
                "country": "Russia",
                "fact": "In Russia, it's traditional to remove shoes when entering someone's home, and slippers are often provided for guests.",
                "category": "etiquette",
                "source": "Russian Home Customs"
            },
            {
                "country": "Thailand",
                "fact": "In Thailand, the head is considered sacred, so never touch someone's head, even children.",
                "category": "etiquette",
                "source": "Thai Cultural Sensitivities"
            },
            {
                "country": "Thailand",
                "fact": "Thai people use the 'wai' greeting - pressing palms together and bowing slightly - as a sign of respect.",
                "category": "greeting",
                "source": "Thai Greeting Customs"
            },
            {
                "country": "Italy",
                "fact": "In Italy, cappuccino is traditionally only drunk in the morning, never after meals.",
                "category": "food",
                "source": "Italian Coffee Culture"
            },
            {
                "country": "Italy",
                "fact": "Italians often speak with their hands, and gestures are an integral part of communication.",
                "category": "language",
                "source": "Italian Communication Styles"
            }
        ]
    
    def search_facts(self, query: str) -> List[Dict[str, Any]]:
        """Search for relevant cultural facts based on query"""
        query_lower = query.lower()
        relevant_facts = []
        
        # Search by country
        for fact in self.cultural_facts:
            if fact['country'].lower() in query_lower:
                relevant_facts.append(fact)
        
        # Search by category
        if not relevant_facts:
            for fact in self.cultural_facts:
                if fact['category'].lower() in query_lower:
                    relevant_facts.append(fact)
        
        # Search by keywords in fact content
        if not relevant_facts:
            keywords = query_lower.split()
            for fact in self.cultural_facts:
                fact_text = fact['fact'].lower()
                if any(keyword in fact_text for keyword in keywords):
                    relevant_facts.append(fact)
        
        return relevant_facts[:5]
    
    def get_random_fact(self) -> Dict[str, Any]:
        """Get a random cultural fact"""
        return random.choice(self.cultural_facts)
    
    def get_facts_by_country(self, country: str) -> List[Dict[str, Any]]:
        """Get all facts for a specific country"""
        return [fact for fact in self.cultural_facts if fact['country'].lower() == country.lower()]
    
    def get_facts_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get all facts for a specific category"""
        return [fact for fact in self.cultural_facts if fact['category'].lower() == category.lower()]
    
    def get_all_countries(self) -> List[str]:
        """Get list of all countries in the database"""
        return list(set(fact['country'] for fact in self.cultural_facts))
    
    def get_all_categories(self) -> List[str]:
        """Get list of all categories in the database"""
        return list(set(fact['category'] for fact in self.cultural_facts))

# Simple AI Response Generator (without OpenAI dependency)
class CultureAI:
    def __init__(self):
        self.cultural_db = CulturalDatabase()
        
    def generate_response(self, user_message: str) -> Dict[str, Any]:
        """Generate response based on cultural database"""
        # Get relevant cultural facts from database
        relevant_facts = self.cultural_db.search_facts(user_message)
        
        if relevant_facts:
            # Use the most relevant fact
            fact = relevant_facts[0]
            
            # Generate contextual response
            if "greeting" in user_message.lower():
                response = f"Regarding greetings in {fact['country']}: {fact['fact']} This reflects the cultural values of respect and social harmony that are important in {fact['country']}."
            elif "business" in user_message.lower():
                response = f"For business practices in {fact['country']}: {fact['fact']} Understanding these customs is crucial for successful professional relationships."
            elif "food" in user_message.lower() or "dining" in user_message.lower():
                response = f"About dining culture in {fact['country']}: {fact['fact']} Food customs often reflect deeper cultural values and social structures."
            else:
                response = f"Here's an important cultural insight about {fact['country']}: {fact['fact']} This practice is rooted in the cultural values and traditions of the region."
            
            # Add additional context if multiple facts are available
            if len(relevant_facts) > 1:
                response += f"\n\nAdditionally, it's worth noting that cultural practices can vary within {fact['country']}, and these customs may differ between regions or generations."
        else:
            # Fallback response
            random_fact = self.cultural_db.get_random_fact()
            response = f"While I don't have specific information about that topic, here's an interesting cultural fact about {random_fact['country']}: {random_fact['fact']} Feel free to ask about specific countries or cultural practices!"
        
        return {
            "response": response,
            "confidence": 0.8 if relevant_facts else 0.6,
            "sources": [fact['source'] for fact in relevant_facts[:3]] if relevant_facts else ["Cultural Database"],
            "category": relevant_facts[0]['category'] if relevant_facts else "general"
        }

# Initialize components
@st.cache_resource
def initialize_components():
    return CultureAI(), CulturalDatabase()

culture_ai, cultural_db = initialize_components()

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .sidebar-info {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: 2rem;
    }
    
    .bot-message {
        background: #f8f9fa;
        color: #333;
        border-left: 4px solid #667eea;
        margin-right: 2rem;
    }
    
    .fact-card {
        background: linear-gradient(135deg, #ffd3a5 0%, #fd6585 100%);
        color: black;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .metric-card {
        background: white;
        color: black;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with app information
with st.sidebar:
    st.markdown("""
    <div class="sidebar-info">
        <h1 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem;">CultureBot</h1>
        <div style="font-size: 0.9rem; opacity: 0.9;">
            <p><strong>Team:</strong> CultureCoders</p>
            <p><strong>Version:</strong> 2.1.0</p>
            <p><strong>Created:</strong> January 2025</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    st.markdown("### 🧭 Navigation")
    page = st.selectbox(
        "Choose a page:",
        ["🏠 Home", "💬 Chat with CultureBot", "📚 Cultural Facts", "ℹ️ About"],
        key="navigation"
    )
    
    st.markdown("---")
    
    # Quick stats
    st.markdown("### 📊 Quick Stats")
    st.success("🟢 System Online")
    st.info(f"📈 {len(cultural_db.cultural_facts)} Cultural Facts")
    st.info(f"🌍 {len(cultural_db.get_all_countries())} Countries")
    
    # Random fact
    st.markdown("### 🎲 Random Fact")
    if st.button("Get Random Fact"):
        fact = cultural_db.get_random_fact()
        st.markdown(f"""
        <div class="fact-card">
            <h4>{fact['country']}</h4>
            <p>{fact['fact']}</p>
            <small>Category: {fact['category']}</small>
        </div>
        """, unsafe_allow_html=True)

# Main content area
if page == "🏠 Home":
    # Home page
    st.markdown("""
    <div class="main-header">
        <h1 style="font-size: 3rem; margin-bottom: 1rem;">Welcome to CultureBot</h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">Your AI-powered guide to understanding cultures, traditions, and social customs from around the world</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🌍 Global Insights</h3>
            <p>Discover fascinating cultural facts and customs from countries across all continents.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🤖 AI-Powered Chat</h3>
            <p>Ask questions and get personalized responses about specific countries and cultural practices.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📚 Learn & Explore</h3>
            <p>Expand your cultural awareness and become a more informed global citizen.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Getting started
    st.markdown("## 🚀 Getting Started")
    st.markdown("""
    1. **Chat with CultureBot**: Ask questions about any culture or country
    2. **Explore Facts**: Browse our curated collection of cultural insights
    3. **Learn Continuously**: Discover new perspectives and traditions
    """)

elif page == "💬 Chat with CultureBot":
    # Chat page
    st.markdown("""
    <div class="main-header">
        <h1>Chat with CultureBot</h1>
        <p>Ask me about any culture, country, or tradition!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>CultureBot:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
    
    # Chat input
    user_input = st.chat_input("Ask about any culture or country...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get bot response
        with st.spinner("CultureBot is thinking..."):
            bot_response = culture_ai.generate_response(user_input)
            st.session_state.messages.append({
                "role": "assistant", 
                "content": bot_response["response"]
            })
        
        st.rerun()
    
    # Suggested questions
    st.markdown("### 💡 Try asking about:")
    suggestions = [
        "Tell me about Japanese business etiquette",
        "What are some Indian greeting customs?",
        "How do Germans view punctuality?",
        "What should I know about dining in France?",
        "Explain Chinese lucky numbers"
    ]
    
    cols = st.columns(len(suggestions))
    for i, suggestion in enumerate(suggestions):
        with cols[i]:
            if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": suggestion})
                with st.spinner("CultureBot is thinking..."):
                    bot_response = culture_ai.generate_response(suggestion)
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": bot_response["response"]
                    })
                st.rerun()

elif page == "📚 Cultural Facts":
    # Cultural facts page
    st.markdown("""
    <div class="main-header">
        <h1>Cultural Facts Explorer</h1>
        <p>Browse our curated collection of cultural insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filters
    col1, col2 = st.columns(2)
    
    with col1:
        countries = ["All Countries"] + sorted(cultural_db.get_all_countries())
        country_filter = st.selectbox("Filter by Country:", countries)
    
    with col2:
        categories = ["All Categories"] + sorted(cultural_db.get_all_categories())
        category_filter = st.selectbox("Filter by Category:", categories)
    
    # Display facts
    if country_filter != "All Countries":
        facts = cultural_db.get_facts_by_country(country_filter)
    elif category_filter != "All Categories":
        facts = cultural_db.get_facts_by_category(category_filter)
    else:
        facts = cultural_db.cultural_facts
    
    if facts:
        for fact in facts:
            st.markdown(f"""
            <div class="fact-card">
                <h3>{fact['country']}</h3>
                <p>{fact['fact']}</p>
                <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                    <small><strong>Category:</strong> {fact['category']}</small>
                    <small><strong>Source:</strong> {fact['source']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No facts found for the selected filters.")

else:  # About page
    st.markdown("""
    <div class="main-header">
        <h1>About CultureBot</h1>
        <p>Bridging cultures through AI-powered conversations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mission and features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Our Mission
        CultureBot was created to help people understand and appreciate the rich diversity of cultures around the world. 
        In our increasingly connected world, cultural awareness is more important than ever.
        
        ### 🔧 Technology Stack
        - **Frontend**: Streamlit (Python)
        - **AI Engine**: Rule-based cultural knowledge system
        - **Database**: In-memory cultural facts database
        - **Deployment**: Hugging Face Spaces
        """)
    
    with col2:
        st.markdown("""
        ### ✨ Features
        - **Global Coverage**: Cultural insights from countries across all continents
        - **Smart Chat**: Context-aware responses about cultural practices
        - **Curated Content**: Carefully researched and verified cultural facts
        - **Interactive Interface**: Beautiful, responsive design
        - **Real-time Interaction**: Fast and responsive chat experience
        """)
    
    st.markdown("---")
    
    # Technical details
    st.markdown("### 🏗️ Architecture")
    st.markdown("""
    CultureBot is built as a single Streamlit application optimized for Hugging Face Spaces:
    
    1. **Streamlit Frontend**: Beautiful, interactive user interface
    2. **Cultural Knowledge Engine**: Smart response generation based on cultural database
    3. **Cultural Database**: Curated collection of cultural facts and insights
    4. **Responsive Design**: Works seamlessly across different devices
    """)
    
    # Contact and support
    st.markdown("### 📞 Support")
    st.markdown("""
    For technical support or cultural content suggestions:
    - **Team**: CultureCoders
    - **Version**: 2.1.0
    - **Platform**: Hugging Face Spaces
    - **Last Updated**: January 2025
    """)