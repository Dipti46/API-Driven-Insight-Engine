import streamlit as st

from services.weather_api import (
    get_current_weather,
    get_forecast,
    get_air_quality,
    is_api_key_available
)

from components.air_quality import show_air_quality

from services.recommendations import get_weather_recommendations

from components.dashboard import show_weather_cards
from components.charts import show_forecast_chart
from components.maps import show_weather_map


# Page Configuration

st.set_page_config(
    page_title="WeatherPulse Dashboard",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# API Validation

if not is_api_key_available():
    st.error("❌ OpenWeather API Key not found.")
    st.info("Please add your API key inside the .env file.")
    st.stop()


# Session State

if "weather" not in st.session_state:
    st.session_state.weather = None

if "forecast" not in st.session_state:
    st.session_state.forecast = None

if "air_quality" not in st.session_state:
    st.session_state.air_quality = None

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []


# Sidebar

with st.sidebar:

    st.title("🌦️ WeatherPulse Dashboard")
    st.markdown("---")

    city = st.text_input(
        "📍 Enter City Name",
        placeholder="e.g. Delhi"
    )

    search_btn = st.button(
        "🔍 Search Weather",
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🕘 Recent Searches")
    st.info("No recent searches")


# Main Page

st.title("🌤️ WeatherPulse Dashboard")

st.write(
    "Get current weather, AQI, forecast, interactive charts "
    "and smart weather recommendations."
)

st.divider()


# Search

if search_btn:

    if city.strip() == "":
        st.warning("⚠️ Please enter a city name.")

    else:

        weather = get_current_weather(city)

        if weather is None:
            st.error("❌ City not found or API Error.")

        else:

            forecast = get_forecast(city)

            lat = weather["coord"]["lat"]
            lon = weather["coord"]["lon"]

            air_quality = get_air_quality(lat, lon)

            recommendations = get_weather_recommendations(
                weather,
                air_quality
            )

            st.session_state.weather = weather
            st.session_state.forecast = forecast
            st.session_state.air_quality = air_quality
            st.session_state.recommendations = recommendations


# Display Data

if st.session_state.weather is not None:

    st.success(
        f"✅ Weather data loaded for {st.session_state.weather['name']}"
    )

    show_weather_cards(st.session_state.weather)

    st.subheader("💡 Smart Recommendations")

    for recommendation in st.session_state.recommendations:
        st.write(recommendation)

    show_forecast_chart(st.session_state.forecast)

    show_air_quality(st.session_state.air_quality)

    show_weather_map(st.session_state.weather)