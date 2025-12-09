import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB





df = pd.read_csv("X:\\Data Science Project\\Hr Analytics\\HR Data.xlsx - HR data.csv")
print(df)
print(df.columns)
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.1f')
plt.show()





# 1 . Predict Monthly Income from Employee Data
print("Predict Monthly Income from Employee Data")

x = df[["Age","CF_current_Employee","Job_Level","Num_Companies_Worked", "Total_Working_Years","Years_At_Company",
        "Years_In_Current_Role", "Percent_Salary_Hike"]]
y = df["Monthly_Income"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(x_train, y_train)
y_pred = model.predict(x_test)

print("R² = ", r2_score(y_test, y_pred))
print("RMSE = ", mean_squared_error(y_test, y_pred))

print("Predict monthly income from employee data")
age  = int(input("Age: "))
job_level = int(input("Job level (1-5): "))
total_working_years  = int(input("Total working years: "))
years_at_company = int(input("Years at company: "))
years_in_current_role = int(input("Years in current role: "))
num_comp = int(input("Num companies worked: "))
hike = int(input("Percent salary hike: "))
current_emp = int(input("Currently employee? (1=Yes,0=No): "))
row = pd.DataFrame([[age, current_emp, job_level, num_comp, total_working_years, years_at_company, years_in_current_role, hike]],
                   columns=x.columns)
pred_income = model.predict(row)[0]
print("Predicted Monthly Income:", round(pred_income, 2))




# 2. Predicting Employee Attrition using K-Nearest Neighbors (KNN)

x = df[["Age","Total_Working_Years","Monthly_Income","Years_At_Company","Job_Satisfaction"]]
y = df["Attrition"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

print("Accuracy = ", accuracy_score(y_test, y_pred))
print("Confusion matrix = ", confusion_matrix(y_test, y_pred))

print("Employee attrition prediction")
age  = int(input("Age: "))
total_working_years  = int(input("Total working years: "))
income = int(input("Monthly income: "))
years_at_company = int(input("Years at company: "))
job_satisfaction = int(input("Job satisfaction (1-4): "))

row = pd.DataFrame([[age, total_working_years, income, years_at_company, job_satisfaction]])

print("Predicted attrition:", knn.predict(row)[0])



#3. Department Classification using Naïve Bayes
x = df[["Age","Job_Level","Years_At_Company","Monthly_Income","Job_Satisfaction"]]
y = df["Department"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
m = RandomForestClassifier(n_estimators=200,random_state=42).fit(x_train,y_train)
y_pred = m.predict(x_test)

print("Accuracy:", accuracy_score(y_test,y_pred))

row = [[int(input("Age = ")),
        int(input("Job level (1-5) = ")),
        int(input("Years at company = ")),
        int(input("Monthly income = ")),
        int(input("Job satisfaction (1-4) = "))]]

print("Predicted Department:", m.predict(row))



