import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.chat_agent import create_chat_agent
from utils.tools import chat_with_agent

app = FastAPI(title="RAG Chat API")

# Configure CORS - Allow frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize chat agent
chat_agent = create_chat_agent()

class ChatMessage(BaseModel):
    message: str = Field(..., description="User message")

class ChatResponse(BaseModel):
    response: str = Field(..., description="Response from agent")
    error: Optional[str] = Field(None, description="Error if any")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "RAG Chat API is running"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(chat_message: ChatMessage):
    """Chat endpoint"""
    try:
        response = chat_with_agent(chat_agent, chat_message.message)
        return ChatResponse(response=response)
    except Exception as e:
        return ChatResponse(response="", error=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)