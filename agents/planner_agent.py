from openai import OpenAI
from tools.poi_search import search_pois
import json
from agents.schemas import TOOLS

def run_trip_planner(
    city,
    days,
    interests,
    pace,
    constraints,
    api_key,
    model
):

    client = OpenAI(
        api_key=api_key
    )

    tool_state = {
        "pois": {}
    }

    prompt = f"""
    Create a {days}-day itinerary
    for {city}.

    Interests:
    {interests}

    Pace:
    {pace}

    Constraints:
    {constraints}
    """

    response = client.responses.create(
        model=model,
        input=prompt,
        tools=TOOLS
    )

    for item in response.output:

        if item.type == "function_call":

            args = json.loads(
                item.arguments
            )

            pois = search_pois(
                args["city"],
                args["interests"]
            )

            for poi in pois:
                tool_state["pois"][
                    poi["poi_id"]
                ] = poi

    final_response = client.responses.create(
        model=model,
        input=f"""
        Tool Results:
        {json.dumps(list(tool_state["pois"].values()))}

        Create final itinerary.
        """
    )

    return json.loads(
        final_response.output_text
    )