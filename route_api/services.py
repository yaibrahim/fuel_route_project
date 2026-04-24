import pandas as pd
import math

FUEL_RANGE = 500  # miles
MPG = 10


def load_fuel_data():
    df = pd.read_csv("fuel_prices.csv")
    return df


def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)