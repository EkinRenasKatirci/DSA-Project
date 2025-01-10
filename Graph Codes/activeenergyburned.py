import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File paths
active_energy_data_path = "/Users/ekinrenaskatirci/Desktop/graph/filtered_2024_HKQuantityTypeIdentifierActiveEnergyBurned.txt"
academic_schedule = {
    "Monday": [{"time": "8:40 am-9:30 am"}, {"time": "4:40 pm-5:30 pm"}],
    "Tuesday": [{"time": "10:40 am-12:30 pm"}, {"time": "12:40 pm-2:30 pm"}, {"time": "2:40 pm-3:30 pm"}, {"time": "3:40 pm-4:30 pm"}],
    "Wednesday": [{"time": "8:40 am-10:30 am"}, {"time": "10:40 am-12:30 pm"}],
    "Thursday": [{"time": "10:40 am-12:30 pm"}, {"time": "2:40 pm-3:30 pm"}, {"time": "5:40 pm-6:30 pm"}],
    "Friday": [{"time": "8:40 am-9:30 am"}, {"time": "9:40 am-12:30 pm"}, {"time": "12:40 pm-2:30 pm"}, {"time": "2:40 pm-4:30 pm"}],
    "Saturday": [],
    "Sunday": []
}

# Parse Active Energy Burned data
def parse_active_energy_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            start_date_match = re.search(r'startDate="([^"]+)"', line)
            value_match = re.search(r'value="([\d.]+)"', line)

            if start_date_match and value_match:
                start_date = start_date_match.group(1)
                value = float(value_match.group(1))
                data.append({"startDate": start_date, "activeEnergy": value})
    return pd.DataFrame(data)

# Parse and preprocess active energy data
active_energy_data = parse_active_energy_data(active_energy_data_path)
active_energy_data['startDate'] = pd.to_datetime(active_energy_data['startDate'])
active_energy_data['Day'] = active_energy_data['startDate'].dt.day_name()
active_energy_data['Date'] = active_energy_data['startDate'].dt.date

# Filter data for the specified date range
filtered_active_energy = active_energy_data[
    (active_energy_data['startDate'] >= "2024-09-25") & 
    (active_energy_data['startDate'] <= "2024-11-27")
]

# Define lecture days
lecture_days = [day for day, slots in academic_schedule.items() if slots]
filtered_active_energy['DayType'] = filtered_active_energy['Day'].apply(
    lambda x: "Lecture Day" if x in lecture_days else "Non-Lecture Day"
)

# Calculate average active energy burned by weekdays
avg_active_energy_weekday = filtered_active_energy.groupby('Day')['activeEnergy'].mean().reset_index()

# Reorder weekdays
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
avg_active_energy_weekday['Day'] = pd.Categorical(avg_active_energy_weekday['Day'], categories=days_order, ordered=True)
avg_active_energy_weekday = avg_active_energy_weekday.sort_values('Day')

# Plot average active energy burned by weekdays
plt.figure(figsize=(10, 6))
sns.barplot(x='Day', y='activeEnergy', data=avg_active_energy_weekday, palette="Oranges")
plt.title("Average Active Energy Burned by Weekday (Sep 25 - Nov 27, 2024)", fontsize=16)
plt.xlabel("Weekday", fontsize=12)
plt.ylabel("Average Active Energy Burned (kcal)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Optional: Scatter Plot for Detailed Analysis
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Day', y='activeEnergy', hue='DayType', data=filtered_active_energy, s=50, palette="Set2")
plt.title("Active Energy Burned by Weekday: Lecture vs. Non-Lecture", fontsize=16)
plt.xlabel("Weekday", fontsize=12)
plt.ylabel("Active Energy Burned (kcal)", fontsize=12)
plt.legend(title="Day Type", loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()