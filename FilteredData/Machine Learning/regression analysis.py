import pandas as pd
import xml.etree.ElementTree as ET
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import json

# 1. Parse Health Data
def parse_health_data(xml_path):
    with open(xml_path, 'r') as file:
        raw_data = file.read()
    # Add a root element to make the XML valid
    wrapped_data = f"<HealthData>{raw_data}</HealthData>"
    root = ET.fromstring(wrapped_data)

    # Extract relevant data from each record
    records = []
    for record in root.findall("Record"):
        records.append({
            "start_date": record.get("startDate"),
            "end_date": record.get("endDate"),
            "value": int(record.get("value"))
        })
    health_data = pd.DataFrame(records)
    health_data['start_date'] = pd.to_datetime(health_data['start_date'])
    health_data['end_date'] = pd.to_datetime(health_data['end_date'])
    health_data['day'] = health_data['start_date'].dt.day_name()
    return health_data

# 2. Academic Schedule Data
def parse_academic_schedule(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    flattened_data = []
    for day, classes in data.items():
        for course in classes:
            flattened_data.append({
                "day": day,
                "course": course["course"],
                "time": course["time"],
                "location": course["location"]
            })
    academic_data = pd.DataFrame(flattened_data)

    # Calculate total class hours
    def calculate_hours(time_range):
        start, end = time_range.split('-')
        start_hour = int(start.split(':')[0]) + (12 if 'pm' in start and '12' not in start else 0)
        end_hour = int(end.split(':')[0]) + (12 if 'pm' in end and '12' not in end else 0)
        return end_hour - start_hour

    academic_data['class_hours'] = academic_data['time'].apply(calculate_hours)
    daily_class_hours = academic_data.groupby('day')['class_hours'].sum().reset_index()
    daily_class_hours.rename(columns={'class_hours': 'total_class_hours'}, inplace=True)
    daily_class_hours['lecture_day'] = daily_class_hours['total_class_hours'].apply(lambda x: 1 if x > 0 else 0)
    return daily_class_hours

# 3. Merge Data
def merge_data(health_data, academic_data):
    merged_data = health_data.merge(academic_data, on='day', how='left')
    merged_data.fillna({'total_class_hours': 0, 'lecture_day': 0}, inplace=True)
    return merged_data

# 4. Perform Regression Analysis
def regression_analysis(merged_data):
    X = merged_data[['lecture_day', 'total_class_hours']]
    y = merged_data['value']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluate model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Mean Squared Error:", mse)
    print("R^2 Score:", r2)

    # Analyze coefficients
    coefficients = pd.DataFrame(model.coef_, index=['lecture_day', 'total_class_hours'], columns=['Coefficient'])
    print("\nCoefficients:\n", coefficients)

    # Visualizations
    visualize_results(y_test, y_pred, merged_data)

# 5. Visualizations
def visualize_results(y_test, y_pred, merged_data):
    # Scatter plot with trend line
    plt.figure(figsize=(10, 6))
    sns.regplot(x=y_test, y=y_pred, line_kws={"color": "red", "lw": 2}, scatter_kws={"alpha": 0.6})
    plt.xlabel("Actual Step Count")
    plt.ylabel("Predicted Step Count")
    plt.title("Actual vs Predicted Step Count with Trend Line")
    plt.show()

    # Residuals plot
    residuals = y_test - y_pred
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True, bins=30, color='blue', alpha=0.7)
    plt.axvline(0, color='red', linestyle='--', lw=2)
    plt.xlabel("Residuals (Actual - Predicted)")
    plt.title("Distribution of Residuals")
    plt.show()

    # Residuals vs Total Class Hours
    merged_data_test = merged_data.iloc[y_test.index]  # Match index of test set
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=merged_data_test['total_class_hours'], y=residuals, hue=merged_data_test['lecture_day'], palette="coolwarm", alpha=0.7)
    plt.axhline(0, color='red', linestyle='--', lw=2)
    plt.xlabel("Total Class Hours")
    plt.ylabel("Residuals (Actual - Predicted)")
    plt.title("Residuals vs Total Class Hours")
    plt.legend(title="Lecture Day")
    plt.show()

# Paths to the files
health_data_path = '/Users/ekinrenaskatirci/Desktop/graph/filtered_2024_HKQuantityTypeIdentifierStepCount.txt'
academic_schedule_path = '/Users/ekinrenaskatirci/Desktop/graph/final_revised_schedule.json'

# Execute the process
health_data = parse_health_data(health_data_path)
academic_data = parse_academic_schedule(academic_schedule_path)
merged_data = merge_data(health_data, academic_data)
regression_analysis(merged_data)
