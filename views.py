from django.shortcuts import render

from .forecast_finder import forecast_finder, current_weather


# Create my views here.
def index(request):
    forecast_result = []
    current_weather_data = {}
    if request.method == 'POST':
        location = request.POST.get('location')
        num_days = request.POST.get('num_days')
        if location and num_days:
            print(f"Location: {location}, Number of Days: {num_days}")
            forecast_result = forecast_finder(location, int(num_days))
            current_weather_data = current_weather(location)
    return render(request, 'index.html', {'forecast': forecast_result,
                                          'current_weather': current_weather_data})
