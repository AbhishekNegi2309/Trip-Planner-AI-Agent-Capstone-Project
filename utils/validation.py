def validate_itinerary_poi_ids(
    itinerary,
    allowed_pois
):

    valid_ids = set(
        allowed_pois.keys()
    )

    for day in itinerary["days"]:

        for block in [
            "morning",
            "afternoon",
            "evening"
        ]:

            for item in day[block]:

                if (
                    item["poi_id"]
                    not in valid_ids
                ):

                    raise ValueError(
                        f"Invalid poi_id: "
                        f"{item['poi_id']}"
                    )


import json
import time

def save_feedback(
    city_key,
    poi_id,
    vote
):

    event = {
        "ts": time.time(),
        "city_key": city_key,
        "poi_id": poi_id,
        "vote": vote
    }

    with open(
        "data/feedback.jsonl",
        "a"
    ) as f:

        f.write(
            json.dumps(event)
            + "\n"
        )


import pydeck as pdk
layer = pdk.Layer(
    "ScatterplotLayer",
    data=points,
    get_position="[lon, lat]",
    get_radius=35,
    radius_min_pixels=3,
    radius_max_pixels=10,
)