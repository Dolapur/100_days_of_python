#!/usr/bin/env python3
import requests
import os
from datetime import datetime


USERNAME = "dolapur"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"
pixela_url = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(pixela_url, json=parameters)
print(response.text)

graph_url = f"{pixela_url}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}
response = requests.post(graph_url, json=graph_params, headers=headers)
print(response.text)


pixel_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Enter number of commits for today: "),
}
response = requests.post(pixel_url, json=pixel_params, headers=headers)
print(response.text)


