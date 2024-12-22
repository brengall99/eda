import json
import csv
import os

# Function to generate the list of JSON filenames
def generate_json_filenames(start_year, start_month, end_year, end_month):
    filenames = []
    year, month = start_year, start_month
    while year < end_year or (year == end_year and month <= end_month):
        filenames.append(f"chess_game_data/{year}-{str(month).zfill(2)}.json")
        month += 1
        if month > 12:
            month = 1
            year += 1
    return filenames

# Function to convert JSON data to CSV and append it to the CSV file
def json_to_csv(json_files, csv_filename):
    # Check if CSV file exists to determine if we need headers
    file_exists = os.path.exists(csv_filename)
    
    # Open the CSV file in append mode
    with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # If file doesn't exist, write headers
        if not file_exists:
            headers = ["url", "pgn", "time_control", "end_time", "rated", "white_username", "white_rating", 
                       "white_result", "black_username", "black_rating", "black_result", "eco"]
            writer.writerow(headers)
        
        # Process each JSON file
        for json_file in json_files:
            if os.path.exists(json_file):  # Check if file exists before processing
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Extract the relevant data from the JSON
                    for game in data['games']:
                        row = [
                            game['url'],
                            game['pgn'],
                            game['time_control'],
                            game['end_time'],
                            game['rated'],
                            game['white']['username'],
                            game['white']['rating'],
                            game['white']['result'],
                            game['black']['username'],
                            game['black']['rating'],
                            game['black']['result'],
                            game['eco']
                        ]
                        # Write the row to CSV
                        writer.writerow(row)

# Example usage:
# Define the start and end year/month
start_year, start_month = 2017, 12
end_year, end_month = 2024, 12  # Adjust this as needed

# Generate the list of JSON filenames
json_files = generate_json_filenames(start_year, start_month, end_year, end_month)

# Specify the CSV filename
csv_filename = 'chess_games.csv'

# Convert and append to CSV
json_to_csv(json_files, csv_filename)
