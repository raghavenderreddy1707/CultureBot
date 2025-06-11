"""
Cultural Data Repository for CultureBot
Contains comprehensive cultural information for countries worldwide
"""

from typing import Dict, List, Any

# Comprehensive cultural data structure
CULTURAL_DATA = {
    "Japan": {
        "basic_info": {
            "continent": "Asia",
            "capital": "Tokyo",
            "population": "125 million",
            "currency": "Japanese Yen (¥)"
        },
        "languages": {
            "official": ["Japanese"],
            "spoken": ["Japanese", "Ainu", "Ryukyuan languages"],
            "facts": [
                "Japanese has three writing systems: Hiragana, Katakana, and Kanji",
                "Honorific language (Keigo) is crucial in Japanese communication",
                "Many Japanese words have been adopted into English, like 'tsunami' and 'karaoke'"
            ]
        },
        "festivals": [
            {
                "name": "Cherry Blossom Festival (Hanami)",
                "season": "Spring (March-May)",
                "description": "Celebration of cherry blossoms with picnics under blooming trees",
                "significance": "Symbolizes the fleeting nature of life and beauty"
            },
            {
                "name": "Obon Festival",
                "season": "Summer (August)",
                "description": "Buddhist festival honoring deceased ancestors",
                "significance": "Families reunite and visit ancestral gravesites"
            },
            {
                "name": "Golden Week",
                "season": "Spring (Late April-Early May)",
                "description": "Series of national holidays creating a week-long break",
                "significance": "Major travel period for Japanese families"
            },
            {
                "name": "Tanabata (Star Festival)",
                "season": "Summer (July 7)",
                "description": "Festival celebrating the meeting of celestial lovers",
                "significance": "People write wishes on paper strips tied to bamboo"
            }
        ],
        "best_locations": [
            {
                "name": "Mount Fuji",
                "type": "Natural Wonder",
                "description": "Japan's highest mountain and spiritual symbol",
                "best_time": "Climbing season: July-September"
            },
            {
                "name": "Kyoto",
                "type": "Historical City",
                "description": "Former imperial capital with thousands of temples",
                "highlights": ["Fushimi Inari Shrine", "Bamboo Grove", "Geisha districts"]
            },
            {
                "name": "Tokyo",
                "type": "Modern City",
                "description": "Bustling capital blending tradition and modernity",
                "highlights": ["Shibuya Crossing", "Senso-ji Temple", "Tsukiji Market"]
            },
            {
                "name": "Hiroshima",
                "type": "Historical Site",
                "description": "Peace Memorial and beautiful Miyajima Island",
                "significance": "Important site for peace education and remembrance"
            }
        ],
        "cultural_facts": [
            {
                "fact": "In Japan, it's considered rude to blow your nose in public. People excuse themselves to do it privately.",
                "category": "etiquette",
                "source": "Japanese Cultural Studies"
            },
            {
                "fact": "Japanese business cards (meishi) are exchanged with both hands and should be received with respect and careful examination.",
                "category": "business",
                "source": "Japanese Business Etiquette Guide"
            },
            {
                "fact": "Bowing is an essential part of Japanese culture, with different depths for different situations.",
                "category": "greeting",
                "source": "Japanese Social Customs"
            }
        ],
        "food_culture": {
            "staples": ["Rice", "Fish", "Soy products", "Vegetables"],
            "popular_dishes": ["Sushi", "Ramen", "Tempura", "Miso soup"],
            "dining_etiquette": [
                "Say 'Itadakimasu' before eating and 'Gochisousama' after",
                "Don't stick chopsticks upright in rice",
                "Slurping noodles is acceptable and shows appreciation"
            ]
        }
    },
    
    "India": {
        "basic_info": {
            "continent": "Asia",
            "capital": "New Delhi",
            "population": "1.4 billion",
            "currency": "Indian Rupee (₹)"
        },
        "languages": {
            "official": ["Hindi", "English"],
            "spoken": ["Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Malayalam", "Kannada", "Odia", "Punjabi", "Assamese"],
            "facts": [
                "India has 22 official languages and over 1,600 spoken languages",
                "Sanskrit is one of the world's oldest languages",
                "Each state often has its own primary language"
            ]
        },
        "festivals": [
            {
                "name": "Diwali (Festival of Lights)",
                "season": "Autumn (October-November)",
                "description": "Hindu festival celebrating victory of light over darkness",
                "significance": "Homes are decorated with lamps and fireworks light the sky"
            },
            {
                "name": "Holi (Festival of Colors)",
                "season": "Spring (March)",
                "description": "Celebration of spring with colored powders and water",
                "significance": "Symbolizes love, forgiveness, and new beginnings"
            },
            {
                "name": "Durga Puja",
                "season": "Autumn (September-October)",
                "description": "Bengali festival honoring Goddess Durga",
                "significance": "Elaborate pandals and cultural performances"
            },
            {
                "name": "Eid al-Fitr",
                "season": "Variable (based on lunar calendar)",
                "description": "Islamic festival marking end of Ramadan",
                "significance": "Celebrated by India's large Muslim population"
            }
        ],
        "best_locations": [
            {
                "name": "Taj Mahal",
                "type": "UNESCO World Heritage Site",
                "description": "Ivory-white marble mausoleum in Agra",
                "best_time": "October to March"
            },
            {
                "name": "Kerala Backwaters",
                "type": "Natural Beauty",
                "description": "Network of canals, rivers, and lakes",
                "highlights": ["Houseboat cruises", "Spice plantations", "Ayurvedic treatments"]
            },
            {
                "name": "Rajasthan",
                "type": "Cultural Region",
                "description": "Land of kings with magnificent palaces and forts",
                "highlights": ["Jaipur", "Udaipur", "Jodhpur", "Jaisalmer"]
            },
            {
                "name": "Goa",
                "type": "Beach Destination",
                "description": "Former Portuguese colony known for beaches and cuisine",
                "highlights": ["Portuguese architecture", "Beach culture", "Spice markets"]
            }
        ],
        "cultural_facts": [
            {
                "fact": "India has 22 official languages and over 1,600 spoken languages, making it one of the most linguistically diverse countries.",
                "category": "language",
                "source": "Indian Linguistic Survey"
            },
            {
                "fact": "In Indian culture, touching someone's feet is a sign of respect, especially for elders and teachers.",
                "category": "greeting",
                "source": "Indian Cultural Traditions"
            },
            {
                "fact": "The concept of 'Atithi Devo Bhava' means 'Guest is God' in Indian culture.",
                "category": "hospitality",
                "source": "Indian Hospitality Traditions"
            }
        ],
        "food_culture": {
            "staples": ["Rice", "Wheat", "Lentils", "Spices"],
            "popular_dishes": ["Curry", "Biryani", "Dosa", "Chapati", "Samosa"],
            "dining_etiquette": [
                "Many Indians eat with their right hand",
                "Sharing food is common and considered bonding",
                "Vegetarianism is widely practiced"
            ]
        }
    },
    
    "Brazil": {
        "basic_info": {
            "continent": "South America",
            "capital": "Brasília",
            "population": "215 million",
            "currency": "Brazilian Real (R$)"
        },
        "languages": {
            "official": ["Portuguese"],
            "spoken": ["Portuguese", "Spanish", "German", "Italian", "Japanese", "Indigenous languages"],
            "facts": [
                "Brazil is the only Portuguese-speaking country in South America",
                "Over 180 indigenous languages are still spoken",
                "Brazilian Portuguese differs significantly from European Portuguese"
            ]
        },
        "festivals": [
            {
                "name": "Carnival",
                "season": "Summer (February-March)",
                "description": "World's largest carnival celebration with parades and street parties",
                "significance": "Showcases Brazilian culture, music, and dance"
            },
            {
                "name": "Festa Junina",
                "season": "Winter (June)",
                "description": "Traditional rural festivals celebrating harvest",
                "significance": "Features quadrilha dancing and traditional foods"
            },
            {
                "name": "New Year's Eve (Réveillon)",
                "season": "Summer (December 31)",
                "description": "Massive beach celebrations, especially in Rio",
                "significance": "Millions dress in white for good luck"
            },
            {
                "name": "Oktoberfest (Blumenau)",
                "season": "October",
                "description": "German-Brazilian cultural festival",
                "significance": "Celebrates German immigrant heritage"
            }
        ],
        "best_locations": [
            {
                "name": "Christ the Redeemer & Rio de Janeiro",
                "type": "Iconic Landmark",
                "description": "Famous statue overlooking Rio's beautiful beaches",
                "highlights": ["Copacabana Beach", "Sugarloaf Mountain", "Carnival"]
            },
            {
                "name": "Amazon Rainforest",
                "type": "Natural Wonder",
                "description": "World's largest tropical rainforest",
                "highlights": ["Wildlife tours", "River cruises", "Indigenous culture"]
            },
            {
                "name": "Iguazu Falls",
                "type": "Natural Wonder",
                "description": "Spectacular waterfall system on Brazil-Argentina border",
                "best_time": "April to June"
            },
            {
                "name": "Salvador",
                "type": "Historical City",
                "description": "First capital of Brazil with Afro-Brazilian culture",
                "highlights": ["Pelourinho", "Capoeira", "Colonial architecture"]
            }
        ],
        "cultural_facts": [
            {
                "fact": "Brazilians typically hug and kiss on the cheek when greeting, even in business settings.",
                "category": "greeting",
                "source": "Brazilian Social Customs"
            },
            {
                "fact": "In Brazil, the 'OK' hand gesture is considered offensive, similar to giving someone the middle finger.",
                "category": "etiquette",
                "source": "Brazilian Cultural Guide"
            },
            {
                "fact": "Football (soccer) is more than a sport in Brazil - it's a cultural obsession.",
                "category": "sports",
                "source": "Brazilian Sports Culture"
            }
        ],
        "food_culture": {
            "staples": ["Rice", "Beans", "Meat", "Tropical fruits"],
            "popular_dishes": ["Feijoada", "Pão de açúcar", "Açaí", "Churrasco", "Coxinha"],
            "dining_etiquette": [
                "Meals are social occasions for family bonding",
                "Fresh fruit juices are preferred over soft drinks",
                "Dinner is often served late (8-9 PM)"
            ]
        }
    },
    
    "Germany": {
        "basic_info": {
            "continent": "Europe",
            "capital": "Berlin",
            "population": "83 million",
            "currency": "Euro (€)"
        },
        "languages": {
            "official": ["German"],
            "spoken": ["German", "Turkish", "Kurdish", "Russian", "Arabic"],
            "facts": [
                "German has many dialects varying by region",
                "German is known for compound words that can be very long",
                "It's the most widely spoken native language in Europe"
            ]
        },
        "festivals": [
            {
                "name": "Oktoberfest",
                "season": "Autumn (September-October)",
                "description": "World's largest beer festival in Munich",
                "significance": "Celebrates Bavarian culture with beer, food, and music"
            },
            {
                "name": "Christmas Markets (Christkindlmärkte)",
                "season": "Winter (November-December)",
                "description": "Traditional markets selling Christmas goods and food",
                "significance": "Dating back to Middle Ages, creating magical atmosphere"
            },
            {
                "name": "Carnival (Karneval/Fasching)",
                "season": "Winter/Spring (February-March)",
                "description": "Pre-Lenten celebration with parades and costumes",
                "significance": "Especially popular in Cologne and Düsseldorf"
            },
            {
                "name": "Unity Day",
                "season": "Autumn (October 3)",
                "description": "National holiday celebrating German reunification",
                "significance": "Commemorates reunification of East and West Germany"
            }
        ],
        "best_locations": [
            {
                "name": "Neuschwanstein Castle",
                "type": "Historical Castle",
                "description": "Fairy-tale castle that inspired Disney's Sleeping Beauty castle",
                "best_time": "Spring to early autumn"
            },
            {
                "name": "Berlin",
                "type": "Capital City",
                "description": "Historic city with rich cultural and political significance",
                "highlights": ["Brandenburg Gate", "Berlin Wall", "Museum Island"]
            },
            {
                "name": "Black Forest",
                "type": "Natural Region",
                "description": "Mountainous region famous for forests and cuckoo clocks",
                "highlights": ["Hiking trails", "Thermal spas", "Traditional villages"]
            },
            {
                "name": "Rhine Valley",
                "type": "Cultural Landscape",
                "description": "UNESCO site with castles and vineyards",
                "highlights": ["River cruises", "Wine tasting", "Medieval castles"]
            }
        ],
        "cultural_facts": [
            {
                "fact": "Germans value punctuality so much that being late is considered very disrespectful, even by a few minutes.",
                "category": "business",
                "source": "German Business Culture"
            },
            {
                "fact": "In Germany, it's customary to maintain eye contact during toasts and say 'Prost' or 'Zum Wohl'.",
                "category": "food",
                "source": "German Dining Etiquette"
            },
            {
                "fact": "Germans prefer direct communication and value honesty over politeness.",
                "category": "communication",
                "source": "German Social Behavior"
            }
        ],
        "food_culture": {
            "staples": ["Bread", "Potatoes", "Meat", "Beer"],
            "popular_dishes": ["Bratwurst", "Sauerkraut", "Pretzels", "Schnitzel", "Strudel"],
            "dining_etiquette": [
                "Keep hands visible on the table while eating",
                "Wait for everyone to be served before eating",
                "Beer is considered a food staple, not just alcohol"
            ]
        }
    },
    
    "France": {
        "basic_info": {
            "continent": "Europe",
            "capital": "Paris",
            "population": "68 million",
            "currency": "Euro (€)"
        },
        "languages": {
            "official": ["French"],
            "spoken": ["French", "Arabic", "Portuguese", "Italian", "Spanish"],
            "facts": [
                "French is spoken on all continents",
                "The Académie française regulates the French language",
                "Many English words have French origins"
            ]
        },
        "festivals": [
            {
                "name": "Bastille Day",
                "season": "Summer (July 14)",
                "description": "National day celebrating French Revolution",
                "significance": "Military parade on Champs-Élysées and fireworks"
            },
            {
                "name": "Cannes Film Festival",
                "season": "Spring (May)",
                "description": "Prestigious international film festival",
                "significance": "Showcases world cinema and French cultural influence"
            },
            {
                "name": "Fête de la Musique",
                "season": "Summer (June 21)",
                "description": "Music festival celebrated across France",
                "significance": "Free concerts and street performances"
            },
            {
                "name": "Christmas Markets",
                "season": "Winter (December)",
                "description": "Traditional markets in Alsace region",
                "significance": "Blend of French and German traditions"
            }
        ],
        "best_locations": [
            {
                "name": "Eiffel Tower & Paris",
                "type": "Iconic Landmark",
                "description": "Symbol of France and city of romance",
                "highlights": ["Louvre Museum", "Notre-Dame", "Champs-Élysées"]
            },
            {
                "name": "Palace of Versailles",
                "type": "Historical Palace",
                "description": "Opulent palace of French royalty",
                "significance": "Symbol of absolute monarchy and French grandeur"
            },
            {
                "name": "French Riviera (Côte d'Azur)",
                "type": "Coastal Region",
                "description": "Glamorous Mediterranean coastline",
                "highlights": ["Nice", "Cannes", "Monaco", "Saint-Tropez"]
            },
            {
                "name": "Loire Valley",
                "type": "Cultural Landscape",
                "description": "Region of Renaissance castles and vineyards",
                "highlights": ["Château de Chambord", "Wine tours", "Gardens"]
            }
        ],
        "cultural_facts": [
            {
                "fact": "French people typically don't eat meals while walking or standing - dining is seen as a social ritual to be savored.",
                "category": "food",
                "source": "French Culinary Culture"
            },
            {
                "fact": "In France, it's polite to greet shopkeepers with 'Bonjour' when entering and 'Au revoir' when leaving.",
                "category": "etiquette",
                "source": "French Social Customs"
            },
            {
                "fact": "The French take fashion seriously and tend to dress more formally than many other cultures.",
                "category": "fashion",
                "source": "French Style Culture"
            }
        ],
        "food_culture": {
            "staples": ["Bread", "Cheese", "Wine", "Butter"],
            "popular_dishes": ["Croissant", "Coq au vin", "Ratatouille", "Crème brûlée", "Bouillabaisse"],
            "dining_etiquette": [
                "Keep hands on the table, not in your lap",
                "Bread is placed directly on the table, not on the plate",
                "Wine is an important part of meals"
            ]
        }
    },
    
    "China": {
        "basic_info": {
            "continent": "Asia",
            "capital": "Beijing",
            "population": "1.4 billion",
            "currency": "Chinese Yuan (¥)"
        },
        "languages": {
            "official": ["Standard Chinese (Mandarin)"],
            "spoken": ["Mandarin", "Cantonese", "Wu", "Min", "Hakka", "Tibetan", "Uyghur"],
            "facts": [
                "Chinese characters are used in writing, not an alphabet",
                "Mandarin is the most spoken language in the world",
                "There are hundreds of Chinese dialects"
            ]
        },
        "festivals": [
            {
                "name": "Chinese New Year (Spring Festival)",
                "season": "Winter/Spring (January-February)",
                "description": "Most important Chinese festival marking lunar new year",
                "significance": "Family reunions, red decorations, and fireworks"
            },
            {
                "name": "Mid-Autumn Festival",
                "season": "Autumn (September-October)",
                "description": "Festival celebrating harvest and family unity",
                "significance": "Mooncakes and moon gazing traditions"
            },
            {
                "name": "Dragon Boat Festival",
                "season": "Summer (June)",
                "description": "Traditional festival with dragon boat races",
                "significance": "Commemorates ancient poet Qu Yuan"
            },
            {
                "name": "National Day Golden Week",
                "season": "Autumn (October 1-7)",
                "description": "Week-long national holiday",
                "significance": "Celebrates founding of People's Republic of China"
            }
        ],
        "best_locations": [
            {
                "name": "Great Wall of China",
                "type": "UNESCO World Heritage Site",
                "description": "Ancient fortification stretching thousands of miles",
                "best_time": "Spring and autumn"
            },
            {
                "name": "Forbidden City",
                "type": "Imperial Palace",
                "description": "Former Chinese imperial palace in Beijing",
                "significance": "Symbol of Chinese imperial power and architecture"
            },
            {
                "name": "Terracotta Army",
                "type": "Archaeological Site",
                "description": "Collection of terracotta sculptures in Xi'an",
                "significance": "Depicts armies of first Emperor of China"
            },
            {
                "name": "Guilin",
                "type": "Natural Beauty",
                "description": "Famous for dramatic karst landscape",
                "highlights": ["Li River cruise", "Reed flute cave", "Yangshuo"]
            }
        ],
        "cultural_facts": [
            {
                "fact": "In Chinese culture, the number 8 is considered extremely lucky because it sounds like the word for 'prosperity'.",
                "category": "beliefs",
                "source": "Chinese Numerology Studies"
            },
            {
                "fact": "When receiving a business card in China, accept it with both hands and take a moment to read it carefully.",
                "category": "business",
                "source": "Chinese Business Etiquette"
            },
            {
                "fact": "Red is considered the luckiest color in Chinese culture, symbolizing prosperity and joy.",
                "category": "symbolism",
                "source": "Chinese Color Symbolism"
            }
        ],
        "food_culture": {
            "staples": ["Rice", "Noodles", "Tea", "Soy sauce"],
            "popular_dishes": ["Peking duck", "Dim sum", "Hot pot", "Kung pao chicken", "Mapo tofu"],
            "dining_etiquette": [
                "Meals are shared family-style",
                "Chopsticks should not be stuck upright in rice",
                "Tea is continuously refilled for guests"
            ]
        }
    }
}

