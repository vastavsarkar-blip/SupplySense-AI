# 📦 SupplySense-AI

## AI-Powered Retail Demand Forecasting & Decision Support System

**SupplySense-AI** is an intelligent retail demand forecasting and decision-support prototype designed to transform historical sales data into actionable operational insights.

Traditional forecasting projects often stop after predicting future sales. SupplySense-AI goes further by combining **machine learning forecasting, forecast reliability analysis, risk scoring, operational recommendations, and what-if scenario simulation** within a single interactive system.

The project is built using the **Rossmann Store Sales dataset** and demonstrates how machine learning can support more informed retail and supply chain decisions.

---

## 🎯 Project Objective

The main objective of SupplySense-AI is to build a system that answers more than:

> **“What will the expected sales be?”**

The system also attempts to answer:

> **“How reliable is the forecast, what operational risk does it indicate, and what action should be considered?”**

This transforms the project from a basic prediction model into a practical **decision-support prototype**.

---

## 🧠 System Architecture

Historical Retail Data
↓
Data Processing & Cleaning
↓
Feature Engineering
↓
Machine Learning Forecasting
↓
Forecast Reliability Assessment
↓
Demand Trend Analysis
↓
Operational Risk Scoring
↓
Actionable Recommendation
↓
What-If Scenario Simulation
↓
Interactive Dashboard

---

## 📊 Dataset

The project uses the **Rossmann Store Sales dataset**, containing historical daily sales information across multiple retail stores.

The main datasets used are:

* `train.csv`
* `store.csv`

The datasets are merged using the `Store` identifier.

The combined dataset contains approximately **1.01 million records before feature engineering** and approximately **986,000 usable records after feature generation and preprocessing**.

A **time-based train-validation split** is used instead of a random split to better represent a real forecasting scenario.

### Training Period

29 January 2013 – 18 June 2015

### Validation Period

19 June 2015 – 31 July 2015

This approach prevents future observations from being randomly mixed into historical training data.

---

## ⚙️ Feature Engineering

SupplySense-AI uses multiple categories of engineered features to capture temporal patterns, store characteristics, promotional activity, competition effects, and recent demand behaviour.

### Calendar Features

* Day
* Month
* Year
* Day of week
* Week of year
* Weekend indicators
* Seasonal time patterns

### Store and Competition Features

* Store type
* Assortment information
* Competition distance
* Competition duration

### Promotion Features

* Promo status
* Promo2 information
* Promotion timing patterns

### Time-Series Features

* Lag-based sales features
* Rolling demand statistics
* Sales momentum
* Recent demand trend indicators

These features help the model understand both long-term store characteristics and short-term changes in sales behaviour.

---

## 🤖 Machine Learning Model

The forecasting engine is built using a **Random Forest Regressor**.

The model learns relationships between historical demand, calendar information, promotions, competition characteristics, store-level information, and engineered time-series features.

The trained model is then used by the prediction pipeline to generate store-level sales forecasts.

The forecasting model acts as the analytical foundation of the complete SupplySense-AI decision pipeline.

---

## 🧩 Beyond Forecasting

A major goal of SupplySense-AI is to move beyond raw sales prediction.

The system combines multiple analytical stages:

### 1. Demand Forecasting

The machine learning model predicts expected sales demand for the selected store and date context.

### 2. Forecast Reliability

The system evaluates historical forecasting behaviour to provide additional context about forecast reliability.

### 3. Demand Trend Analysis

Recent sales patterns are analysed to understand whether demand behaviour is increasing, decreasing, or remaining relatively stable.

### 4. Risk Scoring

Forecast information, demand behaviour, and reliability signals are converted into an operational risk assessment.

### 5. Recommendation Engine

The decision engine translates analytical outputs into understandable operational recommendations.

The goal is to bridge the gap between:

**Prediction → Interpretation → Decision Support**

---

## 🔮 What-If Scenario Simulation

SupplySense-AI includes a what-if simulation layer for exploring alternative operational scenarios.

