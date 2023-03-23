#!/usr/bin/env python3
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get(input("Enter Your Registered API Key: "))

account_sid = input("Enter Your Twilio Account SID: ")
auth_token = os.environ.get(input("Enter Your Twilio Auth Token: "))

TWILIO_TRIAL_NUMBER = input("Enter Your Twilio Trial Number: ")
RECIPIENT_NUMBER =input("Enter Your Twilio Verified Number: ")

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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_= TWILIO_TRIAL_NUMBER,
        to= RECIPIENT_NUMBER        
    )
    print(message.status)
