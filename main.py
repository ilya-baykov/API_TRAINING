import requests


API = "bfcc2a9de8bbc2b6720138dccf429271"

city_name = input("Введите название города ")
coordinates = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API}"
res_coord = requests.get(coordinates)
lon = res_coord.json()[0]['lon']
lat = res_coord.json()[0]['lat']
total_res = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric")
data = total_res.json()["main"]
print(f"Температура в городе {city_name} {data['temp']}°C, ощущается как {data['feels_like']}°C ")
