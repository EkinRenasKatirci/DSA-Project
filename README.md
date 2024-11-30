# DSA-Project: Exploring the Relationship Between Health Metrics and Academic Schedule

---

## Description
This project is part of Sabancı University’s **DSA210: Introduction to Data Science Course (Fall 2024-2025 Term)**. The focus is on analyzing the relationship between my health metrics and academic schedule. By integrating personal health data with my university's lecture schedule, I aim to uncover patterns that reveal how physical activity and energy expenditure are influenced by academic demands.

---

## Motivation
During the brainstorming phase, I realized my daily routine is largely shaped by my academic schedule. This inspired me to explore how my health is impacted by lecture days, workloads, and free days. 

**Key Questions Driving My Motivation:**
- How does my physical activity vary on lecture days compared to non-lecture days?
- Do specific class times correlate with changes in my activity levels or calorie expenditure?
- Can insights from this analysis help me design healthier routines that align with my academic responsibilities?

By answering these questions, this project aims to inform better habits for balancing academic and personal well-being.

---

## Data Source
### 1. **Apple Health Data:**
Collected from my iPhone using the Apple Health export feature. The dataset spans the year 2024 and includes:
- **Steps:** Total daily step counts.
- **Calories Burned:** Active energy expenditure.

### 2. **Academic Schedule:**
Data manually curated from my university’s management system. It contains:
- **Lecture Days and Times:** Specific days, hours, and locations for each course.
- **Free Days:** Days without scheduled lectures.

---

## Tools
- **Jupyter Notebook:** For coding, processing, and documentation.
- **Pandas:** For data cleaning, filtering, and structuring.
- **Matplotlib and Seaborn:** For visualizing patterns and trends.
- **Numpy:** For performing mathematical operations.

---

## Data Analysis
The analysis is structured into the following phases to explore the connection between academic schedules and health metrics:

### 1. **Data Collection**
- Apple Health Data:
  - Exported from the Health app in XML format.
  - Preprocessed into a structured format (e.g., CSV) to extract metrics like steps and calories burned, along with timestamps.
- Academic Schedule Data:
  - Manually organized into a JSON file, including course names, time slots, and lecture locations.

### 2. **Data Cleaning**
- Removed incomplete or erroneous entries (e.g., missing timestamps or incomplete lecture details).
- Standardized timestamps to align Apple Health data and academic schedule data.
- Categorized days into **lecture days** and **non-lecture days**.

### 3. **Exploratory Data Analysis (EDA)**
#### Objectives:
- **Daily Patterns:**
  - Compare activity levels on lecture days vs. free days.
  - Analyze peak activity times during and between lectures.
- **Activity Trends:**
  - Investigate changes in step counts before, during, and after lectures.
  - Examine calorie expenditure on high-workload vs. low-workload days.

---

## Research Questions
This project investigates the following questions to uncover actionable insights:

1. **How does physical activity (steps) vary between lecture and non-lecture days?**
2. **Are certain time slots (e.g., morning vs. afternoon lectures) associated with higher or lower activity levels?**
3. **How does class duration impact calorie expenditure during the day?**
4. **Do free days exhibit consistent patterns of increased physical activity compared to lecture days?**
5. **What is the relationship between lecture locations (e.g., proximity of classrooms) and step counts?**
6. **Are there any correlations between the intensity of the academic workload and calorie expenditure?**
7. **Can specific patterns in activity metrics predict high-stress academic days?**
8. **What insights can be derived to balance academic performance and health metrics effectively?**

---

## Future Work
- **Automated Insights:** Integrate machine learning algorithms to predict high-energy expenditure days based on schedule data.
- **Visualization:** Develop interactive dashboards to display activity patterns.
- **Broader Data Integration:** Include additional health metrics like sleep quality and heart rate for a more holistic analysis.

---

## Conclusion
This project bridges the gap between academic and personal health by uncovering meaningful patterns in health metrics influenced by university schedules. The insights can inform better routines for students aiming to optimize their academic performance while maintaining a healthy lifestyle.
