import config
import requests
import json

api_key = config.api_key
city_name = input()
response = requests.request('GET', f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
output = response.json()
a = json.dumps(output)
print(a)
