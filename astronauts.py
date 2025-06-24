import requests
import time
from utils import log_event

def fetch_astronauts():
    url = "http://api.open-notify.org/astros.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        people = data.get("people", [])

        print(f"\n There are {len(people)} people in space right now:\n")
        for person in people:
            print(f"- {person['name']} aboard {person['craft']}")

        with open("data/iss_data.txt", "a") as f:
            f.write(f"\n===Astronauts - {time.ctime()} ===\n")
            for person in people:
                f.write(f"{person['name']} - {person['craft']}\n")

        log_event("Fetched astronauts successfully.")

    except Exception as e:
        log_event(f"Error fetching astronauts: {e}")
        print("❌ Failed to fetch astronaut data.")