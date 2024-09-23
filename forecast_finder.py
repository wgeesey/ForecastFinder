# forecast_finder.py
# W. Geesey
# Simple program to retrieve a forecast from weatherapi.com based off user input.


import requests, json


def forecast_finder(location, num_days):
    """
     Retrieve a weather forecast for a specified location and number of days.

     Parameters:
     location (str): The name of the location to get the forecast for.
     num_days (int): The number of days to retrieve the forecast.

     Returns:
     str: A formatted string containing the weather forecast.
     """

    # Used for simple debugging.
    # print(location)
    # print(num_days)

    # API key for weatherapi.com
    key = 'e2dfcda79bb44a58a31123829241809'
    # URL construct to be used in the request.
    api_url = f'http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days={num_days}'
    forecast_result = []

    try:
        # Send a get request to the api.
        response = requests.get(api_url)
        # Raise an exception for HTTP error responses.
        response.raise_for_status()
        # Parse JSON response.
        weather_data = response.json()
        print(json.dumps(weather_data, indent=4))
        # Extract the location name and start formatting the result.
        location_name = weather_data['location']['name']

        # Loop through each day in the forecast data.
        for day in weather_data['forecast']['forecastday']:
            date = day['date']
            avg_temp = day['day']['avgtemp_f']
            condition = day['day']['condition']['text']
            icon = day['day']['condition']['icon']

            if date and avg_temp is not None and condition:
                forecast_entry = {
                    'date': date,
                    'temperature': avg_temp,
                    'condition': condition,
                    'icon': icon,
                }

            forecast_result.append(forecast_entry)
            print("Appended Entry:", forecast_entry)

    except requests.exceptions.RequestException as e:
        print(f'Error fetching weather data. {e}')

    print("Final Forecast Result:", forecast_result)

    return forecast_result


def current_weather(location):
    key = 'e2dfcda79bb44a58a31123829241809'
    api_url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={location}'
    current_weather_data = {}

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = response.json()

        current_weather_data = {
            'location': weather_data['location']['name'],
            'temperature': weather_data['current']['temp_f'],
            'condition': weather_data['current']['condition']['text'],
            'humidity': weather_data['current']['humidity'],
            'icon': weather_data['current']['condition']['icon'],  # Weather icon URL
        }

    except requests.exceptions.RequestException as e:
        print(f'Error fetching current weather data. {e}')

    return current_weather_data
