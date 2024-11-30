# DSA-Project
## Description
Sabancı University DSA210 Introduction to Data Science Course Fall 2024-2025 Term Project. This project focuses on analyzing my personal health data collected via Apple Health.
## Motivation
As a university student, my daily routine is heavily influenced by my academic schedule.
This project aims to understand:
	
 •	How my physical activity levels vary on lecture days versus non-lecture days.
	
 •	Whether certain class times correlate with increased or decreased activity levels.
 
 • 	To explore how academic schedules impact overall health, helping to identify patterns that might inform healthier routines.
## Data Source
Apple Health Data:

Collected directly from my iPhone via the Apple Health export feature for the year 2024.
Contains the following metrics:
	
 •	Steps: Total daily steps.

 •	Calories Burned: Active energy expenditure.

Academic Schedule:

Manually created based on my semester course timetable.
Includes:
	
 •	Lecture Days and Times: Specific days and hours for each course.
	
 •	Free Days: Days without any scheduled lectures.
 ## Tools
 - **[Jupyter Notebook](https://jupyter.org/):** Used for coding, processing, and documentation.
 - **[Pandas](https://pandas.pydata.org/):** For data cleaning, filtering, and structuring.
 - **[Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/):** For data visualization in python.
 - **[Numpy](https://numpy.org/):** For mathematical operations.
## Data Analysis
The analysis will proceed through the following stages to investigate the relationship between my health metrics and my academic schedule:
### Data Collection
•	Apple Health Data:
Exported from the Health app in XML format and preprocessed into a structured format (e.g., CSV).
Includes:
	•	Steps and calories burned with timestamps.
	•	Academic Schedule Data:
Manually organized into a JSON file containing:
	•	Course names, time slots, lecture locations, and key exam dates.
 ### Data Cleaning

•	Removed incomplete or erroneous entries (e.g., missing health data or incomplete lecture details).
•	Standardized timestamps to align both data sources.
•	Categorized lecture days and non-lecture days.
### Exploratory Data Analysis (EDA)

Objective:
Determine the relationship between health metrics and academic schedule.
•	Daily Patterns:
•	Analyzing activity levels on lecture days versus free days.
•	Exploring peak activity times during lecture hours and between classes.
•	Sleep Analysis:
•	Examining sleep patterns during exam weeks compared to regular weeks.
•	Identifying the impact of late-night study sessions on sleep quality.
•	Activity Trends:
•	Investigating step counts before, during, and after lectures.
•	Comparing total calories burned on high-workload days versus low-workload days.
