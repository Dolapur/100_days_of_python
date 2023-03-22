#!/usr/bin/env python3
import requests


parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"    
}
response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
