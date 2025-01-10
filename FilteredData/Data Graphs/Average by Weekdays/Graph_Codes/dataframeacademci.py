import pandas as pd
import json

# Load the JSON file
academic_schedule_path = '/Users/ekinrenaskatirci/Desktop/graph/final_revised_schedule.json'

with open(academic_schedule_path, 'r') as file:
    data = json.load(file)

# Transform the JSON data into a flat list
flattened_data = []

for day, classes in data.items():
    for course in classes:
        flattened_data.append({
            "day": day,
            "course": course["course"],
            "class": course["class"],
            "time": course["time"],
            "location": course["location"]
        })

# Create a DataFrame
academic_data = pd.DataFrame(flattened_data)

# Preview the DataFrame
print(academic_data.head())