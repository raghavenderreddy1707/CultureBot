import streamlit as st
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8502")

# Page configuration
st.set_page_config(
    page_title="CultureBot - Your AI Cultural Guide",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
        color:#333;
        border-left: 4px solid #667eea;
        margin-right: 2rem;
    }
    
    .fact-card {
        background: linear-gradient(135deg, #ffd3a5 0%, #fd6585 100%);
        color:#212121;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .metric-card {
        background: white;
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
            <p><strong>Team:</strong> Cultural AI Labs</p>
            <p><strong>Version:</strong> 2.1.0</p>
            <p><strong>Created:</strong> January 15, 2024</p>
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
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            st.success("🟢 Backend Online")
        else:
            st.error("🔴 Backend Offline")
    except:
        st.error("🔴 Backend Offline")
    
    # Random fact
    st.markdown("### 🎲 Random Fact")
    if st.button("Get Random Fact"):
        try:
            response = requests.get(f"{BACKEND_URL}/facts/random", timeout=10)
            if response.status_code == 200:
                fact = response.json()
                st.markdown(f"""
                <div class="fact-card">
                    <h4>{fact['country']}</h4>
                    <p>{fact['fact']}</p>
                    <small>Category: {fact['category']}</small>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error("Unable to fetch random fact")

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
    
    if st.button("Start Chatting Now", type="primary"):
        st.session_state.navigation = "💬 Chat with CultureBot"
        st.rerun()

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
            try:
                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={"message": user_input},
                    timeout=30
                )
                
                if response.status_code == 200:
                    bot_response = response.json()
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": bot_response["response"]
                    })
                else:
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "I'm sorry, I'm having trouble connecting to my knowledge base right now. Please try again later."
                    })
            except Exception as e:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "I'm experiencing some technical difficulties. Please make sure the backend server is running and try again."
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
            if st.button(suggestion, key=f"suggestion_{i}"):
                st.session_state.messages.append({"role": "user", "content": suggestion})
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
        country_filter = st.selectbox(
            "Filter by Country:",
            ["All Countries", "Japan", "India", "Brazil", "Germany", "China", "France", "South Korea", "Mexico", "Egypt", "Russia", "Thailand", "Italy"]
        )
    
    with col2:
        category_filter = st.selectbox(
            "Filter by Category:",
            ["All Categories", "etiquette", "business", "greeting", "food", "language", "family", "beliefs", "general"]
        )
    
    # Fetch and display facts
    try:
        if country_filter != "All Countries":
            response = requests.get(f"{BACKEND_URL}/facts/country/{country_filter}", timeout=10)
        elif category_filter != "All Categories":
            response = requests.get(f"{BACKEND_URL}/facts/category/{category_filter}", timeout=10)
        else:
            # Get random facts for display
            facts = []
            for _ in range(10):
                fact_response = requests.get(f"{BACKEND_URL}/facts/random", timeout=5)
                if fact_response.status_code == 200:
                    facts.append(fact_response.json())
            
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
        
        if country_filter != "All Countries" or category_filter != "All Categories":
            if response.status_code == 200:
                facts = response.json()
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
            else:
                st.error("Unable to fetch facts from the server.")
    
    except Exception as e:
        st.error("Unable to connect to the backend server. Please make sure it's running.")

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
        - **Backend**: FastAPI (Python)
        - **AI Engine**: OpenAI GPT-3.5-turbo
        - **Database**: In-memory cultural facts database
        """)
    
    with col2:
        st.markdown("""
        ### ✨ Features
        - **Global Coverage**: Cultural insights from countries across all continents
        - **AI-Powered Chat**: Natural conversation interface powered by OpenAI
        - **Curated Content**: Carefully researched and verified cultural facts
        - **Smart Responses**: Context-aware answers tailored to your questions
        - **Real-time Interaction**: Fast and responsive chat experience
        """)
    
    st.markdown("---")
    
    # Technical details
    st.markdown("### 🏗️ Architecture")
    st.markdown("""
    CultureBot follows a modern microservices architecture:
    
    1. **Streamlit Frontend**: Beautiful, interactive user interface
    2. **FastAPI Backend**: High-performance API server
    3. **OpenAI Integration**: Advanced natural language processing
    4. **Cultural Database**: Curated collection of cultural facts and insights
    """)
    
    # Contact and support
    st.markdown("### 📞 Support")
    st.markdown("""
    For technical support or cultural content suggestions, please contact:
    - **Team**: Cultural AI Labs
    - **Version**: 2.1.0
    - **Last Updated**: January 15, 2024
    """)
