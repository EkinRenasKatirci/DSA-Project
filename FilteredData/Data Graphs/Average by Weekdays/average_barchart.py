import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone, timedelta

# Path to the folder containing the .txt files
folder_path = "/Users/ekinrenaskatirci/Desktop/graph"

# Define the date range with timezone-awareness
timezone_offset = timezone(timedelta(hours=3))  # UTC+3
start_date = datetime(2024, 9, 25, tzinfo=timezone_offset)
end_date = datetime(2024, 11, 26, tzinfo=timezone_offset)

# Get all .txt files in the folder
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Function to parse records and extract data
def parse_records(file_path):
    data = []
    with open(file_path, 'r') as file:
        content = file.read()
        # Regex to extract each <Record> tag and its attributes
        records = re.findall(r'<Record[^>]+>', content)
        for record in records:
            # Extract relevant attributes using regex
            value_match = re.search(r'value="(\d+(\.\d+)?)"', record)
            start_date_match = re.search(r'startDate="([^"]+)"', record)
            
            if value_match and start_date_match:
                value = float(value_match.group(1))
                # Parse the start date and make it timezone-aware
                start_date = datetime.strptime(start_date_match.group(1), "%Y-%m-%d %H:%M:%S %z")
                data.append({"startDate": start_date, "value": value})
    return data

# Process each file and calculate average for weekdays in the date range
for txt_file in txt_files:
    file_path = os.path.join(folder_path, txt_file)
    try:
        # Parse the data from the file
        records = parse_records(file_path)
        if not records:
            print(f"No valid records found in {txt_file}")
            continue
        
        # Create a DataFrame
        df = pd.DataFrame(records)
        # Filter the data for the specified date range
        df = df[(df['startDate'] >= start_date) & (df['startDate'] <= end_date)]
        if df.empty:
            print(f"No data found in the specified date range for {txt_file}")
            continue
        
        # Add a column for weekdays
        df['weekday'] = df['startDate'].dt.strftime('%A')  # Get weekday names
        weekday_avg = df.groupby('weekday')['value'].mean()

        # Sort weekdays in standard order and fill missing weekdays
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_avg = weekday_avg.reindex(weekday_order, fill_value=0)  # Fill missing weekdays with 0

        # Plot the data as a bar chart
        plt.figure(figsize=(10, 6))
        weekday_avg.plot(kind='bar', color='skyblue')
        plt.title(f"Average Weekdays (25 Sep - 27 Nov) for {txt_file}")
        plt.xlabel("Weekday")
        plt.ylabel("Average Value")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the plot as an image in the same folder
        plot_path = os.path.join(folder_path, f"{os.path.splitext(txt_file)[0]}_weekday_avg_filtered_bar.png")
        plt.savefig(plot_path)
        plt.close()  # Close the figure to save memory
        
        print(f"Bar chart saved for {txt_file} at {plot_path}")
    
    except Exception as e:
        print(f"Error processing {txt_file}: {e}")
