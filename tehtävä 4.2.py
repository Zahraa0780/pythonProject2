import requests
import json

hakusana = input("Anna hakusana: ")
pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&lang=FI&units=metric&appid=52e497241272a80243c2a0c0332b906d"

json_vastaus = requests.get(pyynto).json()
print(json_vastaus["weather"][0]["description"])
Kelvin = json_vastaus["main"]["temp"]

print(Kelvin)