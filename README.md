#DSA-Project

##Description

Sabancı University DSA210 Introduction to Data Science Course Fall 2024-2025 Term Project. This project focuses on analyzing the relationship between my health metrics and academic schedule. The goal is to understand how my physical activity, and energy expenditure are influenced by lecture days, workloads, and overall university schedule.

##Motivation

While brainstorming for this project, I realized that I could explore the connection between my health habits and my academic routine. As a student, my daily routine is heavily shaped by lecture times, class durations.

The motivation behind this analysis is to uncover patterns such as:

• How my physical activity levels vary on lecture days versus non-lecture days.

• Whether certain class times correlate with increased or decreased activity levels.

• To explore how academic schedules impact overall health, helping to identify patterns that might inform healthier routines.

##Data Source

Apple Health Data:

Collected directly from my iPhone via the Apple Health export feature for the year 2024. Contains the following metrics:

• Steps: Total daily steps.

• Calories Burned: Active energy expenditure.

Academic Schedule:

Collected from my university's management system. It contains details such as course names, time slots, and class locations. Includes:

• Lecture Days and Times: Specific days and hours for each course.

• Free Days: Days without any scheduled lectures.

##Tools

Jupyter Notebook: Used for coding, processing, and documentation.
Pandas: For data cleaning, filtering, and structuring.
Matplotlib and Seaborn: For data visualization in python.
Numpy: For mathematical operations.
##Data Analysis

The analysis will proceed through the following stages to investigate the relationship between my health metrics and my academic schedule:

###Data Collection

Apple Health Data:

Exported from the Health app in XML format and preprocessed into a structured format (e.g., CSV).Includes:

• Steps and calories burned with timestamps.

Academic Schedule Data:

Manually organized into a JSON file containing:

• Course names, time slots, lecture locations.

###Data Cleaning

• Removed incomplete or erroneous entries (e.g., missing health data or incomplete lecture details).

• Standardized timestamps to align both data sources.

• Categorized lecture days and non-lecture days.

###Exploratory Data Analysis (EDA)

Objective: Determine the relationship between health metrics and academic schedule.

Daily Patterns:

• Analyzing activity levels on lecture days versus free days.

• Exploring peak activity times during lecture hours and between classes.

Activity Trends:

• Investigating step counts before, during, and after lectures.

• Comparing total calories burned on high-workload days versus low
