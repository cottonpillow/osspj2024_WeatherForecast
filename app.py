from flask import Flask, render_template, request
import requests
from datetime import datetime
import pytz

app = Flask(__name__)

    
API_KEY = 'dbc04e1a5675b8ef6b7642576598ba38'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'

def get_weather_emoji(weather_condition):
    """
    Map weather conditions to emojis
    """
    emoji_map = {
        'clear': '☀️',
        'clouds': '☁️',
        'rain': '🌧️',
        'drizzle': '🌦️',
        'thunderstorm': '⛈️',
        'snow': '❄️',
        'mist': '🌫️',
        'fog': '🌫️'
    }
    return emoji_map.get(weather_condition, '🌡️')

def get_hourly_forecast(city):
    """
    Fetch hourly forecast for the next 24 hours
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(FORECAST_URL, params=params)
        response.raise_for_status()
        forecast_data = response.json()

        hourly_forecast = []
        for entry in forecast_data['list'][:8]:  # Next 24 hours (3-hour intervals)
            timestamp = datetime.utcfromtimestamp(entry['dt'])
            weather_main = entry['weather'][0]['main'].lower()
            emoji = get_weather_emoji(weather_main)
            hourly_forecast.append({
                'time': timestamp.strftime('%I %p'),
                'temp': round(entry['main']['temp'], 1),
                'description': entry['weather'][0]['description'],
                'emoji': emoji
            })
        return hourly_forecast
    except:
        return None

def get_five_day_forecast(city):
    """
    Fetch 5-day weather forecast
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(FORECAST_URL, params=params)
        response.raise_for_status()
        forecast_data = response.json()

        daily_forecast = {}
        for entry in forecast_data['list']:
            date = datetime.utcfromtimestamp(entry['dt']).strftime('%A')
            temp = entry['main']['temp']
            weather_main = entry['weather'][0]['main'].lower()
            emoji = get_weather_emoji(weather_main)

            if date not in daily_forecast:
                daily_forecast[date] = {
                    'low': temp,
                    'high': temp,
                    'emoji': emoji
                }
            else:
                daily_forecast[date]['low'] = min(daily_forecast[date]['low'], temp)
                daily_forecast[date]['high'] = max(daily_forecast[date]['high'], temp)

        return [{'day': day, 'low': round(data['low'], 1), 'high': round(data['high'], 1), 'emoji': data['emoji']} for day, data in daily_forecast.items()]
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    hourly_forecast = None
    five_day_forecast = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            try:
                params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
                response = requests.get(WEATHER_URL, params=params)
                weather_data = response.json()

                hourly_forecast = get_hourly_forecast(city)
                five_day_forecast = get_five_day_forecast(city)

                if 'main' not in weather_data:
                    error = "City not found. Please try again."
            except Exception as e:
                error = "Unable to fetch weather data. Please try again."

    return render_template('index.html', weather=weather_data, hourly_forecast=hourly_forecast, five_day_forecast=five_day_forecast, error=error)

if __name__ == '__main__':
    app.run(debug=True)
