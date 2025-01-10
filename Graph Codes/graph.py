import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Path to the folder containing the .txt files
folder_path = "/Users/ekinrenaskatirci/Desktop/graph"

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
            value_match = re.search(r'value="(\d+)"', record)
            start_date_match = re.search(r'startDate="([^"]+)"', record)
            
            if value_match and start_date_match:
                value = int(value_match.group(1))
                start_date = datetime.strptime(start_date_match.group(1), "%Y-%m-%d %H:%M:%S %z")
                data.append({"startDate": start_date, "value": value})
    return data

# Process each file and generate monthly average graphs
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
        # Group data by month and calculate averages
        df['month'] = df['startDate'].dt.to_period('M')
        monthly_avg = df.groupby('month')['value'].mean()
        
        # Plot the data
        plt.figure()
        monthly_avg.plot(kind='bar')
        plt.title(f"Monthly Average for {txt_file}")
        plt.xlabel("Month")
        plt.ylabel("Average Value")
        plt.xticks(rotation=45)
        
        # Save the plot as an image in the same folder
        plot_path = os.path.join(folder_path, f"{os.path.splitext(txt_file)[0]}_monthly_avg.png")
        plt.tight_layout()
        plt.savefig(plot_path)
        plt.close()  # Close the figure to save memory
        
        print(f"Graph saved for {txt_file} at {plot_path}")
    
    except Exception as e:
        print(f"Error processing {txt_file}: {e}")