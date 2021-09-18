import json
from secret import ACCESS_KEY
import requests


def parse_weather_codes(filepath):
    weather_codes = {}
    with open(filepath, encoding='utf-8') as file:
        for line in file.readlines():
            temp = line.strip().split()
            if temp[0][0].isdigit():
                weather_codes[int(temp[0])] = temp[1]
    return weather_codes


def get_weather(city):
    url = ("http://api.weatherstack.com/current?access_key=" + ACCESS_KEY + "&query=" + city).replace(" ", "%20")
    response = requests.get(url)
    return json.loads(response.text)


class BadRequestException(Exception):
    pass


def parse_weather(info, weather_codes):
    try:
        if not info['success']:
            raise BadRequestException("No success")
    except KeyError:
        result = f"Location: {info['request']['query']}\n" \
                 f"Current time: {info['location']['localtime']}\n" \
                 f"Temperature: {info['current']['temperature']}°C\n" \
                 f"Weather: {weather_codes[int(info['current']['weather_code'])]}\n" \
                 f"Wind speed and direction: {info['current']['wind_speed']} {info['current']['wind_dir']}\n"
        return result
