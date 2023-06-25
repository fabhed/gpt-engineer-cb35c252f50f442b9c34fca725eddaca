from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather_data():
    """Fetches the current weather data for Stockholm from the OpenWeatherMap API."""
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Stockholm,SE&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    """Renders the main page with the current weather in Stockholm."""
    weather_data = get_weather_data()
    current_temperature = weather_data['main']['temp']
    return render_template('index.html', temperature=current_temperature)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
