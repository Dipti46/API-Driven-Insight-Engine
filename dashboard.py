import streamlit as st

from utils.helpers import format_time, format_visibility


def show_weather_cards(weather):

    city = weather.get("name", "Unknown City")
    country = weather.get("sys", {}).get("country", "")

    main = weather.get("main", {})
    wind = weather.get("wind", {})
    clouds = weather.get("clouds", {})
    weather_info = weather.get("weather", [{}])[0]
    sys = weather.get("sys", {})

    st.subheader(f"📍 {city}, {country}")

    st.markdown(
        f"**Current Weather:** {weather_info.get('description', 'N/A').title()}"
    )

    st.divider()

    # -------------------------
    # First Row
    # -------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🌡 Temperature",
            f"{main.get('temp', '--')} °C"
        )

    with col2:
        st.metric(
            "💧 Humidity",
            f"{main.get('humidity', '--')} %"
        )

    with col3:
        st.metric(
            "🌬 Wind Speed",
            f"{wind.get('speed', '--')} m/s"
        )

    with col4:
        st.metric(
            "🤗 Feels Like",
            f"{main.get('feels_like', '--')} °C"
        )

    st.divider()

    # -------------------------
    # Second Row
    # -------------------------

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric(
            "🔵 Pressure",
            f"{main.get('pressure', '--')} hPa"
        )

    with col6:
        st.metric(
            "☁ Cloudiness",
            f"{clouds.get('all', '--')} %"
        )

    with col7:
        st.metric(
            "👀 Visibility",
            format_visibility(weather.get("visibility", 0))
        )

    with col8:
        st.metric(
            "🌤 Condition",
            weather_info.get("main", "--")
        )

    st.divider()

    # -------------------------
    # Sunrise & Sunset
    # -------------------------

    col9, col10 = st.columns(2)

    with col9:
        st.metric(
            "🌅 Sunrise",
            format_time(sys.get("sunrise", 0))
        )

    with col10:
        st.metric(
            "🌇 Sunset",
            format_time(sys.get("sunset", 0))
        )