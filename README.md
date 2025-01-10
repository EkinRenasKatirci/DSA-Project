# DSA-Project

## Description

Sabancı University **DSA210: Introduction to Data Science Course** Fall 2024-2025 Term Project.  
This project focuses on analyzing the relationship between my health metrics and academic schedule.  
The goal is to understand how my physical activity, energy expenditure are influenced by lecture days, workloads, and overall university schedule.

For the final report see [here](./DSA-210%20Report.pdf).    
For a detailed analysis of the hypothesis, research questions, and visualizations, please check the [website](https://ekin-renas-katirci-dsa-210.netlify.app) I prepared for this project.
---

## Motivation

While brainstorming for this project, I realized that I could explore the connection between my health habits and my academic routine. As a student, my daily routine is heavily shaped by lecture times and class durations.

The motivation behind this analysis is to uncover patterns such as:
- **How my physical activity levels vary on lecture days versus non-lecture days.**
- **Whether certain class times correlate with increased or decreased activity levels.**
- **How academic schedules impact overall health, helping to identify patterns that might inform healthier routines.**

---

## Data Source

### **1. Apple Health Data**:
The data was collected directly from my iPhone using the Apple Health export feature and spans the years 2021 to 2024. It includes metrics such as step count, energy burned, and walking distance. The 2021-2023 data has been filtered to align the analysis with the Fall 2024 academic schedule. [View data in csv format](./FilteredData)

### **2. Academic Schedule**:
Collected from my university's management system. It includes:
- **Lecture Days and Times**: Specific days, hours, and locations for each course.
- **Free Days**: Days without scheduled lectures.[View data in .json format](./FilteredData/final_revised_schedule.json)
### **3. Graphs**: 
The graphs were filtered to show the average weekdays between 25 September and 27 November and have been saved in the folder named "Average by Weekdays"  [View data on graphs](./FilteredData/Data%20Graphs/Average%20by%20Weekdays)
### **4. Graph Generating Code**:
The graph-generating code has been filtered to include data between 25 September and 27 November. The results, in both bar chart and line chart formats, have been saved in the directory: [View the python code for deriving graphs.](./FilteredData/Graph%20Codes)


---

## Tools

- **[Jupyter Notebook](https://jupyter.org/):**  Used for coding, processing, and documentation.
- **[Pandas](https://pandas.pydata.org/):** For data cleaning, filtering, and structuring.
- **[Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/):** For data visualization in Python.
- **[Numpy](https://numpy.org/):** For mathematical operations.
- **[scikit-learn](https://scikit-learn.org/):** For machine learning tasks, including Linear Regression model training and performance evaluation.

---

## Data Analysis

The analysis will proceed through the following stages to investigate the relationship between my health metrics and academic schedule:

### **1. Data Collection**
- **Apple Health Data**:
  - Exported from the Health app in XML format.
  - Preprocessed into a structured format (e.g., CSV) to include metrics like steps, calories burned and timestamps.
- **Academic Schedule Data**:
  - Manually organized into a JSON file containing course names, time slots, and lecture locations.

### **2. Data Cleaning**
- Removed incomplete or erroneous entries (e.g., missing health data or incomplete lecture details).
- Standardized timestamps to align Apple Health data and academic schedule data.
- Categorized days into **lecture days** and **non-lecture days**.

### **3. Exploratory Data Analysis (EDA)**

**Objective:** Determine the relationship between health metrics and academic schedule.  
#### **Daily Patterns**:
- Analyzing activity levels on lecture days versus free days.
- Exploring peak activity times during lecture hours and between classes.

#### **Activity Trends**:
- Investigating step counts before, during, and after lectures.
- Comparing total calories burned on high-workload days versus low-workload days.
---
## Machine Learning

### **Overview**
This technique applies **Linear Regression**, a supervised machine learning algorithm, to analyze how academic schedules influence physical activity. The goal is to predict step counts based on academic workload and understand patterns in physical activity.
For the regression analysis python code see [here](./FilteredData/Machine%20Learning/regression%20analysis.py)


### **Objectives**
- Predict step counts using:
  - **Lecture Day**: Whether it is a lecture day (1) or not (0).
  - **Total Class Hours**: Total number of class hours in a day.
- Evaluate the model using **Mean Squared Error (MSE)** and **R² Score**.
- Identify factors affecting step counts during the academic term.


## Machine Learning Workflow

### **1. Data Preprocessing**
- Merged health data (step counts) with academic schedule data.
- Extracted features:
  - `lecture_day`: Binary feature for lecture days.
  - `total_class_hours`: Numeric feature for daily class hours.

### **2. Model Selection**
- I Chose **Linear Regression** for its simplicity in predicting continuous variables.

### **3. Model Training and Testing**
- Split data into **training (80%)** and **testing (20%)** sets.
- Trained the model on training data and evaluated its performance on testing data.

### **4. Evaluation Metrics**
- **Mean Squared Error (MSE)**: 111,769.17 (high error, suggesting limitations in the model's performance).
- **R² Score**: -0.0007 (indicates the model does not explain the variance in step counts).


### **Results**
- **Coefficients**:
  - `lecture_day`: -10.27 (lecture days slightly decrease step counts).
  - `total_class_hours`: +2.68 (each additional class hour slightly increases step counts).
- The model struggled to accurately predict step counts due to limited features and noisy data.


### **Visualization**
For the regression analysis graph see [here](./FilteredData/Machine%20Learning/Figure_21.png)
- **Actual vs Predicted Step Counts**: Shows alignment between predictions and actual values, with a trend line.
- **Residual Distribution**: Visualizes the errors in predictions.
- **Residuals vs Total Class Hours**: Explores the relationship between errors and academic workload.

---

## Research Question

- How do physical activity levels vary between lecture days and free days?


---
## Findings
### **1. Steps and Physical Activity**:
- Academic schedules influence activity, with lecture-heavy days increasing steps and non-lecture days showing variable movement.
- Weekends demonstrate a steady increase in physical activity, likely tied to recreational or leisure activities.
### **2. Active Energy Burned**:
- Structured lecture days provide a baseline of activity, while non-lecture days allow for higher energy output through leisure or sports.
### **3. Flights Climbed**:
- Lecture days encourage moderate but consistent stair activity, often tied to class transitions.
- Non-lecture days exhibit spontaneous, intense activity peaks, reflecting unstructured movement.
---
## Limitations
### **1. Limited Data Scope**:
- The project uses data from a short time period (September-November 2024). A full academic year could show seasonal trends.
### **2.Single-User Data**:
- The analysis is based on one person’s data, making it less generalizable. Including more participants would improve reliability.
### **3. Missing Influencing Factors**:
- External factors like weather or mood were not included but might affect physical activity.
---
## Future Directions
### **1. Enhanced Physical Activity During Lecture Days**
- Incorporate walking or light exercise between classes to increase movement and reduce sedentary behavior during academic hours.
### **2. Leverage Weekends for Physical Engagement**
- Students can utilize weekends for more diverse and intensive activities to maintain a balanced routine.
### **3. Further Analysis of Activity Patterns**
- Explore correlations between academic workload and physical activity over a broader timeline.
- Examine how weather or external factors influence these trends to develop more tailored strategies for maintaining health and well-being during university life.
---
