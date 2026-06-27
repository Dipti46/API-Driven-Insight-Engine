# 🌤️ WeatherPulse Dashboard

A comprehensive weather monitoring dashboard built using Python and Streamlit. This application allows users to fetch real-time weather data, analyze air quality, view 5-day forecasts, and get intelligent recommendations based on local weather conditions.

## 🔌 API Integration & Data Visualization

I have developed this **Weather Report Dashboard** by integrating the **OpenWeatherMap API**. Through this dashboard, you can easily view the weather report of any city, including various visualizations to better understand the data and analyze different parameters.

## 📚 Features

* **Weather Data:** Fetches live temperature, humidity, wind speed, pressure, and visibility.
* **Interactive Charts:** Uses visual plots to track temperature and humidity trends over 5 days.
* **Air Quality Index (AQI):** Monitors air pollutants like PM2.5, PM10, CO, NO2, etc., to provide an AQI status.
* **Geographic Mapping:** Displays the city's location using OpenStreetMap integration.
* **Smart Recommendations:** Provides context-aware suggestions (e.g., "Stay hydrated," "Wear a mask") based on the current weather and air quality.

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Data Source:** OpenWeatherMap API
* **Mapping:** Folium & Streamlit-Folium
* **Data Analysis:** Pandas, NumPy
* **IDE:** Visual Studio Code

## 🚀 How to Run

1. **Clone the repository** or download the files to your local machine.

2. **Setup:** Ensure you have Python installed. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. **API Key:** Create a (.env) file in the project root and add your OpenWeatherMap API key:
    (OPENWEATHER_API_KEY=your_api_key_here)

4. **Run the Dashboard:** Open your terminal in the project folder and run:
    (streamlit run main.py)

***Note: An active internet connection is required to fetch data from the API.***


![Dashboard Overview](https://github.com/user-attachments/assets/25b2bffb-5dae-4dd3-a938-60825704ded9)
![Recommendations](https://github.com/user-attachments/assets/932c0948-c672-436a-af63-c35b31f34681)
![Weather Forecast](https://github.com/user-attachments/assets/53b53881-d879-4da9-bba6-db787c5419f2)
![Air Quality](https://github.com/user-attachments/assets/84eae1f6-d374-4b62-8a62-1a087dcddd93)
![Map](https://github.com/user-attachments/assets/f41d056c-4a85-49c1-b23a-9d5f9a261fdc)