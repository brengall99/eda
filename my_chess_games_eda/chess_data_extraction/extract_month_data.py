import json
import requests
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

with open('archives.json', 'r') as f:
    data = json.loads(f.read())

# Ensure the output directory exists
output_dir = "chess_game_data"
os.makedirs(output_dir, exist_ok=True)

for archive_url in data["archives"]:
    response = requests.get(archive_url, headers=headers)
    
    if response.status_code == 200:
        archive_data = response.json()
        
        # Extract the year and month from the URL for the file name
        year_month = archive_url.split("/")[-2:]
        file_name = f"{year_month[0]}-{year_month[1]}.json"
        file_path = os.path.join(output_dir, file_name)
        
        # Save the archive data to a file
        with open(file_path, "w") as json_file:
            json.dump(archive_data, json_file, indent=4)
        print(f"Saved data to {file_path}")
    else:
        print(f"Failed to fetch data from {archive_url}. HTTP Status Code: {response.status_code}")