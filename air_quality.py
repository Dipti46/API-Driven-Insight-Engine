import streamlit as st

from utils.helpers import get_aqi_status


def show_air_quality(air_quality):

    if air_quality is None:
        st.warning("Air Quality data not available.")
        return

    data = air_quality["list"][0]

    aqi = data["main"]["aqi"]
    components = data["components"]

    st.subheader("🌫 Air Quality")

    st.metric(
        "Air Quality Index (AQI)",
        get_aqi_status(aqi)
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "PM2.5",
            f"{components['pm2_5']} µg/m³"
        )

        st.metric(
            "CO",
            f"{components['co']}"
        )

        st.metric(
            "NH₃",
            f"{components['nh3']}"
        )

    with col2:
        st.metric(
            "PM10",
            f"{components['pm10']} µg/m³"
        )

        st.metric(
            "NO",
            f"{components['no']}"
        )

        st.metric(
            "NO₂",
            f"{components['no2']}"
        )

    with col3:
        st.metric(
            "O₃",
            f"{components['o3']}"
        )

        st.metric(
            "SO₂",
            f"{components['so2']}"
        )