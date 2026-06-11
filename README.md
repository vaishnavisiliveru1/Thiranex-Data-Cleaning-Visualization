# Thiranex-Data-Cleaning-Visualization
Thiranex Internship Assignment – Data Cleaning &amp; Visualization Project
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
  Most individuals sleep between **6–8 hours**, with fewer cases below 6 hours or above 8.5 hours. The distribution is fairly normal, suggesting that short sleep (<6 hours) may be linked to stress or lifestyle imbalance.

- **Correlation Heatmap:**  
  - **Sleep Duration ↔ Quality of Sleep** shows a strong positive correlation (**0.89**).  
  - **Stress Level ↔ Quality of Sleep** has a strong negative correlation (**-0.91**), confirming that higher stress reduces sleep quality.  
  - **Daily Steps ↔ Physical Activity Level** are strongly correlated (**0.82**).  
  - **Age ↔ Person ID** is highly correlated (**0.99**) — expected since IDs are sequential.

- **Box Plot of Numeric Columns:**  
  - **Daily Steps** has the widest range (up to ~10,000), showing high variability in physical activity.  
  - **Stress Level** displays clear outliers, indicating individuals with unusually high or low stress compared to the majority.  
  - Other metrics (Sleep Duration, Heart Rate, Quality of Sleep) are more compact but still show spread.

- **Sleep Disorder Distribution:**  
  - **Insomnia** and **Sleep Apnea** appear in nearly equal counts (~70 each).  
  - This balanced distribution suggests both disorders are common in the dataset.  
  - These conditions are often linked to obesity, high stress, and poor sleep quality.

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
