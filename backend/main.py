from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from ai_engine import CultureAI
from content_db import CulturalDatabase

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="CultureBot API",
    description="AI-powered cultural insights and information",
    version="2.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI engine and database
culture_ai = CultureAI()
cultural_db = CulturalDatabase()

# Define Pydantic models
class ChatMessage(BaseModel):
    message: str
    user_id: Optional[str] = "anonymous"

class ChatResponse(BaseModel):
    response: str
    confidence: float
    sources: List[str]
    category: Optional[str] = None

class CulturalFact(BaseModel):
    country: str
    fact: str
    category: str
    source: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to CultureBot API",
        "version": "2.1.0",
        "status": "active"
    }

@app.post("/chat", response_model=ChatResponse)
async def chat_with_bot(message: ChatMessage):
    """
    Main chat endpoint for interacting with CultureBot
    """
    try:
        # Get AI response
        ai_response = await culture_ai.generate_response(message.message)
        
        # Get relevant cultural facts from database
        relevant_facts = cultural_db.search_facts(message.message)
        
        return ChatResponse(
            response=ai_response["response"],
            confidence=ai_response["confidence"],
            sources=ai_response["sources"],
            category=ai_response.get("category")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/facts/random", response_model=CulturalFact)
async def get_random_fact():
    """
    Get a random cultural fact
    """
    try:
        fact = cultural_db.get_random_fact()
        return CulturalFact(**fact)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching fact: {str(e)}")

@app.get("/facts/country/{country}", response_model=List[CulturalFact])
async def get_country_facts(country: str):
    """
    Get cultural facts for a specific country
    """
    try:
        facts = cultural_db.get_facts_by_country(country)
        return [CulturalFact(**fact) for fact in facts]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching country facts: {str(e)}")

@app.get("/facts/category/{category}", response_model=List[CulturalFact])
async def get_category_facts(category: str):
    """
    Get cultural facts for a specific category
    """
    try:
        facts = cultural_db.get_facts_by_category(category)
        return [CulturalFact(**fact) for fact in facts]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching category facts: {str(e)}")

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "ai_engine": "operational",
        "database": "connected"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
