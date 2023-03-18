#!/usr/bin/env python3
import requests, datetime as dt, time, smtplib

# Location of Lagos
parameters ={
    'lat': 6.524379,
    'long': 3.379206, 
    'formatted': 0
}

print("Input your credentials! (make sure it's gmail and you have allowed third party application to send emails")
user = input("Insert your email: ")
password = input("Insert your password: ")

def is_close():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    location = response.json()['iss_position']
    latitude = float(location['latitude'])
    longitude = float(location['longitude'])
    if abs(latitude-parameters['lat']) <= 5 and abs(longitude-parameters['long']) <= 5:
        return True
    return False

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
    response.raise_for_status
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[-1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[-1].split(":")[0])
    now = dt.datetime.now().hour

    if now >= sunset or now <= sunrise:
        return True
    return False

def iss_inform():
    if is_close() and is_night():
        with smtplib.SMTP('smtp.gmail.com:587') as connection:
            connection.starttls()
            connection.login(user = user, password = password)
            connection.sendmail(from_addr=user, to_addrs=user, msg = 'Subject: Look Up!!\n\nYou might be able to see the International Space Station\n\nHeads up!!')
    else:
      print("Not even close")

# Supposedly notify every 30 minutes with an email if International Space Station is close (if its not it won't send an email), can just be run on python anywhere with an interval

while True:
    iss_inform()
    time.sleep(60)
