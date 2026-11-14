"""
Using an API an Example with Open Meteo - written by Joe Manlove

created 11/14/2026
"""

import requests

# set the url and parameters to use in our request
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 37.36,
    "longitude": -118.40,
    "current": "temperature_2m"
}

# send a request to open meteo's api and get a response
response = requests.get(url, params=params)

# This is an an analogy to make our request a bit more clear.
# You can think about a request/response as a food order.
# order -> request
# restaurant -> server
# delivery -> response
# food -> response content
# receipt/bag -> response headers and status code

print(f"Request resulted in a status code of: {response.status_code}")

data = response.json()
current_conditions = data["current"]


print(f"The current temperature in Bishop is: {current_conditions["temperature_2m"]}{data["current_units"]["temperature_2m"]}.")