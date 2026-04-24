import pandas as pd
import math

FUEL_RANGE = 500  # miles
MPG = 10


def load_fuel_data():
    df = pd.read_csv("fuel_prices.csv")
    return df


def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)


def find_fuel_stops(route_coords, fuel_df):
    stops = []
    total_cost = 0

    step = 80  # approx ~500 miles depending on route density

    for i in range(0, len(route_coords), step):
        lat, lon = route_coords[i][1], route_coords[i][0]

        fuel_df['distance'] = fuel_df.apply(
            lambda row: calculate_distance(lat, lon, row['latitude'], row['longitude']),
            axis=1
        )

        nearest = fuel_df.nsmallest(5, 'distance')
        cheapest = nearest.loc[nearest['price'].idxmin()]

        gallons = FUEL_RANGE / MPG
        cost = gallons * cheapest['price']

        total_cost += cost

        stops.append({
            "city": cheapest['city'],
            "price": cheapest['price'],
            "cost": cost
        })

    return stops, total_cost