# forecast_finder.py
# W. Geesey
# Simple program to retrieve a forecast from weatherapi.com based off user input.


import requests


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
    key = 'ENTER YOUR API KEY HERE'
    # URL construct to be used in the request.
    api_url = f'http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days={num_days}'
    forecast_result = ''

    try:
        # Send a get request to the api.
        response = requests.get(api_url)
        # Raise an exception for HTTP error responses.
        response.raise_for_status()
        # Parse JSON response.
        weather_data = response.json()

        # Extract the location name and start formatting the result.
        location_name = weather_data['location']['name']
        forecast_result += f"Your {num_days} day forecast for {location_name}:\n\n"

        # Loop through each day in the forecast data.
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
