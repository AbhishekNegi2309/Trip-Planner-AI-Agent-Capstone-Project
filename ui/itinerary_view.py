import streamlit as st
import json


def render_activity(activity):
    """
    Render a single activity card.
    """

    st.markdown(
        f"""
        ### 📍 {activity.get('name', 'Unknown')}
        **Category:** {activity.get('category', 'N/A')}

        **Why Visit?**
        {activity.get('why', '')}
        """
    )

    if activity.get("source"):
        st.caption(
            f"Source: {activity['source']}"
        )


def render_day(day):
    """
    Render one day of itinerary.
    """

    st.markdown("---")
    st.header(f"Day {day['day']}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🌅 Morning")

        for activity in day.get(
            "morning",
            []
        ):
            render_activity(activity)

    with col2:
        st.subheader("☀️ Afternoon")

        for activity in day.get(
            "afternoon",
            []
        ):
            render_activity(activity)

    with col3:
        st.subheader("🌙 Evening")

        for activity in day.get(
            "evening",
            []
        ):
            render_activity(activity)


def render_itinerary(itinerary):
    """
    Main itinerary renderer.
    """

    st.title("🗺️ Generated Itinerary")

    if not itinerary:
        st.warning(
            "No itinerary generated yet."
        )
        return

    for day in itinerary.get(
        "days",
        []
    ):
        render_day(day)

    st.markdown("---")

    st.download_button(
        label="⬇️ Download Itinerary JSON",
        data=json.dumps(
            itinerary,
            indent=2
        ),
        file_name="itinerary.json",
        mime="application/json"
    )