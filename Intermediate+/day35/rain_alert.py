#!/usr/bin/env python3
import requests
import os
from twilio.rest import Client


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

TWILIO_TRIAL_NUMBER = os.environ.get("TWILIO_TRIAL_NUMBER")
RECIPIENT_NUMBER = os.environ.get("RECIPIENT_NUMBER")

weather_parameters = {
    "lat": 6.524379,
    "lon": 3.379206, 
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_endpoint, weather_parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

will_rain = False
for data in hourly_data:
    condition_code = data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_= TWILIO_TRIAL_NUMBER,
        to= RECIPIENT_NUMBER        
    )
    print(message.status)
