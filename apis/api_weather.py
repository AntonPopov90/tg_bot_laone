import os
from pathlib import Path
from dotenv import load_dotenv
from pyowm import OWM


env_path = Path("..") / ".env"
load_dotenv(dotenv_path=env_path)
owm_key: str = os.getenv('OWM')
owm = OWM(owm_key)
weather_manager = owm.weather_manager()


def get_weather_by_coordinates(latitude: float, longitude: float) -> dict:
    """Function for finding weather in place with longitude and latitude, if it will be necessary in future"""
    observation = weather_manager.weather_at_coords(latitude, longitude)
    w = observation.weather
    stat = w.detailed_status
    temp = w.temperature('celsius')['temp']
    wind = w.wind()['speed']
    print(stat)
    print('temperature', temp, 'C')
    print('wind', wind, 'm/s')
    result_dict = {'temp': temp, 'wind': wind, 'stat': stat}
    return result_dict


def get_weather_by_place(city: str) -> dict:
    """returns weather forecast in the selected city. It's possible to add another weather information
    e.g. pressure, humidility, clouds etc."""
    observation = weather_manager.weather_at_place(city)
    w = observation.weather
    stat = w.detailed_status
    temp = w.temperature('celsius')['temp']
    wind = w.wind()['speed']
    print(stat)
    print('temperature', temp, 'C')
    print('wind', wind, 'm/s')
    result_dict = {'temp': temp, 'wind': wind, 'stat': stat}
    return result_dict
