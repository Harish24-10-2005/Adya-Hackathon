import asyncio
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

llm = ChatGroq(
    model="qwen-qwq-32b"
)

client = MultiServerMCPClient({
    "pagerduty": {
        "command": "uv",
        "args": [
            "run",
            "python",
            "-m",
            "pagerduty_mcp_server"
        ],
        "cwd": "D:/Adya/MCPs_Server/pagerduty-mcp-server",
        "transport": "stdio",
        "env": {
            "PAGERDUTY_API_TOKEN": "###"
        }
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
        "messages": [{"role": "user", "content": "show all escalation policies available in team id PIBQIWK in pagerduty"}]
    })
    for i in response["messages"]:
        i.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())
