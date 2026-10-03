import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient

from graph import graph_builder


async def main():
    client = MultiServerMCPClient(
        {
            "properties": {
                "command": "python",
                "args": ["property_server.py"],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()

    graph = graph_builder.compile()

    client_request = input("Enter the client's requirements: ")

    result = await graph.ainvoke({
        "client_request": client_request,
        "tools": tools
    })

    print("\nFinal recommendation:")
    print(result["recommendation"])


if __name__ == "__main__":
    asyncio.run(main())