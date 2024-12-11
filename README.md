# osspj2024_WeatherForecast

# Weather Dashboard

A dynamic and visually appealing Weather Dashboard that provides current weather updates, an hourly forecast, and a 5-day forecast for cities worldwide. The dashboard features a user-friendly interface and real-time data powered by weather APIs.

## Features

- **Search by City**: Enter a city name to get the latest weather information.
- **Current Weather**: Displays the city name, temperature, weather description, humidity, and wind speed.
- **Hourly Forecast**: Shows weather predictions for the next few hours, including time, temperature, and a description.
- **5-Day Forecast**: Provides a daily summary of weather conditions for the next five days, including temperature ranges and weather icons.
- **Dynamic Background**: Includes animated cloud effects for an engaging user experience.
- **Responsive Design**: Optimized for various screen sizes using media queries.
- **Weather Emojis**: Maps weather conditions to intuitive emojis for enhanced user interaction.

## Technologies Used

- **Python (Flask)**: For server-side logic and routing.
- **HTML, CSS**: For structuring and styling the website.
- **Jinja2**: For templating dynamic content.
- **Weather API**: Retrieves real-time weather and forecast data from OpenWeatherMap.
- **pytz, datetime**: For handling timezone conversions and timestamps.

## Python Highlights

### API Integration
- Utilizes the OpenWeatherMap API for fetching weather data.
- Handles both current weather and forecasts using separate API endpoints (`/weather` and `/forecast`).

### Hourly Forecast
- Processes API data to generate a list of hourly forecasts for the next 24 hours.
- Uses 3-hour intervals and maps weather conditions to descriptive emojis.

### 5-Day Forecast
- Aggregates data into daily high and low temperatures.
- Assigns each day an emoji representing the predominant weather condition.

### Error Handling
- Provides feedback for invalid city names or connectivity issues.
- Displays user-friendly error messages on the interface.

### Weather Emojis
- Maps weather conditions (e.g., clear, rain, clouds) to emojis like ☀️ or 🌧️ for better visualization.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/weather-dashboard.git
   cd weather-dashboard
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an API key from your preferred weather API provider (e.g., OpenWeatherMap).

4. Add your API key to the project (e.g., in a `.env` file or directly in the code).

5. Run the application:
   ```bash
   flask run
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- Enter a city name in the search bar and click "Search" to view the weather details.
- Explore the hourly and 5-day forecasts for detailed insights.

## CSS Highlights

- **Color Palette**: Defined using CSS variables for easy theme management.
- **Animations**: Animated cloud effects and smooth hover/transition effects.
- **Responsiveness**: Media queries ensure compatibility with mobile and tablet devices.
- **Hover Effects**: Subtle scaling and color changes enhance interactivity.
- **Clean Layout**: Grid and flexbox layouts for intuitive organization of elements.

## Future Improvements

- Add interactive charts for weather trends.
- Implement a geolocation feature to fetch weather based on the user's location.
- Expand support for additional languages.
- Optimize for mobile and tablet devices.

## Contributors

- **Your Name** - Developer and Designer

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
