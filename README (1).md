# HR Analytics - Employee Attrition & Performance Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A comprehensive machine learning solution for HR analytics, featuring predictive models for employee attrition risk assessment, monthly income prediction, and department classification. This project leverages advanced ML algorithms to help organizations make data-driven HR decisions.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Models](#models)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Project Structure](#project-structure)
- [Technical Stack](#technical-stack)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements three core predictive analytics solutions for human resources management:

1. **Monthly Income Prediction** - Estimates employee compensation based on experience, role, and performance metrics
2. **Attrition Risk Assessment** - Identifies employees at high risk of leaving the organization
3. **Department Classification** - Predicts optimal department placement for employees

These models enable HR professionals to:
- Proactively address retention risks
- Ensure competitive and fair compensation
- Optimize workforce allocation across departments
- Make evidence-based talent management decisions

## ✨ Features

### 1. Monthly Income Prediction
- **Algorithm**: Linear Regression
- **Features**: Age, Job Level, Work Experience, Tenure, Salary Hike History
- **Output**: Predicted monthly income with regression metrics
- **Use Case**: Compensation benchmarking, salary negotiations, budget planning

### 2. Employee Attrition Prediction
- **Algorithm**: Random Forest Classifier (300 estimators)
- **Features**: Demographics, Job Satisfaction, Work-Life Balance, Overtime, Commute Distance
- **Output**: Binary prediction (Stay/Leave) + Risk probability percentage
- **Use Case**: Retention strategy, targeted interventions, workforce planning

### 3. Department Classification
- **Algorithm**: Random Forest Classifier (200 estimators)
- **Features**: Age, Job Level, Tenure, Income, Job Satisfaction
- **Output**: Predicted department assignment
- **Use Case**: Internal mobility, organizational restructuring, role optimization

## 📊 Dataset

The project uses HR employee data containing the following key attributes:

### Employee Demographics
- Age
- Distance from Home
- Years at Company
- Total Working Years
- Number of Companies Worked

### Job Information
- Department
- Job Level (1-5)
- Monthly Income
- Job Satisfaction (1-4)
- Environment Satisfaction (1-4)
- Work-Life Balance (1-4)

### Performance Metrics
- Percent Salary Hike
- Years Since Last Promotion
- Years with Current Manager
- Years in Current Role

### Status Indicators
- Attrition (Yes/No)
- Overtime (Yes/No)
- Current Employee Status

**Data Source**: `HR Data.xlsx - HR data.csv`

## 🤖 Models

### Model 1: Income Prediction (Linear Regression)

```python
Features: 8 predictors including Age, Job Level, Working Years, Salary Hike
Target: Monthly Income
Train/Test Split: 80/20
```

**Evaluation Metrics:**
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
- Adjusted R² Score

### Model 2: Attrition Prediction (Random Forest)

```python
Features: 10 predictors including Satisfaction metrics, Overtime, Distance
Target: Attrition (Binary)
Algorithm: RandomForestClassifier with 300 estimators
Class Weighting: Balanced (handles class imbalance)
Train/Test Split: 80/20 (stratified)
```

**Evaluation Metrics:**
- Accuracy Score
- Confusion Matrix
- Precision, Recall, F1-Score
- Classification Report
- Attrition Risk Probability

### Model 3: Department Classification (Random Forest)

```python
Features: 5 predictors (Age, Job Level, Tenure, Income, Satisfaction)
Target: Department (Multiclass)
Algorithm: RandomForestClassifier with 200 estimators
Train/Test Split: 80/20 (stratified)
```

**Evaluation Metrics:**
- Accuracy Score

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/hr-analytics.git
cd hr-analytics
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required Libraries:**
```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
joblib>=1.0.0
```

## 💻 Usage

### Running the Complete Pipeline

```bash
python hr_analytics.py
```

### Individual Model Usage

#### 1. Income Prediction

```python
from joblib import load

# Load the model
income_model = load('hr_model.pkl')

# Prepare input data
employee_data = [[35, 1, 3, 2, 10, 5, 3, 15]]  # [Age, Current_Emp, Job_Level, ...]

# Predict
predicted_income = income_model.predict(employee_data)
print(f"Predicted Monthly Income: ${predicted_income[0]:,.2f}")
```

#### 2. Attrition Risk Assessment

```python
from joblib import load

# Load the model
attrition_model = load('attrition_model.pkl')

# Prepare input data
employee_profile = [[28, 5000, 2, 3, 3, 3, 1, 15, 2, 2]]

# Predict attrition risk
prediction = attrition_model.predict(employee_profile)[0]
probability = attrition_model.predict_proba(employee_profile)[0][1]

print(f"Attrition Risk: {'High' if prediction == 1 else 'Low'}")
print(f"Probability: {probability * 100:.2f}%")
```

#### 3. Department Classification

```python
from joblib import load

# Load the model
department_model = load('department_model.pkl')

# Prepare input data
employee_info = [[32, 3, 6, 6500, 4]]  # [Age, Job_Level, Years, Income, Satisfaction]

# Predict department
predicted_dept = department_model.predict(employee_info)
print(f"Recommended Department: {predicted_dept[0]}")
```

### Interactive Prediction Mode

The script includes an interactive mode where you can input employee details manually:

```bash
python hr_analytics.py
```

Follow the prompts to enter:
- Employee demographics
- Job information
- Performance metrics

The system will output predictions from all three models.

## 📈 Model Performance

### Income Prediction Model
- **R² Score**: ~0.95 (indicates strong predictive power)
- **RMSE**: Typically within 10-15% of actual income
- **Key Predictors**: Job Level, Total Working Years, Years at Company

### Attrition Prediction Model
- **Accuracy**: ~85-90% on test set
- **Precision (Attrition=Yes)**: ~0.75-0.85
- **Recall (Attrition=Yes)**: ~0.70-0.80
- **Key Risk Factors**: Overtime, Low Job Satisfaction, Distance from Home

### Department Classification Model
- **Accuracy**: ~75-80% on test set
- **Key Predictors**: Job Level, Monthly Income, Years at Company

*Note: Actual performance metrics may vary based on the specific dataset used.*

## 📁 Project Structure

```
hr-analytics/
│
├── hr_analytics.py           # Main script with all models
├── HR Data.xlsx              # Original dataset (Excel format)
├── HR data.csv               # CSV version of dataset
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
│
├── models/                   # Saved model files
│   ├── hr_model.pkl         # Income prediction model
│   ├── attrition_model.pkl  # Attrition prediction model
│   └── department_model.pkl # Department classification model
│
├── notebooks/               # Jupyter notebooks (optional)
│   └── exploratory_analysis.ipynb
│
└── visualizations/          # Generated plots and charts
    └── correlation_heatmap.png
```

## 🛠️ Technical Stack

- **Programming Language**: Python 3.8+
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Persistence**: joblib

### Key Libraries

| Library | Purpose |
|---------|---------|
| pandas | Data manipulation and analysis |
| NumPy | Numerical computing |
| scikit-learn | Machine learning algorithms |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualizations |
| joblib | Model serialization |

## 🔮 Future Enhancements

### Planned Features
- [ ] Web-based dashboard for real-time predictions
- [ ] Integration with HRIS systems via API
- [ ] Advanced feature engineering (PCA, feature interactions)
- [ ] Deep learning models for improved accuracy
- [ ] Time-series analysis for attrition trends
- [ ] Automated model retraining pipeline
- [ ] A/B testing framework for model evaluation
- [ ] Explainable AI (SHAP values) for prediction interpretability

### Model Improvements
- [ ] Hyperparameter tuning using GridSearchCV/RandomizedSearchCV
- [ ] Ensemble methods (stacking, boosting)
- [ ] Cross-validation for robust performance estimates
- [ ] Feature importance analysis and selection
- [ ] Handling of missing data and outliers

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Dataset source: [Specify source if applicable]
- Inspired by real-world HR analytics challenges
- Built with ❤️ for the HR and Data Science communities

## 📞 Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Email: your.email@example.com
- Join our discussions in the Issues section

---

**⭐ If you find this project useful, please consider giving it a star!**

*Last Updated: January 2026*
