import json
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma4:e4b",
    temperature=0
)


def client_requirements_agent(client_request):
    prompt = f"""
You are a client requirements agent for a real estate system.

Read the client's request and identify these requirements:

location
budget
bedrooms
parking

Return only a JSON object with these four fields.

Client request:
{client_request}
"""

    result = llm.invoke(prompt)

    text = result.content.replace("```json", "").replace("```", "").strip()

    requirements = json.loads(text)

    return requirements


async def property_search_agent(tools, requirements):
    budget = requirements["budget"]
    budget = int(str(budget).replace("$", "").replace(",", ""))

    search_tool = next(
        tool for tool in tools
        if tool.name == "search_properties"
    )

    result = await search_tool.ainvoke({
        "location": requirements["location"],
        "max_price": budget,
        "bedrooms": int(requirements["bedrooms"])
    })

    properties = []

    for item in result:
        if item.get("type") == "text":
            properties.append(json.loads(item["text"]))

    return properties


def property_analysis_agent(properties, requirements):
    if not properties:
        return "No properties match the client's requirements."

    prompt = f"""
You are a property analysis agent.

Compare the properties with the client's requirements.

Client requirements:
{requirements}

Properties:
{properties}

For each property, explain briefly whether it matches the requirements.
Pay special attention to budget, bedrooms, location and parking.

Then identify the properties that are the best matches.

Keep the answer simple.
"""

    result = llm.invoke(prompt)

    return result.content


def recommendation_agent(analysis):
    if analysis == "No properties match the client's requirements.":
        return analysis

    prompt = f"""
You are a real estate recommendation agent.

Read the property analysis below and give the client a final recommendation.

Property analysis:
{analysis}

Recommend the properties that best match the client's requirements.
Briefly explain why they are suitable.

Do not recommend properties that were identified as not matching.

Keep the answer simple and clear.
"""

    result = llm.invoke(prompt)

    return result.content