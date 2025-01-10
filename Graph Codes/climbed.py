import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# File paths
flights_data_path = "/Users/ekinrenaskatirci/Desktop/graph/filtered_2024_HKQuantityTypeIdentifierFlightsClimbed.txt"
academic_schedule_path = "/Users/ekinrenaskatirci/Desktop/graph/final_revised_schedule.json"

# Load academic schedule from JSON
with open(academic_schedule_path, 'r') as f:
    academic_schedule = json.load(f)

# Parse Flights Climbed data
def parse_flights_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            start_date_match = re.search(r'startDate="([^"]+)"', line)
            value_match = re.search(r'value="([\d.]+)"', line)

            if start_date_match and value_match:
                start_date = start_date_match.group(1)
                value = float(value_match.group(1))
                data.append({"startDate": start_date, "flights": value})
    return pd.DataFrame(data)

# Parse and preprocess flights climbed data
flights_data = parse_flights_data(flights_data_path)
flights_data['startDate'] = pd.to_datetime(flights_data['startDate'])
flights_data['Day'] = flights_data['startDate'].dt.day_name()
flights_data['Date'] = flights_data['startDate'].dt.date
flights_data['Hour'] = flights_data['startDate'].dt.hour

# Filter data for the specified date range
filtered_flights = flights_data[
    (flights_data['startDate'] >= "2024-09-25") & 
    (flights_data['startDate'] <= "2024-11-27")
]

# Focus on hours between 8:00 and 19:00
filtered_flights = filtered_flights[(filtered_flights['Hour'] >= 8) & (filtered_flights['Hour'] <= 19)]

# Extract lecture days from the academic schedule JSON
lecture_days = {day: [slot['time'] for slot in slots] for day, slots in academic_schedule.items() if slots}
filtered_flights['DayType'] = filtered_flights['Day'].apply(
    lambda x: "Lecture Day" if x in lecture_days else "Non-Lecture Day"
)

# Box Plot
plt.figure(figsize=(14, 8))
sns.boxplot(
    data=filtered_flights,
    x='Hour',
    y='flights',
    hue='DayType',
    palette="Set3"
)
plt.title("Flights Climbed by Hour: Box Plot", fontsize=16)
plt.xlabel("Hour of the Day", fontsize=12)
plt.ylabel("Flights Climbed", fontsize=12)
plt.legend(title="Day Type", loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()