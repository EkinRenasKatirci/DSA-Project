import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import json
from datetime import datetime, timedelta

# Function to generate date mapping for the academic schedule
def generate_date_mapping(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    date_mapping = {}
    current_date = start_date
    
    while current_date <= end_date:
        weekday = current_date.strftime("%A")
        if weekday not in date_mapping:
            date_mapping[weekday] = []
        date_mapping[weekday].append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    
    return date_mapping

# Function to parse academic schedule with date mapping
def parse_academic_schedule(json_path, date_mapping):
    with open(json_path, 'r') as file:
        data = json.load(file)
    
    schedule_data = []
    for weekday, classes in data.items():
        if weekday in date_mapping:
            for date in date_mapping[weekday]:
                total_hours = sum(
                    [1 for _ in classes]  # Assuming each class contributes 1 hour
                )
                schedule_data.append({
                    "date": date,
                    "total_class_hours": total_hours,
                    "lecture_day": 1 if total_hours > 0 else 0
                })
    return pd.DataFrame(schedule_data)

# Function to parse step count data with error handling
def parse_step_count(file_path):
    step_data = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for record in root.findall('Record'):
            step_data.append({
                "date": record.get("startDate")[:10],  # Extract the date part
                "step_count": int(record.get("value"))
            })
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        print("Attempting to use regex as a fallback...")
        step_data = parse_step_count_with_regex(file_path)  # Fallback method
    return pd.DataFrame(step_data)

# Fallback: Parse step count data with regex
def parse_step_count_with_regex(file_path):
    import re
    step_data = []
    with open(file_path, 'r') as file:
        content = file.read()
        records = re.findall(r'<Record.*?startDate="(.*?)".*?value="(.*?)"/>', content)
        for record in records:
            date, value = record
            step_data.append({
                "date": date[:10],
                "step_count": int(value)
            })
    return pd.DataFrame(step_data)

# Function to filter data by date range
def filter_data_by_date(dataframe, start_date, end_date):
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    return dataframe[(dataframe['date'] >= start_date) & (dataframe['date'] <= end_date)]

# Paths to your data
academic_schedule_path = "/Users/ekinrenaskatirci/Desktop/graph/final_revised_schedule.json"
step_count_path = "/Users/ekinrenaskatirci/Desktop/graph/filtered_2024_HKQuantityTypeIdentifierStepCount.txt"

# Generate date mapping
start_date = "2024-09-25"
end_date = "2024-11-27"
date_mapping = generate_date_mapping(start_date, end_date)

# Parse the datasets
academic_schedule = parse_academic_schedule(academic_schedule_path, date_mapping)
step_count = parse_step_count(step_count_path)

# Debugging: Check the filtered data
print("Filtered Academic Schedule Data:")
print(academic_schedule.head())
print("\nFiltered Step Count Data:")
print(step_count.head())

# Merge the datasets on the date column
merged_data = pd.merge(academic_schedule, step_count, on="date", how="inner")

# Debugging: Check the merged data
print("\nMerged Data:")
print(merged_data.head())
print(merged_data.info())

# Ensure the merged dataset is not empty
if merged_data.empty:
    print("Error: No overlapping data between academic schedule and step count in the specified date range.")
else:
    # Compute the correlation matrix
    correlation_matrix = merged_data[["total_class_hours", "lecture_day", "step_count"]].corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        cbar_kws={"label": "Correlation Coefficient"},
        linewidths=0.5
    )
    plt.title("Correlation Between Academic Workload and Step Count (25 Sep - 27 Nov)")
    plt.tight_layout()
    plt.show()

    # Create a scatter plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=merged_data,
        x="total_class_hours",
        y="step_count",
        hue="lecture_day",
        palette="coolwarm",
        alpha=0.7
    )
    plt.title("Step Count vs Total Class Hours (25 Sep - 27 Nov)")
    plt.xlabel("Total Class Hours")
    plt.ylabel("Step Count")
    plt.legend(title="Lecture Day", loc="upper right")
    plt.tight_layout()
    plt.show()