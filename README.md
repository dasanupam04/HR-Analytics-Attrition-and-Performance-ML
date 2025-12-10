# HR-Analytics-Attrition-and-Performance-ML
This project uses HR employee data to explore workforce patterns and build predictive machine-learning models for salary estimation, attrition risk detection, and department classification.


It includes:

    🔍 Exploratory Data Analysis (EDA)
    🤖 Machine Learning Models (Regression, KNN, Random Forest)
    📈 Interactive Predictions using user input


📊 Exploratory Data Analysis (EDA)

A deep EDA was performed to understand employee demographics, satisfaction, income distribution, and attrition trends.

    📌 1.1 Data Distributions
    1. Histograms of all numeric features
    2. Understanding age, income, experience, job involvement, satisfaction, etc

    📌 1.2 Attrition Distribution
    1. Count plot showing employees who left vs stayed
    2. Helps detect class imbalance

    📌 1.3 Attrition by Department
    1. Shows which departments face the most attrition
    2. Useful for HR decision-making

    📈 1.4 Key Statistical Insights
    | Insight                                     | Description        | ------------------------------------------- | --------------------------------- |
    | **Mean Age**                                | Average age of workforce          |
    | **Median Monthly Income**                   | Central salary value              |
    | **Age ↔ Monthly Income Correlation**        | Do older employees earn more?     |
    | **Experience ↔ Monthly Income Correlation** | Income increases with experience  |
    | **Overall Attrition Rate**                  | % of employees who quit           |
    | **Income by Gender**                        | Male vs Female salary comparison  |
    | **Age by Department**                       | Which teams are younger/older     |
    | **Income by Job Level**                     | Salary structure by job hierarchy |

    

📉 1.5 Visual HR Insights

Income and Growth
      
      Bar chart showing Average Monthly Income by Job Level
      Regression plot showing Working Years vs Income

Attrition Behavior
     
     Violin + box plot of Monthly Income vs Attrition
     Attrition rate by Job Role
     Attrition rate by Work-Life Balance
     Attrition rate by Job Satisfaction


Heatmap
    
    A full correlation heatmap reveals:
    Strong predictors of income
    Factors impacting attrition
    Relationships between satisfaction, experience, and job level
    This EDA forms the foundation for selecting features for ML models.



🤖 2. Machine Learning Models

Three ML models were implemented to solve different HR problems:


🟦 2.1 Monthly Income Prediction (Linear Regression)

Goal: Predict an employee’s monthly income based on:
    
    Age
    Job level
    Job experience
    Salary hike percentage
    Number of companies worked
    Current employee status

Outputs:
    
    R² Score
    RMSE
    Predicted monthly income from user inputs
