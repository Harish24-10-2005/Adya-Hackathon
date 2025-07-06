import asyncio
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b"
)

client = MultiServerMCPClient({
    "pagerduty": {
        "url": "http://127.0.0.1:8000/mcp/",
        "transport": "streamable_http",
    },
    "bugsnag": {

        "command": "node",
        "args": ["D:/Adya/MCPs/bugsnag-mcp/build/index.js"],
        "transport": "stdio",
        "env": {
            "BUGSNAG_API_KEY": "#-#-#-##-#"
        },
        "disabled": False,
        "alwaysAllow":[]
    },
    "redhat": {
        "command": "uv",
        "args": [
            "run",
            "redhat_mcp_server.py"
        ],
        "cwd": "D:/Adya/MCPs_Server/redhat-api-mcp",
        "transport": "stdio",
        "env": {
            "RH_API_OFFLINE_TOKEN": "##.##.#-#"
        }
    },
    "LangSmith API MCP Server": {
            "command": "D:/Adya/MCPs/langsmith-mcp-server/.venv/Scripts/python.exe",
            "args": [
                "-m",
                "langsmith_mcp_server.server"
            ],
            "cwd": "D:/Adya/MCPs/langsmith-mcp-server",
            "transport": "stdio",
            "env": {
                "LANGSMITH_API_KEY": "#####"
            }
    }
})

async def main():
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    response = await agent.ainvoke({
        "messages": [{"role": "user", "content": "list the datasets in langsmith"}]
    })
    for i in response["messages"]:
        i.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())
