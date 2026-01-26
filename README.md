**📊 HR Analytics & Employee Intelligence**


An end-to-end Machine Learning project that analyzes employee data to generate business insights and predictive models for salary estimation, attrition risk, and department classification.

This project demonstrates how HR data can be transformed into actionable intelligence using regression, classification, and ensemble learning techniques.


**🚀 Project Overview**

This repository builds multiple predictive models using employee data to help HR teams:

      1. Predict Monthly Income (Regression)
      2. Predict Employee Attrition Risk (Classification)
      3. Classify Employee Department (Multi-class Classification)

All models are trained using real-world HR-style features such as job level, experience, satisfaction scores, and compensation data.



**🧠 Models Implemented**

*1️⃣ Monthly Income Prediction*
    
    Type: Linear Regression
    Goal: Estimate an employee’s monthly salary based on experience, job level, and career history.

Key Features Used:
      
      Age
      Job Level
      Total Working Years
      Years at Company
      Years in Current Role
      Number of Companies Worked
      Percent Salary Hike
      Current Employee Status
      

Evaluation Metrics:
     
     MAE (Mean Absolute Error)
     MSE / RMSE
     R² Score
     Adjusted R²
     Model saved as: hr_model.pkl



*2️⃣ Employee Attrition Prediction*
    
    Type: Random Forest Classifier
    Goal: Predict the probability of an employee leaving the company.
    

Key Features Used:
    
    Age
    Monthly Income
    Job Level
    Job Satisfaction
    Environment Satisfaction
    Work Life Balance
    Overtime
    Distance from Home
    Years Since Last Promotion
    Years with Current Manager
    
Evaluation Metrics: 
    
    Accuracy
    Confusion Matrix
    Classification Report
    Attrition Risk Probability Score

Model saved as: attrition_model.pkl


*3️⃣ Department Classification*
    
    Type: Random Forest Classifier
    Goal: Predict which department an employee belongs to based on job and compensation attributes.


Key Features Used:
    
    Age
    Job Level
    Years at Company
    Monthly Income
    Job Satisfaction
    
Evaluation Metric:
    
    Accuracy Score

Model saved as: department_model.pkl


*📈 Exploratory Data Analysis*

A correlation heatmap is generated to understand relationships between numerical variables:

    Identifies strong predictors
    Helps detect multicollinearity
    Guides feature selection


🛠️ Tech Stack

    Python
    Pandas, NumPy – Data processing
    Seaborn, Matplotlib – Visualization
    Scikit-learn – Machine Learning
    Joblib – Model serialization


*▶️ How to Run*

1. Clone the repository
2. Place the dataset CSV file in the project directory
3. Install dependencies:
   
       pip install pandas numpy matplotlib seaborn scikit-learn joblib
   
5. Run the script:

       python hr_analytics.py


The program will:
  
    Train models
    Display performance metrics
    Allow manual input for real-time predictions



💼 Business Use Cases

    ✔ Salary benchmarking
    ✔ Identifying high attrition risk employees
    ✔ Workforce planning & department analysis
    ✔ HR decision support systems

📌 Future Improvements

    Hyperparameter tuning
    Model explainability (SHAP / feature importance dashboards)
    Web app deployment (Streamlit / Flask)
    Automated data pipeline


👨‍💻 Author

Anupam

HR Analytics & Machine Learning Enthusiast
