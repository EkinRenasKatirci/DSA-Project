import os
from lxml import etree
from datetime import datetime

# Define input and output paths
input_file = "/Users/ekinrenaskatirci/Desktop/apple_health_export/data.xml"
output_folder = "/Users/ekinrenaskatirci/Desktop/FilteredData"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Parse the XML file
with open(input_file, 'r', encoding='utf-8') as file:
    tree = etree.parse(file)
    root = tree.getroot()

# Dictionary to store categorized records
categories = {}

# Filter records from 2024 and categorize by "type"
for record in root.findall(".//Record"):
    start_date_str = record.get("startDate")
    record_type = record.get("type")  # Extract the "type" attribute
    if start_date_str and record_type:
        try:
            # Extract and parse the date
            start_date = datetime.strptime(start_date_str.split()[0], "%Y-%m-%d")
            if start_date.year == 2024:
                # Add the record to the appropriate category
                if record_type not in categories:
                    categories[record_type] = []
                categories[record_type].append(etree.tostring(record, pretty_print=True).decode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")

# Write each category to a separate file
for category, records in categories.items():
    output_file = os.path.join(output_folder, f"filtered_2024_{category}.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(records)
    print(f"Filtered data for category '{category}' saved to: {output_file}")

print("All records have been processed successfully!")