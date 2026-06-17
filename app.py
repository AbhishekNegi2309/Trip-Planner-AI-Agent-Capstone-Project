import streamlit as st
from agents.planner_agent import run_trip_planner
from ui.itinerary_view import render_itinerary
from ui.map_view import render_map

st.set_page_config(
    page_title="AI Trip Planner",
    layout="wide"
)

st.title("🌍 AI Trip Planner Agent")

if "itinerary" not in st.session_state:
    st.session_state.itinerary = None

with st.sidebar:
    st.header("Configuration")

    api_key = st.text_input(
        "OpenAI API Key",
        type="password"
    )

    model_name = st.selectbox(
        "Model",
        ["gpt-4.1", "gpt-4o"]
    )

destination = st.text_input("Destination")

days = st.slider(
    "Trip Length",
    1,
    14,
    3
)

pace = st.selectbox(
    "Pace",
    ["Relaxed", "Balanced", "Fast"]
)

interests = st.multiselect(
    "Interests",
    [
        "food",
        "museums",
        "outdoors",
        "history"
    ]
)

constraints = st.text_area(
    "Constraints"
)

if st.button("Generate Itinerary"):

    with st.spinner("Agent is planning your trip..."):

        itinerary = run_trip_planner(
            destination,
            days,
            interests,
            pace,
            constraints,
            api_key,
            model_name
        )

        st.session_state.itinerary = itinerary

if st.session_state.itinerary:
    render_itinerary(st.session_state.itinerary)
    render_map(st.session_state.itinerary)