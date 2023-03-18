#!/usr/bin/env python3
import requests
import datetime as dt


PARAMETERS = {
    'lat':-6.175110,
    'lng':106.865036,
    'formatted':0    
}
response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
response.raise_for_status
data = response.json()

sunrise = data['results']['sunrise'].split("T")[-1].split(":")[0]
sunset= data['results']['sunset'].split("T")[-1].split(":")[0]
print(sunrise)
print(sunset)

now = dt.datetime.now().hour
print(now)
