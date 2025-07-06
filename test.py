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
            "BUGSNAG_API_KEY": "943769e3-a508-4b21-82ed-8e5e6ea93d05"
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
            "RH_API_OFFLINE_TOKEN": "eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0NzQzYTkzMC03YmJiLTRkZGQtOTgzMS00ODcxNGRlZDc0YjUifQ.eyJpYXQiOjE3NTE1MTU1OTQsImp0aSI6ImY5NjRmODExLWJlZmQtNDc0ZS1iNWUwLTYxNmYwMDI0NDRkYSIsImlzcyI6Imh0dHBzOi8vc3NvLnJlZGhhdC5jb20vYXV0aC9yZWFsbXMvcmVkaGF0LWV4dGVybmFsIiwiYXVkIjoiaHR0cHM6Ly9zc28ucmVkaGF0LmNvbS9hdXRoL3JlYWxtcy9yZWRoYXQtZXh0ZXJuYWwiLCJzdWIiOiJmOjUyOGQ3NmZmLWY3MDgtNDNlZC04Y2Q1LWZlMTZmNGZlMGNlNjpkZWF2YW5hdGhhbiIsInR5cCI6Ik9mZmxpbmUiLCJhenAiOiJyaHNtLWFwaSIsInNpZCI6IjUwNWU4YWUwLTZhNDEtNDVjMi05NmQ3LWU4NzUyOGIzMDE3OCIsInNjb3BlIjoiYmFzaWMgcm9sZXMgd2ViLW9yaWdpbnMgY2xpZW50X3R5cGUucHJlX2tjMjUgb2ZmbGluZV9hY2Nlc3MifQ.HnzQ70jYMO5n8378Sxdz6nEIpUrZjkROstvehzMbfmifKD9Nj9Dh__DE-Btnihasr0nHYKCItSxJm5Bo6zuCVQ"
        }
    }
})

async def main():
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    response = await agent.ainvoke({
        "messages": [{"role": "user", "content": "what are tool u have access in redhat"}]
    })
    for i in response["messages"]:
        i.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())
