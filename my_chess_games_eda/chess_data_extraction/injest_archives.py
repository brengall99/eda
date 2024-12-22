
import requests
import json

# URL containing the data
url = "https://api.chess.com/pub/player/brengall99/games/archives"

# Add headers (User-Agent is often required)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Fetch the data from the URL
response = requests.get(url, headers=headers)

if response.status_code == 200:  # Ensure the request was successful
    data = response.json()  # Parse the JSON response

    # Save the data to a local JSON file
    with open("archives.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Data has been successfully written to archives.json.")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")