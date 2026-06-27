import streamlit as st
import pandas as pd


def show_forecast_chart(forecast):

    forecast_list = forecast.get("list", [])

    if not forecast_list:
        st.warning("Forecast data not available.")
        return

    data = []

    for item in forecast_list:

        data.append({
            "Date & Time": item["dt_txt"],
            "Temperature (°C)": item["main"]["temp"],
            "Humidity (%)": item["main"]["humidity"]
        })

    df = pd.DataFrame(data)

    st.subheader("📈 5-Day Weather Forecast")

    st.line_chart(
        data=df,
        x="Date & Time",
        y="Temperature (°C)"
    )

    st.line_chart(
        data=df,
        x="Date & Time",
        y="Humidity (%)"
    )