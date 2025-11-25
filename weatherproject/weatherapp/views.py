from django.shortcuts import render, redirect
import requests
import datetime

def home(request):

    if request.method == "POST":
        city = request.POST.get('city')
    else:
        city = "Bangalore"

    API_KEY = "5b6a9e5227f8afbbf5a2c3a03de2b1bb"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    
    if response.status_code != 200:
        context = {"error": "City not found", "city": city}
        return render(request, "weatherapp/home.html", context)

    data = response.json()

    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    icon = data["weather"][0]["icon"]
    day = datetime.datetime.today()
    
    context = {
        "day": day,
        "description": description,
        "temp": temp,
        "icon": icon,
    }

    return render(request, "weatherapp/home.html", context)
