# Real Estate Multi Agent System

## Project description

This project is a multi agent AI system for helping clients find residential properties.

The client gives their requirements such as location, budget, number of bedrooms and parking. The system then extracts the requirements, searches the available property data, checks the results and gives a recommendation.

The system was built using LangGraph, LangChain, Ollama and MCP.

## How the system works

The system has four main agents.

The client requirements agent reads the client's request and extracts the main requirements.

The property search agent searches the property data using an MCP tool.

The property analysis agent compares the properties with the client's requirements.

The recommendation agent gives the final recommendation based on the analysis.

There is also a safety check in the LangGraph workflow. It checks the location, budget, bedrooms and parking before properties are sent to the analysis agent.

## MCP tools

The MCP server provides two tools.

search_properties searches the property data using location, maximum price and bedrooms.

get_property_details gets the details of a property using its ID.

The property data is stored locally in properties.json.

## Technologies

Python

LangChain

LangGraph

Ollama

MCP

LangChain MCP Adapters

Jupyter Notebook

## Files

agents.py contains the agents.

graph.py contains the LangGraph workflow.

property_server.py contains the MCP server and tools.

properties.json contains the property data.

main.py runs the system from the terminal.

testing.ipynb contains the testing of the system.

requirements.txt contains the required Python packages.

## Running the project

Install the packages from requirements.txt.

Make sure Ollama is installed and the required model is available.

Run the following command from the project folder.

python main.py

The system will ask for the client's requirements and then provide a final recommendation.

## Testing

The system was tested with different property requirements.

The tests included normal matching requests, requests where parking was required, requests with no matching properties and different locations and budgets.

The system was also tested through the complete LangGraph workflow and through main.py from the terminal.

## Limitations

The property data is stored locally and is not connected to live real estate websites.

The system only searches the properties available in properties.json.

The client requirements are extracted using the local language model, so unusual or unclear requests may not always be interpreted correctly.

The system does not currently keep long term client memory between separate requests.

## Future improvements

The system could be connected to live real estate listing sources.

More property features could be added to the search.

The system could keep client preferences for future searches.

The recommendation agent could use more detailed property comparisons.

