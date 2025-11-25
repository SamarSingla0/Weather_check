from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):

    # City detection
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'

    WEATHER_API_KEY = ''
    SEARCH_ENGINE_ID = ''

    # WEATHER API URL
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
    PARAMS = {'units': 'metric'}

    # GOOGLE IMAGE SEARCH URL
    query = f"{city} 1920x1080"
    google_url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={WEATHER_API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
        f"&searchType=image&imgSize=xlarge"
    )

    # IMAGE FETCH
    try:
        img_data = requests.get(google_url).json()
        image_url = img_data["items"][0]["link"]
    except:
        image_url = None

    # WEATHER FETCH
    try:
        data = requests.get(weather_url, params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'image_url': image_url,
            'exception_occurred': False,
        })

    except KeyError:
        messages.error(request, "City not found. Showing default Indore weather.")

        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'indore',
            'image_url': image_url,
            'exception_occurred': True,
        })
