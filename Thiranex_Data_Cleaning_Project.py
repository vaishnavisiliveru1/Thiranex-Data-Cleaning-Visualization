import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/Users/pc/Downloads/Sleep_health_and_lifestyle_dataset (1).csv")
print("Data shape =", df.shape)
print(df.head())

# Handle missing values
for col in df.columns:
    if df[col].dtype in ['int64','float64']:
        df[col].fillna(df[col].mean(), inplace=True)   
    else:
        df[col].fillna(df[col].mode()[0], inplace=True) 

# Remove duplicates
df.drop_duplicates(inplace=True)

# Outlier removal function (replace with NaN instead of dropping rows)
def remove_outlier(data, col):
    if data[col].dtype in ['int64','float64']:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        # Replace outliers with NaN
        data.loc[(data[col] < lower) | (data[col] > upper), col] = None
    return data

# Apply outlier removal and fill with median
for col in df.select_dtypes(include=['int64','float64']).columns:
    df = remove_outlier(df, col)
    df[col].fillna(df[col].median(), inplace=True)

# Dashboard Visualization
fig, axes = plt.subplots(2, 2, figsize=(14,10))

# Plot 1: Sleep Duration Histogram
sns.histplot(df["Sleep Duration"], bins=20, kde=True, ax=axes[0,0], color="skyblue")
axes[0,0].set_title("Distribution of Sleep Duration")

# Plot 2: Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Reds", ax=axes[0,1])
axes[0,1].set_title("Correlation Heatmap")

# Plot 3: Boxplot of Numeric Columns
df.select_dtypes(include=['int64','float64']).boxplot(ax=axes[1,0])
axes[1,0].set_title("Box Plot of Numeric Columns")
for label in axes[1,0].get_xticklabels():
    label.set_rotation(45)

# Plot 4: Sleep Disorder Count
sns.countplot(x="Sleep Disorder", data=df, ax=axes[1,1], palette="Set2")
axes[1,1].set_xlabel("Sleep Disorder")
axes[1,1].set_ylabel("Count")
axes[1,1].set_title("Distribution of Sleep Disorders")

plt.tight_layout()
plt.show()

# Save cleaned dataset
df.to_csv("C:/Users/pc/Downloads/cleaned_sleep_dataset.csv", index=False)
print("Processed dataset saved as cleaned_sleep_dataset.csv")