Instead of treating the forecast as a static output, the system allows different demand situations to be explored and their potential impact on operational decisions to be evaluated.

This feature demonstrates how predictive models can be extended into interactive decision-support tools.

---

## 🖥️ Interactive Dashboard

The project includes an interactive Streamlit dashboard located at:

`app/dashboard.py`

The dashboard allows users to:

* Select a store
* Select a date
* Analyse historical demand behaviour
* Generate sales forecasts
* Evaluate forecast reliability
* View operational risk
* Receive actionable recommendations
* Explore what-if scenarios

The dashboard connects the machine learning pipeline with the decision engine to provide a unified user experience.

---

## 📁 Project Structure

SupplySense-AI/

├── app/

│   └── dashboard.py

├── models/

│   ├── feature_columns.joblib

│   ├── random_forest_sales_model.joblib

│   └── store_error_profile.csv

├── notebooks/

│   ├── data exploration and preprocessing notebooks

│   ├── feature engineering notebooks

│   └── model development notebooks

├── src/

│   ├── predictor.py

│   └── decision_engine.py

├── .gitignore

├── requirements.txt

└── README.md

---

## 🛠️ Technology Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Regression
* Joblib
* Streamlit
* Matplotlib
* Feature Engineering
* Time-Series Analysis
* Machine Learning

---

## 🚀 How the System Works

1. Historical store sales and store metadata are processed.

2. Calendar, promotion, competition, lag, rolling, momentum, and trend features are generated.

3. The trained Random Forest model predicts expected sales.

4. Forecast reliability information is evaluated.

5. Recent demand behaviour is analysed.

6. The decision engine calculates operational risk.

7. The system generates an actionable recommendation.

8. Users can explore alternative scenarios through the what-if simulation layer.

9. Results are displayed through the interactive Streamlit dashboard.

---

## 💡 What Makes SupplySense-AI Different?

Many beginner machine learning projects follow this pipeline:

**Dataset → Model → Prediction**

SupplySense-AI follows a broader approach:

**Dataset → Features → Forecast → Reliability → Trend → Risk → Recommendation → Simulation → Decision Support**

The key idea is that a prediction alone is rarely enough for operational decision-making.

SupplySense-AI demonstrates how machine learning outputs can be transformed into structured and understandable decision-support signals.

---

## 🔮 Future Improvements

Future versions of SupplySense-AI could include:

* Comparison with gradient boosting and advanced forecasting models
* Probabilistic forecasting and prediction intervals
* Multi-store forecasting at scale
* Inventory-level data integration
* Supplier lead-time modelling
* Stockout probability estimation
* Overstock cost modelling
* Dynamic safety-stock recommendations
* Multi-objective inventory optimization
* Automated model retraining
* Real-time data pipeline integration
* Cloud deployment
* Explainable AI for recommendation transparency

---

## 🎯 Key Learning Outcomes

This project demonstrates practical experience in:

* Retail demand forecasting
* Machine learning
* Feature engineering
* Time-aware model validation
* Time-series feature creation
* Forecast reliability analysis
* Risk scoring
* Decision-engine development
* What-if scenario simulation
* Streamlit application development
* End-to-end ML system design

---

## ⚠️ Project Scope

SupplySense-AI is a machine learning and decision-support prototype.

The system demonstrates how historical retail data can be transformed into forecasts, risk indicators, and operational recommendations. However, real-world supply chain deployment would require additional data such as inventory levels, supplier lead times, procurement costs, stockout costs, logistics constraints, and real-time operational information.

The recommendations generated by the current system should therefore be treated as analytical decision-support outputs rather than autonomous supply chain decisions.

---

## 👨‍💻 Project Vision

The long-term vision of SupplySense-AI is to evolve from a retail demand forecasting prototype into an intelligent supply chain decision system capable of answering three critical questions:

**What is likely to happen?**

**How risky is the situation?**

**What action should be considered next?**

SupplySense-AI represents a step toward building machine learning systems that do more than predict numbers—they help convert data into decisions.
