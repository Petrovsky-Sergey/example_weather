from django.shortcuts import render
import requests


def index(request):
    appid = '9168126ab4661d1056c642fcc0606e45'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'London'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }
    context = {'info': city_info}
    return render(request, 'weather/index.html', context)
