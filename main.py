import requests
from datetime import *
import os

APP_ID = os.environ["YOUR_APP_ID"]
API_KEY = os.environ["YOUR_API_KEY"]
NUTRIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["YOUR_SHEETY_API_ENDPOINT"] 

# EXAMPLE ENDPOINTS:
# https://api.sheety.co/4bb3a7097948d0ad5e777b0275476ho/workoutTracking/workouts
# Ran 2 miles and walked 3km

parameters = {
    "query": input("Tell me which exercises you did?")
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutrionix_response = requests.post(url=NUTRIONIX_ENDPOINT, json=parameters, headers=header)
nutrionix_response.raise_for_status()

for i in range(0, len(nutrionix_response.json()['exercises'])):
    duration = nutrionix_response.json()['exercises'][i]['duration_min']
    exercise = nutrionix_response.json()['exercises'][i]['name'].title()
    calories = nutrionix_response.json()['exercises'][i]['nf_calories']
    date = datetime.now().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")

    res_params = {
      "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
        "id": i + 3

      }
    }

    res_header = {
        "Authorization": f"Basic {os.environ['d2F5bmVhcnVsOlN1a3VuYWlkYXRvck=']}",
        "Content-Type": "application/json"
    }

    response = requests.post(url=SHEET_ENDPOINT, json=res_params, headers=res_header)
    response.raise_for_status()
    print(response.json())
