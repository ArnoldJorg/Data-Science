# -*- coding: utf-8 -*-

import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
city_name = os.getenv("CITY_NAME")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

# Make API request
response = requests.get(url)
data = response.json()

# Print the response
print(data)
