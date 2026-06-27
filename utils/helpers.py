from datetime import datetime


def format_temperature(temp):
    return f"{temp} °C"


def format_visibility(visibility):
    return f"{visibility / 1000:.1f} km"


def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%I:%M %p")


def get_aqi_status(aqi):

    status = {
        1: "Good 😊",
        2: "Fair 🙂",
        3: "Moderate 😐",
        4: "Poor 😷",
        5: "Very Poor ⚠️"
    }

    return status.get(aqi, "Unknown")