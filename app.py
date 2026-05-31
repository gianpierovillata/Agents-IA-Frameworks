#app para agent frameworks con python y modelos 
#con openai y ollama

import asyncio
import os
from agent_framework.openai import OpenAIChatClient

async def main():
    agent = OpenAIChatClient(
        api_key="ollama",  # Placeholder, Ollama doesn't require an API key
        base_url=os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434/v1/"),
        model=os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    ).as_agent(
        name="HelpfulAssistant",
        instructions="You are a helpful assistant running locally via Ollama.",
    )
    consulta = input("Enter your question: ")
    result = await agent.run(consulta)
    print(result)

asyncio.run(main())