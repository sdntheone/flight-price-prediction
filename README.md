# ✈️ Flight Price Prediction Model

This project predicts flight ticket prices based on various journey details using machine learning techniques. It includes a full pipeline for data preprocessing, feature engineering, model training, and evaluation — along with a clean Flask-based frontend for user-friendly interaction.

---

## 🔧 Technologies & Libraries Used

- **Python** – Core programming language  
- **NumPy** & **Pandas** – Data manipulation and analysis  
- **Scikit-learn** – Machine learning tools including:
  - `SimpleImputer` for missing data handling  
  - `StandardScaler` for feature scaling  
  - `OneHotEncoder` for categorical encoding  
  - `Pipeline` and `ColumnTransformer` for streamlined preprocessing  
  - Regression models: `LinearRegression`, `SVR`, `RandomForestRegressor`  
  - Metrics and evaluation tools: `r2_score`, `learning_curve`  
- **Feature-engine** – Advanced feature engineering, especially `DatetimeFeatures` for extracting time-based features from date columns  
- **Flask** – Web framework used to build a responsive frontend for prediction input and output  

---

## 🚀 Features

- Automated data preprocessing and feature engineering pipeline  
- Handling of missing values and categorical data encoding  
- Extraction of rich datetime features to improve model accuracy  
- Multiple regression models tested for best performance  
- Evaluation of models with R² score and learning curves visualization  
- Interactive Flask web app for easy input of flight details and price prediction  

---

## 📋 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sdntheone/flight-price-prediction.git
   cd flight-price-prediction
