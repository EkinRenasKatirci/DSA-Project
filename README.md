# DSA-Project

## Description

Sabancı University **DSA210: Introduction to Data Science Course** Fall 2024-2025 Term Project.  
This project focuses on analyzing the relationship between my health metrics and academic schedule.  
The goal is to understand how my physical activity, energy expenditure are influenced by lecture days, workloads, and overall university schedule.

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
The data was collected directly from my iPhone using the Apple Health export feature and spans the years 2021 to 2024. It includes metrics such as step count, energy burned, and walking distance. The 2021-2023 data has been filtered to align the analysis with the Fall 2024 academic schedule. [View data in csv format]

### **2. Academic Schedule**:
Collected from my university's management system. It includes:
- **Lecture Days and Times**: Specific days, hours, and locations for each course.
- **Free Days**: Days without scheduled lectures.

---

## Tools

- **[Jupyter Notebook](https://jupyter.org/):**  Used for coding, processing, and documentation.
- **[Pandas](https://pandas.pydata.org/):** For data cleaning, filtering, and structuring.
- **[Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/):** For data visualization in Python.
- **[Numpy](https://numpy.org/):** For mathematical operations.

---

## Data Analysis

The analysis will proceed through the following stages to investigate the relationship between my health metrics and academic schedule:

### **1. Data Collection**
- **Apple Health Data**:
  - Exported from the Health app in XML format.
  - Preprocessed into a structured format (e.g., CSV) to include metrics like steps, calories burned, sleep duration, and timestamps.
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

## Research Question

- How do physical activity levels vary between lecture days and free days?


---
