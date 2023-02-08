import requests

API = "bfcc2a9de8bbc2b6720138dccf429271"

url_coord = "http://api.openweathermap.org/geo/1.0/direct"

city_name = input("Введите название города ").capitalize()
params_for_coord = {
    "q": city_name,
    "limit": 1,
    "appid": API
}

res_coord = requests.get(url_coord, params=params_for_coord)
lon = res_coord.json()[0]['lon']
lat = res_coord.json()[0]['lat']

url_total_res = "https://api.openweathermap.org/data/2.5/weather"
params_for_total_res = {
    "lat": {lat},
    "lon": {lon},
    "appid": {API},
    "units": "metric"
}

total_res = requests.get(url_total_res, params=params_for_total_res)
data = total_res.json()["main"]
print(f"Температура в городе {city_name} {data['temp']}°C, ощущается как {data['feels_like']}°C ")
