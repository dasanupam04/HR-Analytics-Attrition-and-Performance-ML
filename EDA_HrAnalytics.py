import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("X:\\Data Science Project\\Hr Analytics\\HR Data.xlsx - HR data.csv")
print(df)

df.isnull().sum()
df = df.dropna()
print(df)

#MEAN AGE OF EMPLOYEE
mean_age = np.mean(df['Age'])
print("1. Mean Age of Employees:", round(mean_age, 2))

#MEDIAN MONTHLY INCOME
median_income = np.median(df['Monthly_Income'])
print("2. Median Monthly Income:", round(median_income, 2))

#STANDARD DIAVIATION OF DISTANCE FROM HOME
std_distance = np.std(df['Distance_From_Home'])
print("3. Standard Deviation of Distance from Home:", round(std_distance, 2))

#CORRELATION BTW AGE AND MONTHLY INCOME
corr_age_income = np.corrcoef(df['Age'], df['Monthly_Income'])[0, 1]
print("4. Correlation (Age vs Monthly Income):", round(corr_age_income, 3))

#CORRELATION BTW TOTAL WORKING YEARS AND MONTHLY INCOME
corr_years_income = np.corrcoef(df['Total_Working_Years'], df['Monthly_Income'])[0, 1]
print("5. Correlation (Total Working Years vs Monthly Income):", round(corr_years_income, 3))

#Attrition Rate
attrition_rate = (df['Attrition'].value_counts(normalize=True).get('Yes', 0)) * 100
print("6. Attrition Rate: {:.2f}%".format(attrition_rate))

#Average Monthly Income by Gender
avg_income_by_gender = df.groupby('Gender')['Monthly_Income'].mean()
print("7. Average Monthly Income by Gender:\n", avg_income_by_gender)

#Average Age by Department
avg_age_by_department = df.groupby('Department')['Age'].mean()
print("8. Average Age by Department:\n", avg_age_by_department)

#Average Monthly Income by Job Level
income_vs_job_level = df.groupby('Job_Level')['Monthly_Income'].mean()
print("9. Average Monthly Income by Job Level:\n", income_vs_job_level)

#Average Work-Life Balance by Marital Status
avg_wlb_by_marital = df.groupby('Marital_Status')['Work_Life_Balance'].mean()
print("10. Average Work-Life Balance by Marital Status:\n", avg_wlb_by_marital)


# 1 Seaborn countplot: Attrition by Over_Time
plt.figure(figsize=(8,5))
sns.countplot(x='Over_Time', hue='Attrition', data=df)
plt.title('Attrition by Over Time')
plt.xlabel('Over Time')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 2 Matplotlib histogram: Monthly Income distribution
plt.figure(figsize=(8,5))
plt.hist(df['Monthly_Income'], bins=30)
plt.title('Monthly Income Distribution')
plt.xlabel('Monthly Income')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 3 Seaborn boxplot: Monthly Income by Job Level
plt.figure(figsize=(8,5))
sns.boxplot(x='Job_Level', y='Monthly_Income', data=df)
plt.title('Monthly Income by Job Level')
plt.xlabel('Job Level')
plt.ylabel('Monthly Income')
plt.tight_layout()
plt.show()

# 4 Seaborn heatmap: Correlation of numerical features
plt.figure(figsize=(12,10))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Heatmap (numerical features)')
plt.tight_layout()
plt.show()

# 5 Seaborn scatter: Age vs Monthly Income colored by Attrition
plt.figure(figsize=(8,5))
sns.scatterplot(x='Age', y='Monthly_Income', hue='Attrition', data=df, alpha=0.7)
plt.title('Age vs Monthly Income (colored by Attrition)')
plt.xlabel('Age')
plt.ylabel('Monthly Income')
plt.tight_layout()
plt.show()

# 6 Seaborn barplot: Average Monthly Income by Department
plt.figure(figsize=(10,5))
dept_income = df.groupby('Department')['Monthly_Income'].mean().reset_index().sort_values('Monthly_Income', ascending=False)
sns.barplot(x='Department', y='Monthly_Income', data=dept_income)
plt.title('Average Monthly Income by Department')
plt.xlabel('Department')
plt.ylabel('Average Monthly Income')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7 Matplotlib bar: Attrition rate by Job Role (percent)
attr_by_role = df.groupby('Job_Role')['Attrition'].apply(lambda x: (x=='Yes').mean()*100).reset_index().sort_values('Attrition', ascending=False)
plt.figure(figsize=(12,6))
plt.bar(attr_by_role['Job_Role'], attr_by_role['Attrition'])
plt.title('Attrition Rate (%) by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Attrition Rate (%)')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()



