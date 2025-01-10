import os
import re
import pandas as pd
import matplotlib.pyplot as plt

# File path for step data
file_path = os.path.expanduser("~/Desktop/graph/filtered_2024_HKQuantityTypeIdentifierStepCount.txt")

# Read the step data from the file
with open(file_path, "r", encoding="utf-8") as file:
    step_data_raw = file.read()

# Extract step data using regex
records = re.findall(
    r'<Record.*?startDate="(.*?)".*?value="(.*?)"/>',
    step_data_raw,
)

# Create DataFrame
step_data = pd.DataFrame(records, columns=["startDate", "value"])
step_data["startDate"] = pd.to_datetime(step_data["startDate"])
step_data["value"] = step_data["value"].astype(int)

# Aggregate steps by weekday and calculate average
step_data["Weekday"] = step_data["startDate"].dt.day_name()
average_steps_by_weekday = step_data.groupby("Weekday")["value"].mean()

# Ensure consistent ordering of weekdays
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
average_steps_by_weekday = average_steps_by_weekday.reindex(days_order, fill_value=0)

# Academic schedule (manually provided)
academic_schedule = {
    "Monday": [
        {"course": "CS 204-B", "class": "12534", "time": "8:40 am-9:30 am", "location": "UC G030"},
        {"course": "MATH 306R-H", "class": "10929", "time": "4:40 pm-5:30 pm", "location": "FENS L065"}
    ],
    "Tuesday": [
        {"course": "DSA 210R-B", "class": "12658", "time": "10:40 am-12:30 pm", "location": "FENS G035"},
        {"course": "HUM 201-0", "class": "10660", "time": "12:40 pm-2:30 pm", "location": "FASS G062"},
        {"course": "MATH 204-0", "class": "10902", "time": "2:40 pm-3:30 pm", "location": "FENS G077"},
        {"course": "DSA 210-A", "class": "12655", "time": "3:40 pm-4:30 pm", "location": "FASS G062"}
    ],
    "Wednesday": [
        {"course": "MATH 306-0", "class": "10917", "time": "8:40 am-10:30 am", "location": "FENS G077"},
        {"course": "CS 204-B", "class": "12534", "time": "10:40 am-12:30 pm", "location": "UC G030"}
    ],
    "Thursday": [
        {"course": "MATH 204-0", "class": "10902", "time": "10:40 am-12:30 pm", "location": "FENS G077"},
        {"course": "HUM 201D-C", "class": "10667", "time": "2:40 pm-3:30 pm", "location": "FASS G049"},
        {"course": "MATH 204R-A1", "class": "10904", "time": "5:40 pm-6:30 pm", "location": "FASS 1096"}
    ],
    "Friday": [
        {"course": "MATH 306-0", "class": "10917", "time": "8:40 am-9:30 am", "location": "FENS G077"},
        {"course": "PSY 201-0", "class": "10970", "time": "9:40 am-12:30 pm", "location": "FENS G077"},
        {"course": "DSA 210-A", "class": "12655", "time": "12:40 pm-2:30 pm", "location": "FASS G062"},
        {"course": "CS 204L-C1", "class": "10226", "time": "2:40 pm-4:30 pm", "location": "FENS L029"}
    ],
    "Saturday": [],
    "Sunday": []
}

# Calculate number of classes per weekday
number_of_classes_by_weekday = {day: len(classes) for day, classes in academic_schedule.items()}
number_of_classes_by_weekday = pd.Series(number_of_classes_by_weekday).reindex(days_order, fill_value=0)

# Visualization
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot average steps on the first y-axis
ax1.plot(average_steps_by_weekday.index, average_steps_by_weekday.values, label="Average Steps", color="red", marker="o", linestyle="-")
ax1.set_ylabel("Average Steps", color="red")
ax1.tick_params(axis="y", labelcolor="red")

# Create a second y-axis for number of classes
ax2 = ax1.twinx()
ax2.plot(number_of_classes_by_weekday.index, number_of_classes_by_weekday.values, label="Number of Classes", color="blue", marker="s", linestyle="--")
ax2.set_ylabel("Number of Classes", color="blue")
ax2.tick_params(axis="y", labelcolor="blue")

# Title and grid
plt.title("Average Weekdays: Classes vs Average Steps")
plt.grid(alpha=0.3)

# Add legend
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

# Save and show the plot
plt.tight_layout()
plt.savefig("steps_vs_classes_dual_axis.png")
plt.show()
