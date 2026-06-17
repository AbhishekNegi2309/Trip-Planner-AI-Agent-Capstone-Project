import streamlit as st
import pydeck as pdk
import pandas as pd


def extract_points(itinerary):
    """
    Convert itinerary activities
    into map points.
    """

    points = []

    for day in itinerary.get(
        "days",
        []
    ):

        for block in [
            "morning",
            "afternoon",
            "evening"
        ]:

            for item in day.get(
                block,
                []
            ):

                if (
                    item.get("lat")
                    and item.get("lon")
                ):

                    points.append(
                        {
                            "name":
                                item["name"],

                            "category":
                                item.get(
                                    "category",
                                    ""
                                ),

                            "lat":
                                item["lat"],

                            "lon":
                                item["lon"],

                            "day":
                                day["day"],

                            "block":
                                block
                        }
                    )

    return pd.DataFrame(points)


def calculate_view(points):

    center_lat = points["lat"].mean()

    center_lon = points["lon"].mean()

    return pdk.ViewState(
        latitude=center_lat,
        longitude=center_lon,
        zoom=11,
        pitch=40
    )


def render_map(itinerary):

    st.header("🗺️ Trip Map")

    points = extract_points(
        itinerary
    )

    if points.empty:
        st.info(
            "No location data available."
        )
        return

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=points,
        get_position="[lon, lat]",
        get_radius=35,
        radius_min_pixels=3,
        radius_max_pixels=10,
        pickable=True
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=
        calculate_view(points),
        tooltip={
            "html":
            """
            <b>{name}</b><br/>
            {category}<br/>
            Day {day}<br/>
            {block}
            """
        }
    )

    st.pydeck_chart(deck)