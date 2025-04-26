

### **Project: AI Assistant with MCP Servers (LangChain + Groq)**  
**Technologies:** MCP (Model Context Protocol), LangChain, Groq (Llama3-8B), Cursor IDE (MCP Host), Streamlit/Flask, MCP Servers (Playwright, Airbnb, DuckDuckGoSearch)  

#### **Key Features & Achievements**  
1. **MCP-Powered Multi-Source Integration**  
   - Built an AI assistant that dynamically connects to **MCP servers** (Playwright for web automation, Airbnb/DuckDuckGo for real-time data) via a configurable `MCPClient`.  
   - Leveraged **LangChain's agent framework** to orchestrate context-aware interactions between Groq’s LLM (`llama3-8b-8192`) and MCP services.  

2. **Conversational Memory & Stateful Dialog**  
   - Implemented persistent conversation history (`memory_enabled=True`) to retain context across user queries, enabling coherent long-term interactions.  
   - Added user commands (`clear`, `exit`) to manage session state dynamically.  

3. **Scalable & Fault-Tolerant Design**  
   - Used **asynchronous I/O** (`asyncio`) for non-blocking MCP server calls, ensuring responsiveness.  
   - Deployed error handling and session cleanup to gracefully manage API failures (`client.close_sessions()`).  

#### **Technical Highlights**  
- **MCP Protocol**: Customized `MCPAgent` to route queries between LLM and external services (e.g., scrape data via Playwright, fetch listings from Airbnb).  
- **Groq Optimization**: Utilized Groq’s ultra-low-latency API for real-time inference.  
- **Config-Driven**: Server endpoints defined in `browser_mcp.json` for modularity.  

**Impact:** Enabled accurate, multi-source responses (e.g., travel queries combining Airbnb data + DuckDuckGo search) with a single chatbot interface.  

---  

### **Code Snippet Summary**  
```python
# 1. Initialize MCP client with servers (Playwright, Airbnb, etc.)
client = MCPClient.from_config_file("browser_mcp.json")  

# 2. Set up Groq's Llama3 LLM
llm = ChatGroq(model="llama3-8b-8192")  

# 3. Create agent with memory
agent = MCPAgent(llm=llm, memory_enabled=True, client=client)  

# 4. Run interactive chat loop
response = await agent.run(user_input)  # Fetches data from MCP servers + LLM
```  

---  

### **Why It Stands Out**  
- **Beyond RAG**: Unlike static retrieval, your MCP agent **actively pulls live data** from diverse APIs/web sources.  
- **User-Centric**: Memory and session controls mimic commercial chatbots (e.g., ChatGPT).  

