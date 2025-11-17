from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize MongoDB connection (if needed)
mongo_uri = os.getenv("MONGO_ATLAS_CLUSTER_URI", "mongodb://localhost:27017")

# Initialize tools list
tools = []

def chat_with_agent(agent, user_message: str):
    """Helper function to chat with the agent"""
    try:
        response = agent.invoke({"input": user_message})
        
        # Handle different response types
        if hasattr(response, 'content'):
            # If it's an AIMessage object with .content attribute
            return response.content
        elif isinstance(response, str):
            # If it's already a string, return as-is
            return response
        else:
            # Fallback: convert to string
            return str(response)
    except Exception as e:
        import traceback
        print(f"Error in chat_with_agent: {str(e)}")
        print(traceback.format_exc())
        raise Exception(f"Error in chat: {str(e)}")

# Initialize tools list
tools = []