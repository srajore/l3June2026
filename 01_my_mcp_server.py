from fastmcp import FastMCP
from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()

import os

mcp = FastMCP("My First MCP Server")

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool
def add(a: int, b: int) -> int:
    ''' this is performing addition of two numbers '''
    return a + b

@mcp.tool
def search_web(query:str) -> dict:
    """
        Search the web using Tavily.
    """
    return tavily_client.search(
        query=query,
        max_results=3
        )


if __name__ == "__main__":
    #mcp.run(transport="http", port=8000)
    mcp.run()


    #uv run 01_my_mcp_server.py