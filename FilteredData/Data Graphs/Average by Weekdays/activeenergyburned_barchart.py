import re
import pandas as pd
import matplotlib.pyplot as plt

# File path
file_path = '/Users/ekinrenaskatirci/Desktop/graph/filtered_2024_HKQuantityTypeIdentifierActiveEnergyBurned.txt'

# Read the file line by line
with open(file_path, 'r') as file:
    lines = file.readlines()

# Extract data using regular expressions
data = []
for line in lines:
    match = re.search(r'startDate="(.*?)".*?value="(.*?)"', line)
    if match:
        start_date = match.group(1)
        value = float(match.group(2))
        data.append((start_date, value))

# Create a DataFrame
df = pd.DataFrame(data, columns=['Date', 'Value'])

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter data between 25 September and 27 November
df_filtered = df[(df['Date'] >= '2024-09-25') & (df['Date'] <= '2024-11-27')]

# Extract weekday names
df_filtered['Weekday'] = df_filtered['Date'].dt.day_name()

# Group by weekdays and calculate the average value
weekday_avg = df_filtered.groupby('Weekday')['Value'].mean()

# Reorder weekdays (to ensure proper order in the chart)
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_avg = weekday_avg.reindex(weekday_order)

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(weekday_avg.index, weekday_avg.values)
plt.xlabel('Weekday')
plt.ylabel('Average Value (kcal)')
plt.title('Average Active Energy Burned by Weekday (25 September - 27 November)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
