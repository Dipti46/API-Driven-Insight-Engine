"""
Smart Recommendation Engine
Generates intelligent weather-based suggestions.
"""


def get_weather_recommendations(weather, air_quality=None):

    recommendations = []

    temperature = weather["main"]["temp"]
    humidity = weather["main"]["humidity"]
    wind_speed = weather["wind"]["speed"]

    weather_main = weather["weather"][0]["main"].lower()
    weather_desc = weather["weather"][0]["description"].lower()

    # Weather Condition

    if weather_main == "clear":

        recommendations.append("☀ Clear skies today.")

        if temperature > 42:
            recommendations.append("🥵 Extremely hot weather.")
            recommendations.append("🏠 Stay indoors during peak afternoon hours.")
            recommendations.append("💧 Drink plenty of water.")

        elif temperature > 38:
            recommendations.append("🌞 It's a very hot day.")
            recommendations.append("🥤 Stay hydrated throughout the day.")

        elif temperature > 32:
            recommendations.append("🌡 It may feel warm outside.")
            recommendations.append("🧴 Apply sunscreen before going outside.")

    elif weather_main == "clouds":

        recommendations.append("☁ Cloudy weather expected today.")

        if temperature >= 32:
            recommendations.append("🌡 It may still feel warm. Stay hydrated.")

    elif weather_main == "rain":

        recommendations.append("☔ Carry an umbrella before heading out.")
        recommendations.append("🚶 Roads may be slippery. Walk carefully.")

    elif weather_main == "drizzle":

        recommendations.append("🌦 Light rain expected.")
        recommendations.append("☂ Carry an umbrella just in case.")

    elif weather_main == "thunderstorm":

        recommendations.append("⚡ Thunderstorms expected.")
        recommendations.append("🏠 Stay indoors whenever possible.")
        recommendations.append("🔌 Avoid using electrical appliances during lightning.")

    elif weather_main == "snow":

        recommendations.append("❄ Snowfall expected.")
        recommendations.append("🧥 Wear warm clothes.")
        recommendations.append("🚗 Drive carefully on slippery roads.")

    elif weather_main in ["mist", "fog", "haze"]:

        recommendations.append("🌫 Low visibility expected.")
        recommendations.append("🚗 Drive carefully.")

    # Temperature

    if temperature >= 40:

        recommendations.append("🥵 Extremely hot weather.")
        recommendations.append("🚫 Avoid going outside during afternoon hours.")

    elif 30 <= temperature < 40:

        recommendations.append("💧 Drink plenty of water to stay hydrated.")

    elif temperature <= 10:

        recommendations.append("🥶 Cold weather.")
        recommendations.append("🧥 Wear warm clothing before going outside.")

    # Humidity

    if humidity >= 85:

        recommendations.append("💦 High humidity may cause discomfort.")

    elif humidity <= 30:

        recommendations.append("💧 Dry weather. Keep yourself hydrated.")

    # Wind

    if wind_speed >= 10:

        recommendations.append("🌬 Strong winds expected.")
        recommendations.append("🚴 Ride carefully and secure loose objects.")

    # Air Quality

    if air_quality is not None:

        aqi = air_quality["list"][0]["main"]["aqi"]

        if aqi == 1:

            recommendations.append("😊 Air quality is excellent. Outdoor activities are safe.")

        elif aqi == 2:

            recommendations.append("🙂 Air quality is good for most people.")

        elif aqi == 3:

            recommendations.append("😷 Sensitive individuals should consider wearing a mask.")

        elif aqi == 4:

            recommendations.append("🌫 Air quality is poor.")
            recommendations.append("😷 Wear a mask if staying outdoors.")
            recommendations.append("🏃 Avoid prolonged outdoor exercise.")

        elif aqi == 5:

            recommendations.append("🚨 Air quality is very poor.")
            recommendations.append("😷 Wear an N95 mask.")
            recommendations.append("🏠 Stay indoors and keep windows closed.")

    # Default

    if not recommendations:

        recommendations.append("✅ Weather looks pleasant. Have a great day!")

    return recommendations