import streamlit as st
import folium
from streamlit_folium import st_folium


def show_weather_map(weather):
    """
    Display the selected city's location on an interactive map.
    """

    lat = weather["coord"]["lat"]
    lon = weather["coord"]["lon"]
    city = weather["name"]

    # Create Map
    weather_map = folium.Map(
        location=[lat, lon],
        zoom_start=10
    )

    # Add Marker
    folium.Marker(
        [lat, lon],
        popup=city,
        tooltip=city,
        icon=folium.Icon(color="blue", icon="cloud")
    ).add_to(weather_map)

    # Show Map
    st.subheader("🗺️ City Location")

    st_folium(
        weather_map,
        width=700,
        height=450
    )