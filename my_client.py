import asyncio
from fastmcp import Client

#client = Client("http://localhost:8000/mcp")
client = Client("01_my_mcp_server.py")

async def call_tool(query: str):
    async with client:
        #result = await client.call_tool("greet", {"name": name})
        tools = await client.list_tools()

        result = await client.call_tool("search_web", {"query": query})

        # for tool in result:
        #     print(f"Tool Name: {tool.name}, Description: {tool.description or 'No description'}")

        #print(tools)
        print(f"Result: {result}")

asyncio.run(call_tool("What are the latest advancements in AI technology?"))