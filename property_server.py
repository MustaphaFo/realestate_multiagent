import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("properties")

with open("properties.json", "r") as file:
    properties = json.load(file)


@mcp.tool()
def search_properties(
    location: str,
    max_price: int,
    bedrooms: int
) -> list:
    """Search for properties based on location, budget and bedrooms."""
    
    results = []

    for property in properties:
        if (
            property["location"].lower() == location.lower()
            and property["price"] <= max_price
            and property["bedrooms"] == bedrooms
        ):
            results.append(property)

    return results


@mcp.tool()
def get_property_details(property_id: int) -> dict:
    """Get the details of a property using its id."""

    for property in properties:
        if property["id"] == property_id:
            return property

    return {"error": "Property not found"}


if __name__ == "__main__":
    mcp.run(transport="stdio")