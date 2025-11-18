from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from agents.chat_agent import create_chat_agent
from utils.tools import chat_with_agent

app = FastAPI(title="RAG Chat API")

# Allowed origins for frontend
origins = [
    "https://petai.ama24.my",
    "https://petai-frontend.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_agent = create_chat_agent()

class ChatMessage(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    error: Optional[str] = None

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "RAG Chat API is running"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(chat_message: ChatMessage):
    try:
        response = chat_with_agent(chat_agent, chat_message.message)
        return ChatResponse(response=response)
    except Exception as e:
        return ChatResponse(response="", error=str(e))
