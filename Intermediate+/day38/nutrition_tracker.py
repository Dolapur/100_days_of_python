#!/usr/bin/env python3
import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["APP_KEY"]
GENDER = "female"
AGE = 25
WEIGHT_KG= 45
HEIGHT_CM = 169

exercise_text = input("Tell me which exercises you did: ")

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "age": AGE,
    "weight": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
}

response = requests.post(nutri_endpoint, json=parameters, headers=HEADERS)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]        
        }
        
    }
    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    #print(sheet_response.text)

    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        auth=(
            os.environ["USERNAME"], 
            os.environ["PASSWORD"],      
        )
    )
    #print(sheet_response.text)

    #Bearer Token
    bearer_headers = {"Authorization": f"Bearer {os.environ['TOKEN']}"}
    sheet_response = requests.post(    
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers   
    )    
    print(sheet_response.text)
