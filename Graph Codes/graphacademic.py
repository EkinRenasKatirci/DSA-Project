import json
import matplotlib.pyplot as plt
import pandas as pd

# Path to your academic schedule JSON file
academic_schedule_path = '/Users/ekinrenaskatirci/Desktop/graph/final_revised_schedule.json'

# Function to parse academic schedule and calculate total class hours per day
def parse_academic_schedule(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    
    total_class_hours = {}
    for day, classes in data.items():
        total_hours = 0
        for cls in classes:
            time = cls['time']
            start_time, end_time = time.split('-')
            start_hour, start_minute = map(int, start_time[:-3].split(':'))
            end_hour, end_minute = map(int, end_time[:-3].split(':'))

            # Convert time to 24-hour format for PM times
            if 'pm' in start_time and start_hour != 12:
                start_hour += 12
            if 'pm' in end_time and end_hour != 12:
                end_hour += 12
            
            # Calculate class duration in hours
            class_duration = (end_hour + end_minute / 60) - (start_hour + start_minute / 60)
            total_hours += class_duration

        total_class_hours[day] = total_hours

    return total_class_hours

# Parse the academic schedule
total_class_hours = parse_academic_schedule(academic_schedule_path)

# Create a DataFrame for better visualization
schedule_df = pd.DataFrame(list(total_class_hours.items()), columns=['Day', 'Total Class Hours'])

# Plotting the schedule
plt.figure(figsize=(10, 6))
plt.bar(schedule_df['Day'], schedule_df['Total Class Hours'], color='skyblue', edgecolor='black')
plt.title('Total Class Hours per Day', fontsize=16)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Total Class Hours', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the graph as an image
output_path = '/Users/ekinrenaskatirci/Desktop/graph/academic_schedule_graph.png'
plt.savefig(output_path)

# Show the plot
plt.show()