"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

from pyowm import OWM
from pprint import pprint

owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()

while True:
    city = input("input city name:")
    if (not city):
        break
    w = mgr.weather_at_place(city)
    w_dict = w.to_dict()
    # pprint(dir(w.weather))
    print(f"City: {w_dict["location"]["name"]} ({w_dict["location"]["country"]}), temperature: {w.weather.temperature('celsius')["temp"]}")