def get_all_countries() -> List[str]:
    """Get list of all countries in the database"""
    return list(CULTURAL_DATA.keys())

def get_country_data(country: str) -> Dict[str, Any]:
    """Get all data for a specific country"""
    return CULTURAL_DATA.get(country, {})

def search_by_category(category: str) -> List[Dict[str, Any]]:
    """Search cultural facts by category across all countries"""
    results = []
    for country, data in CULTURAL_DATA.items():
        if 'cultural_facts' in data:
            for fact in data['cultural_facts']:
                if fact['category'].lower() == category.lower():
                    fact_with_country = fact.copy()
                    fact_with_country['country'] = country
                    results.append(fact_with_country)
    return results

def get_all_cultural_facts() -> List[Dict[str, Any]]:
    """Get all cultural facts from all countries"""
    all_facts = []
    for country, data in CULTURAL_DATA.items():
        if 'cultural_facts' in data:
            for fact in data['cultural_facts']:
                fact_with_country = fact.copy()
                fact_with_country['country'] = country
                all_facts.append(fact_with_country)
    return all_facts

def get_festivals_by_season(season: str) -> List[Dict[str, Any]]:
    """Get festivals by season across all countries"""
    results = []
    for country, data in CULTURAL_DATA.items():
        if 'festivals' in data:
            for festival in data['festivals']:
                if season.lower() in festival['season'].lower():
                    festival_with_country = festival.copy()
                    festival_with_country['country'] = country
                    results.append(festival_with_country)
    return results

def search_locations_by_type(location_type: str) -> List[Dict[str, Any]]:
    """Search best locations by type across all countries"""
    results = []
    for country, data in CULTURAL_DATA.items():
        if 'best_locations' in data:
            for location in data['best_locations']:
                if location_type.lower() in location['type'].lower():
                    location_with_country = location.copy()
                    location_with_country['country'] = country
                    results.append(location_with_country)
    return results
