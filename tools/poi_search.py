import requests
import streamlit as st

USER_AGENT = (
    "trip-planner-capstone/1.0 "
    "(contact@example.com)"
)

INTEREST_TO_TAGS = {
    "museums": [
        ("tourism", "museum|gallery")
    ],

    "food": [
        ("amenity", "restaurant|cafe|fast_food")
    ],

    "outdoors": [
        ("leisure", "park|nature_reserve"),
        ("natural", "peak|beach")
    ],

    "history": [
        ("historic", "castle|monument")
    ]
}

import streamlit as st
@st.cache_data(ttl=3600)
def geocode_city(city):

    headers = {
        "User-Agent": USER_AGENT
    }

    response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={
            "q": city,
            "format": "json",
            "limit": 1
        },
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    results = response.json()

    if not results:
        raise ValueError(
            f"No results found for {city}"
        )

    return {
        "lat": float(results[0]["lat"]),
        "lon": float(results[0]["lon"])
    }


@st.cache_data(ttl=3600)
def search_pois(city, interests):

    location = geocode_city(city)

    lat = location["lat"]
    lon = location["lon"]

    pois = []

    for interest in interests:

        tags = INTEREST_TO_TAGS.get(
            interest,
            []
        )

        for key, value in tags:

            query = f"""
            [out:json];
            (
              node
                ["{key}"~"{value}"]
                (around:10000,{lat},{lon});
            );
            out body;
            """

            response = requests.post(
                "https://overpass-api.de/api/interpreter",
                data=query,
                headers={
                    "User-Agent": USER_AGENT
                }
            )

            response.raise_for_status()

            data = response.json()

            for element in data["elements"]:

                pois.append({
                    "poi_id": f"osm_{element['id']}",
                    "name": element["tags"].get(
                        "name",
                        "Unnamed"
                    ),
                    "category": interest,
                    "lat": element["lat"],
                    "lon": element["lon"],
                    "url": element["tags"].get(
                        "website",
                        ""
                    )
                })

    return pois
