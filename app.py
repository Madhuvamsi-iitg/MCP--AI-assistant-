"""
simple chat example using MCP agent with built in conversation memeory
"""

import asyncio
from mcp_use import MCPAgent, MCPClient
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
import os


async def run_memory_chat():
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    config_file = "browser_mcp.json"
    print("Initializing chat")

    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model_name="llama3-8b-8192")

    #vcreate agent with memory_enabled=true
    agent = MCPAgent(
        llm=llm,
        memory_enabled=True,
        client=client,
        max_steps=15,
        verbose=True
    )

    print("\n =====Interactive MCP chat=====")


    try:

        while True:

            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat")
                break

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared")
                continue
            #get response from agent
            print("\nAssistant: ", end="", flush=True)

            try:
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally:
        if client and client.sessions:
            await client.close_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())

      
            
            
    
  
