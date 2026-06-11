# Thiranex-Data-Cleaning-Visualization
Thiranex Internship Assignment – Data Cleaning & Visualization Project
#  Sleep Health & Lifestyle Analysis

##  Project Overview
This project analyzes a dataset on **sleep health and lifestyle factors**.  
The goal is to clean the data, handle missing values and outliers, and generate meaningful visual reports that highlight correlations between lifestyle habits and sleep disorders.

---

##  Dataset
**File:** `Sleep_health_and_lifestyle_dataset.csv`  
**Features include:**
- Demographics: Person ID, Gender, Age, Occupation  
- Health Metrics: Sleep Duration, Quality of Sleep, Stress Level, BMI Category, Blood Pressure, Heart Rate  
- Lifestyle Metrics: Physical Activity Level, Daily Steps  
- Sleep Disorders: Insomnia, Sleep Apnea, None  

---

##  Steps Performed
1. **Data Loading** – Import dataset using Pandas  
2. **Data Cleaning**  
   - Fill missing values (median/mode)  
   - Remove duplicates  
   - Handle outliers (IQR method)  
3. **Plots visualized**  
   - Histograms for sleep duration distribution  
   - Correlation heatmap of numeric features  
   - Boxplots for stress level and numeric columns  
   - Count plots for sleep disorders  
4. **Dashboard Visualization** – Multiple plots arranged in a single figure 
5. **Export Results** – Save cleaned dataset as `cleaned_sleep_dataset.csv`

---

##  Visual Report Findings
- **Sleep Duration:**  
  Most individuals sleep between **6–8 hours**, with fewer cases below 6 hours or above 8.5 hours.  

- **Correlation Heatmap:**  
  - Sleep Duration ↔ Quality of Sleep: strong positive correlation (**0.88**)  
  - Stress Level ↔ Quality of Sleep: strong negative correlation (**-0.9**)  
  - Daily Steps ↔ Physical Activity Level: positive correlation (**0.77**)  
  - Age ↔ Person ID: highly correlated (**0.99**)  

- **Box Plot of Numeric Columns:**  
  - Daily Steps has the widest range (up to ~10,000).  
  - Stress Level shows clear outliers.  
  - Other metrics (Sleep Duration, Heart Rate, Quality of Sleep) are more compact.  

- **Sleep Disorder Distribution:**  
  - Sleep Apnea cases are significantly higher (~300) compared to Insomnia (~75).  
  - Sleep Apnea is more prevalent in the dataset, while Insomnia is less frequent.  
---


##  Outcome
- Cleaned dataset ready for ML modeling  
- Professional dashboard visualizations for quick insights   

---

##  How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/vaishnavisiliveru1/Thiranex-Data-Cleaning-Visualization

2.pip install pandas matplotlib seaborn

3.Run the Script
python Thiranex_Data_Cleaning_Project.py
