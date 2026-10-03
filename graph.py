from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from agents import (
    client_requirements_agent,
    property_search_agent,
    property_analysis_agent,
    recommendation_agent
)


class AgentState(TypedDict):
    client_request: str
    requirements: dict
    properties: list
    analysis: str
    recommendation: str
    tools: list


def requirements_node(state):
    result = client_requirements_agent(state["client_request"])

    return {
        "requirements": result
    }


async def search_node(state):
    result = await property_search_agent(
        state["tools"],
        state["requirements"]
    )

    return {
        "properties": result
    }


def safety_node(state):
    requirements = state["requirements"]
    properties = state["properties"]

    budget = int(
        str(requirements["budget"])
        .replace("$", "")
        .replace(",", "")
    )

    safe_properties = []

    for property in properties:
        if (
            property["location"].lower() == requirements["location"].lower()
            and property["price"] <= budget
            and property["bedrooms"] == int(requirements["bedrooms"])
            and (
                not requirements["parking"]
                or property["parking"]
            )
        ):
            safe_properties.append(property)

    return {
        "properties": safe_properties
    }


def analysis_node(state):
    result = property_analysis_agent(
        state["properties"],
        state["requirements"]
    )

    return {
        "analysis": result
    }


def recommendation_node(state):
    result = recommendation_agent(
        state["analysis"]
    )

    return {
        "recommendation": result
    }


graph_builder = StateGraph(AgentState)

graph_builder.add_node("requirements", requirements_node)
graph_builder.add_node("search", search_node)
graph_builder.add_node("safety", safety_node)
graph_builder.add_node("analysis", analysis_node)
graph_builder.add_node("recommendation", recommendation_node)

graph_builder.add_edge(START, "requirements")
graph_builder.add_edge("requirements", "search")
graph_builder.add_edge("search", "safety")
graph_builder.add_edge("safety", "analysis")
graph_builder.add_edge("analysis", "recommendation")
graph_builder.add_edge("recommendation", END)