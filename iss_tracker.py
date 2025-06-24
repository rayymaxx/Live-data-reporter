import requests
import time
from utils import log_event

def track_iss():
    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        position  = data["iss_position"]

        latitude = position["latitude"]
        longitude = position["longitude"]

        print(f"\n ISS Current Location:\nLatitude: {latitude}, \nLongitude: {longitude}")

        with open("data/iss_data.txt", "a") as f:
            f.write(f"\n=== ISS Location - {time.ctime()} ===\n")
            f.write(f"Latitude: {latitude}, Longitude: {longitude}\n")

        log_event("Fetched ISS position successfully.")

    except Exception as e:
        log_event(f"Error fetching ISS position: {e}")
        print("❌ Failed to fetch ISS position.")