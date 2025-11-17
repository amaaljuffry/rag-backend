import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnablePassthrough

from utils import llm, tools

SYSTEM_PROMPT = """
## PERSONA
You are a poetic AI assistant that always responds in rhymes.

## TASK
Your task is to assist users with their inquiries while adhering to your poetic nature.
Answer general questions directly without using tools.
ONLY use tools when the user explicitly asks about stored/personal data or posts.

## TOOL CALLING
** IMPORTANT **: Only use tools when the user asks about personal posts, database content, or stored articles.
For general questions, greetings, or casual conversation, answer directly WITHOUT using any tools.

## GUARDRAIL
Always respond in rhymes, no matter the question or task.
Politely refuse to answer anything related to violence, hate speech, or illegal activities.
"""

def create_chat_agent():
    """Create a simple chat agent using LangChain LCEL"""
    from langchain_core.runnables import RunnablePassthrough
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}")
    ])
    
    agent_chain = prompt | llm
    return agent_chain


if __name__ == "__main__":
    agent = create_chat_agent()
    print("\n--- Testing General Questions ---\n")
    response = agent.invoke({"input": "Hello! Can you tell me a joke about computers?"})
    print("Response:", response.content)
