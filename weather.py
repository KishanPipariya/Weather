import config
import requests
import json


class Api:

    def __init__(self, api_key):
        self.api_key = api_key

    def current_weather(self, *args):
        if len(args) == 1:
            response = requests.request('GET', f'https://api.openweathermap.org/data/2.5/weather?q={args[0]}&appid={self.api_key}')
            output = response.json()
            out = json.dumps(output)
            print(out)
        else:
            response = requests.request('GET', f'https://api.openweathermap.org/data/2.5/weather?lat={args[0]}&lon={args[1]}&appid={self.api_key}')
            output = response.json()
            out = json.dumps(output)
            print(out)


api = Api(config.api_key)
api.current_weather('rajkot')
api.current_weather('22.3039', '70.8022')
