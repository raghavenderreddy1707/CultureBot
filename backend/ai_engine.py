import openai
import os
import json
import random
from typing import Dict, List, Any
from dotenv import load_dotenv
from .content_db import CulturalDatabase

# Load environment variables
load_dotenv()

class CultureAI:
    def __init__(self):
        # Initialize OpenAI client with the API key
        openai.api_key = os.getenv("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")  # Use the environment variable for the API key
        self.cultural_db = CulturalDatabase()
        self.system_prompt = """
        You are CultureBot, an expert AI assistant specializing in cultural knowledge from around the world. 
        You provide accurate, respectful, and insightful information about:
        - Cultural customs and traditions
        - Social etiquette and norms
        - Business practices across cultures
        - Food customs and dining etiquette
        - Religious and spiritual practices
        - Language and communication styles
        - Family structures and relationships
        - Festivals and celebrations
        
        Guidelines:
        1. Always be respectful and avoid stereotypes
        2. Acknowledge cultural diversity within countries
        3. Provide context and explain the reasoning behind customs
        4. Mention when practices may vary by region or generation
        5. Be educational and engaging
        6. If unsure, acknowledge limitations and suggest further research
        
        Keep responses informative but conversational, and always maintain cultural sensitivity.
        """
    
    async def generate_response(self, user_message: str) -> Dict[str, Any]:
        """
        Generate AI response using OpenAI with cultural context
        """
        try:
            # Get relevant cultural facts from database
            relevant_facts = self.cultural_db.search_facts(user_message)
            
            # Build context from relevant facts
            context = ""
            if relevant_facts:
                context = "\n\nRelevant cultural information:\n"
                for fact in relevant_facts[:3]:  # Limit to top 3 facts
                    context += f"- {fact['country']}: {fact['fact']} (Category: {fact['category']})\n"
            
            # Create the full prompt
            full_prompt = f"{self.system_prompt}\n\nUser  question: {user_message}{context}"
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(  # Corrected method call
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"{user_message}{context}"}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message['content']  # Corrected access to response content
            
            # Determine category and confidence
            category = self._determine_category(user_message)
            confidence = self._calculate_confidence(user_message, relevant_facts)
            sources = [fact['source'] for fact in relevant_facts if 'source' in fact]
            
            return {
                "response": ai_response,
                "confidence": confidence,
                "sources": sources,
                "category": category
            }
            
        except Exception as e:
            # Fallback to database-based response
            return self._fallback_response(user_message)
    
    def _fallback_response(self, user_message: str) -> Dict[str, Any]:
        """
        Fallback response when OpenAI is unavailable
        """
        relevant_facts = self.cultural_db.search_facts(user_message)
        
        if relevant_facts:
            fact = random.choice(relevant_facts)
            response = f"Here's an interesting cultural insight about {fact['country']}: {fact['fact']}"
        else:
            response = "I'd be happy to help you learn about different cultures! Try asking about specific countries, customs, or cultural practices."
        
        return {
            "response": response,
            "confidence": 0.7,
            "sources": ["Cultural Database"],
            "category": "general"
        }
    
    def _determine_category(self, message: str) -> str:
        """
        Determine the category of the user's question
        """
        message_lower = message.lower()
        
        categories = {
            "greeting": ["greeting", "hello", "hi", "meet", "introduction"],
            "business": ["business", "work", "office", "meeting", "professional"],
            "food": ["food", "eat", "dining", "meal", "restaurant", "cuisine"],
            "etiquette": ["etiquette", "manners", "polite", "rude", "behavior"],
            "family": ["family", "parent", "child", "marriage", "wedding"],
            "religion": ["religion", "religious", "spiritual", "worship", "prayer"],
            "language": ["language", "speak", "communication", "translate"],
            "festival": ["festival", "celebration", "holiday", "ceremony"]
        }
        
        for category, keywords in categories.items():
            if any(keyword in message_lower for keyword in keywords):
                return category
        
        return "general"
    
    def _calculate_confidence(self, message: str, relevant_facts: List[Dict]) -> float:
        """
        Calculate confidence score based on available information
        """
        base_confidence = 0.8  # Base confidence for OpenAI responses
        
        # Adjust based on relevant facts
        if relevant_facts:
            base_confidence += min(len(relevant_facts) * 0.05, 0.15)
        
        # Adjust based on message specificity
        if len(message.split()) > 5:
            base_confidence += 0.05
        
        return min(base_confidence, 0.95)  # Corrected return statement

