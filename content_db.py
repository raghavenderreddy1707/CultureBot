import json
import random
from typing import List, Dict, Any

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
        """
        Search for relevant cultural facts based on query
        """
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
        
        return relevant_facts[:5]  # Return top 5 matches
    
    def get_random_fact(self) -> Dict[str, Any]:
        """
        Get a random cultural fact
        """
        return random.choice(self.cultural_facts)
    
    def get_facts_by_country(self, country: str) -> List[Dict[str, Any]]:
        """
        Get all facts for a specific country
        """
        return [fact for fact in self.cultural_facts if fact['country'].lower() == country.lower()]
    
    def get_facts_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Get all facts for a specific category
        """
        return [fact for fact in self.cultural_facts if fact['category'].lower() == category.lower()]
    
    def get_all_countries(self) -> List[str]:
        """
        Get list of all countries in the database
        """
        return list(set(fact['country'] for fact in self.cultural_facts))
    
    def get_all_categories(self) -> List[str]:
        """
        Get list of all categories in the database
        """
        return list(set(fact['category'] for fact in self.cultural_facts))