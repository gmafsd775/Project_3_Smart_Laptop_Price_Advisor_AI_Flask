# 💻 Smart Laptop Price Advisor AI

An end-to-end Machine Learning web application that predicts laptop prices based on hardware specifications. The project covers the complete ML workflow—from data preprocessing and feature engineering to model selection and deployment using Flask.

---

## 📌 Project Overview

Smart Laptop Price Advisor AI is a Machine Learning project developed to estimate laptop prices using technical specifications such as brand, RAM, storage, processor, GPU, display, warranty, and other hardware features.

Instead of training a single model, multiple regression algorithms were evaluated, compared, and validated before selecting the final production model. The trained model was then integrated into a Flask web application with a modern Glassmorphism user interface.

> **Note:** The original dataset did not specify the currency of laptop prices. Therefore, the application displays only **Estimated Price** instead of assuming any currency.

---

# ✨ Features

* End-to-End Machine Learning Project
* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Advanced Feature Engineering
* Multiple Model Comparison
* 5-Fold Cross Validation
* Hyperparameter Tuning using GridSearchCV
* Linear Regression selected as Final Model
* Flask Web Application
* Responsive Glassmorphism UI
* Dynamic CPU Dropdowns
* Brand-wise Price Chart (Chart.js)
* AI Prediction Summary Card
* Prediction Details
* Professional Project Structure

---

# 📊 Dataset

* Laptop Price Prediction Dataset
* Source: Kaggle
* Dataset contains laptop hardware specifications and corresponding prices.

---

# ⚙️ Feature Engineering

The raw dataset contained a limited number of laptop specification columns. A complete feature engineering pipeline was developed to transform the raw data into machine-learning-ready features.

### Major preprocessing steps

* Standardized RAM values
* Converted storage values (TB → GB)
* Cleaned numerical columns
* Processed missing values
* Parsed CPU information into:

  * CPU Brand
  * CPU Family
  * CPU Series
  * CPU Generation
  * CPU Cores
  * CPU Threads
* Parsed GPU information into:

  * GPU Brand
  * GPU Series
  * GPU Memory
* Split display resolution into:

  * Resolution Width
  * Resolution Height
* Processed warranty information
* One-Hot Encoding of categorical features

### Feature Expansion

| Stage                                |           Approximate Features |
| ------------------------------------ | -----------------------------: |
| Original Dataset                     |               ~20 Raw Features |
| After Feature Engineering & Encoding | ~107 Machine Learning Features |

This transformation enabled the models to learn richer relationships from laptop specifications and improved predictive performance.

---

# 🤖 Machine Learning Pipeline

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Feature Encoding
      │
      ▼
Train/Test Split
      │
      ▼
Model Training
      │
      ▼
Cross Validation
      │
      ▼
GridSearchCV
      │
      ▼
Model Comparison
      │
      ▼
Final Model Selection
      │
      ▼
Flask Deployment
```

---

# 📈 Models Evaluated

| Model                              |  R² Score |        MAE |       RMSE |
| ---------------------------------- | --------: | ---------: | ---------: |
| **Linear Regression ⭐ (Selected)** | **0.863** | **14,001** | **21,640** |
| Random Forest (Tuned)              |     0.851 |     12,639 |     22,586 |
| Extra Trees Regressor              |     0.850 |     12,722 |     22,685 |
| Random Forest Regressor            |     0.848 |     12,794 |     22,839 |
| Decision Tree Regressor            |     0.720 |     15,770 |     30,949 |

---

# 🔧 Hyperparameter Tuning

Random Forest Regressor was optimized using **GridSearchCV**.

### Configuration

* Cross Validation: **5-Fold**
* Candidate Combinations: **24**
* Total Model Fits: **120**

### Best Parameters

```python
{
    "max_depth": 20,
    "min_samples_leaf": 1,
    "min_samples_split": 2,
    "n_estimators": 100
}
```

### Best Cross Validation Score

```
0.7785
```

Although Random Forest performance improved after tuning, **Linear Regression** achieved the highest overall R² score and was selected as the final production model due to its overall performance, simplicity, and deployment efficiency.

---

# 🏆 Final Model

**Model:** Linear Regression

### Performance

* R² Score: **0.863**
* MAE: **14,001**
* RMSE: **21,640**

---

# 🖥️ Application Preview

## Home Page

> *(Screenshot will be added here.)*

---

## Prediction Result

> *(Screenshot will be added here.)*

---

## Brand Price Analysis

> *(Screenshot will be added here.)*

---

## About AI Section

> *(Screenshot will be added here.)*

---

# 📁 Project Structure

```
Project_3_Smart_Laptop_Price_Advisor_AI_Flask
│
├── app.py
├── prediction.py
├── requirements.txt
├── README.md
│
├── data
│   └── laptop_price.csv
│
├── model
│   ├── laptop_price_model.pkl
│   └── feature_names.pkl
│
├── static
│   ├── css
│   ├── images
│   └── js
│
└── templates
    └── index.html
```

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

### Web Development

* Flask
* HTML5
* CSS3
* JavaScript

### Visualization

* Chart.js

---

# 🚀 Installation

```bash
git clone <repository-url>

cd Project_3_Smart_Laptop_Price_Advisor_AI_Flask

pip install -r requirements.txt

python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🔮 Future Improvements

* Support additional machine learning algorithms
* Add feature importance visualization
* Introduce model explainability (SHAP/LIME)
* Deploy cloud-hosted trained models
* Add laptop recommendation functionality
* Support real-time dataset updates

---

# 👨‍💻 Author

Developed as a Machine Learning portfolio project demonstrating an end-to-end workflow including data preprocessing, feature engineering, model evaluation, Flask integration, and deployment.

---

## ⭐ If you found this project helpful, consider giving it a star on GitHub.
