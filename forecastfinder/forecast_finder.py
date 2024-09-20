import requests


def forecast_finder(location, num_days):
    print(location)
    print(num_days)

    key = 'e2dfcda79bb44a58a31123829241809'
    api_url = f'http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days={num_days}'
    forecast_result = ''

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = response.json()

        location_name = weather_data['location']['name']
        forecast_result += f"Your {num_days} day forecast for {location_name}:\n\n"

        for day in weather_data['forecast']['forecastday']:
            date = day['date']
            avg_temp = day['day']['avgtemp_f']
            condition = day['day']['condition']['text']
            forecast_result += (f"Date: {date}\n"
                                f"Average temperature: {avg_temp}\u00B0F\n"
                                f"Conditions: {condition}\n\n")

    except requests.exceptions.RequestException as e:
        print(f'Error fetching weather data. {e}')

    return forecast_result
