import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("X:\\Data Science Project\\Hr Analytics\\HR Data.xlsx - HR data.csv")
print(df.head(5))
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())


df.hist(figsize=(15,10))
plt.show()

plt.figure(figsize=(5,4))
sns.countplot(x='Attrition', data=df)
plt.show()


plt.figure(figsize=(8,4))
sns.countplot(x='Department', hue='Attrition', data=df)
plt.show()


#mean age of employeee
mean_age = np.mean(df['Age'])
print("1.  Mean age of employee:", round(mean_age, 2))

#Median monthly income
median_income = np.median(df['Monthly_Income'])
print("2. Median monthly income: ", round(median_income, 2))

#correlation btw Age and monthly income
correlation_age_income = np.corrcoef(df['Age'], df['Monthly_Income'])[0, 1]
print("3. Correlation (Age vs Monthly income):", round(correlation_age_income, 3))

#correlation btw Monthly income and total working years
corr_years_income = np.corrcoef(df['Total_Working_Years'], df['Monthly_Income'])[0, 1]
print("4. Correlation (Total working years vs Monthly income):", round(corr_years_income, 3))

#Attrition Rate
attrition_rate = (df['Attrition'] == 'Yes').mean() * 100
print("5. attrition rate :", attrition_rate)

#Average monthly oincome by gender
avg_income_by_gender = df.groupby('Gender')['Monthly_Income'].mean()
print("6. average monthly income by gender",  avg_income_by_gender)

#Average age by department
avg_age_by_department = df.groupby('Department')['Age'].mean()
print("7. average age by department ", avg_age_by_department)

#Average monthly income by job level
income_vs_job_level = df.groupby('Job_Level')['Monthly_Income'].mean()
print("8. Average Monthly Income by Job Level ", income_vs_job_level )


# Average Monthly Income by Job Level (Bar Chart)
plt.figure(figsize=(7,4))
sns.barplot(data=df, x='Job_Level', y='Monthly_Income', ci=95)
plt.ylabel("Average Monthly Income")
plt.title("Average Monthly Income by Job Level (Bar Chart)")
plt.tight_layout()
plt.show()


#Monthly Income Distribution by Attrition (Violin + Box Plot)
plt.figure(figsize=(8,5))
sns.violinplot(data=df, x='Attrition', y='Monthly_Income', inner='box')
plt.title("Monthly Income by Attrition (Violin + Box Plot)")
plt.tight_layout()
plt.show()


# Attrition Rate by Job Role (Bar Chart)
role_attr = df.groupby('Job_Role')['Attrition'].apply(lambda x: (x=='Yes').mean()*100)
role_attr = role_attr.sort_values(ascending=False)

plt.figure(figsize=(11,5))
sns.barplot(x=role_attr.index, y=role_attr.values)
plt.xticks(rotation=45, ha='right')
plt.ylabel("Attrition Rate (%)")
plt.title("Attrition Rate by Job Role (Bar Chart)")
plt.tight_layout()
plt.show()


# Relationship btw Experience and income
plt.figure(figsize=(8,6))
sns.regplot(data=df, x='Total_Working_Years', y='Monthly_Income', scatter_kws={'alpha':0.5})
plt.title("Total Working Years vs Monthly Income (Regression Plot)")
plt.tight_layout()
plt.show()


# Work-Life Balance vs Attrition (Bar Chart)
wlb_attr = df.groupby('Work_Life_Balance')['Attrition'].apply(lambda x: (x=='Yes').mean()*100)
plt.figure(figsize=(9,5))
sns.barplot(x=wlb_attr.index, y=wlb_attr.values)
plt.ylabel("Attrition Rate (%)")
plt.title("Work-Life Balance vs Attrition (Bar Chart)")
plt.tight_layout()
plt.show()

#Job Satisfaction vs Attrition (Bar Chart)
plt.figure(figsize=(9,6))
satis = pd.crosstab(df['Job_Satisfaction'], df['Attrition'])
satis.plot(kind='bar', figsize=(9,6))
plt.ylabel("Count")
plt.title("Job Satisfaction vs Attrition (Bar Chart)")
plt.tight_layout()
plt.show()


#Correlation Matrix (Heatmap)
num = df.select_dtypes(include=[np.number])
corr = num.corr()
plt.figure(figsize=(12,9))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Matrix (Full Heatmap)")
plt.tight_layout()
plt.show()











