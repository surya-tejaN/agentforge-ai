"""
Backboard API Client - Python bridge for JAC
Handles real LLM calls using Backboard SDK
"""
import asyncio
import os
import sys

try:
    from backboard import BackboardClient
except ImportError:
    print("ERROR: backboard-sdk not installed")
    print("Run: pip install backboard-sdk")
    sys.exit(1)

# Use environment variable for API key
BACKBOARD_KEY = os.getenv("BACKBOARD_API_KEY", "espr_b-rlAldmlPbHyYwphY6eRKc9jgEUqKGS13iGm2ONkFg")

async def call_architect(requirement):
    """Call Backboard API for architecture design"""
    client = BackboardClient(api_key=BACKBOARD_KEY)
    
    # Create assistant
    assistant = await client.create_assistant(
        name="System Architect",
        system_prompt="You are a senior software architect. Design system architectures concisely in 50 words or less."
    )
    
    # Create thread
    thread = await client.create_thread(assistant.assistant_id)
    
    # Send message
    response = await client.add_message(
        thread_id=thread.thread_id,
        content=f"Design architecture for: {requirement}",
        stream=False
    )
    
    return response.content

async def call_reviewer(code_summary):
    """Call Backboard API for code review"""
    client = BackboardClient(api_key=BACKBOARD_KEY)
    
    # Create assistant
    assistant = await client.create_assistant(
        name="Code Reviewer",
        system_prompt="You are a code reviewer. Find bugs and security issues concisely in 50 words or less."
    )
    
    # Create thread
    thread = await client.create_thread(assistant.assistant_id)
    
    # Send message
    response = await client.add_message(
        thread_id=thread.thread_id,
        content=f"Review this system: {code_summary}",
        stream=False
    )
    
    return response.content

# Synchronous wrappers for JAC
def design_architecture(requirement):
    """Synchronous wrapper for JAC"""
    return asyncio.run(call_architect(requirement))

def review_code(code_summary):
    """Synchronous wrapper for JAC"""
    return asyncio.run(call_reviewer(code_summary))

if __name__ == "__main__":
    # Test the client
    print("🔍 Testing Backboard API...\n")
    result = design_architecture("Build a blog API with JWT auth")
    print(f"✅ Result: {result}\n")
