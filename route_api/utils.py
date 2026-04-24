import requests
import os
from django.conf import settings

ORS_API_KEY = settings.ORS_API_KEY


def get_coordinates(city):
    url = f"https://api.openrouteservice.org/geocode/search?api_key={ORS_API_KEY}&text={city}"
    res = requests.get(url).json()
    coords = res['features'][0]['geometry']['coordinates']
    return coords  # [lng, lat]


def get_route(start, end):
    url = "https://api.openrouteservice.org/v2/directions/driving-car/geojson"

    body = {
        "coordinates": [start, end]
    }

    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }

    res = requests.post(url, json=body, headers=headers)
    return res.json()