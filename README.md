SupplySense-AI

AI-Powered Retail Demand Forecasting and Supply Chain Decision Support System

SupplySense-AI is an end-to-end machine learning project designed to transform historical retail sales data into actionable supply chain decisions.

The system goes beyond traditional demand forecasting. Instead of only predicting future sales, SupplySense-AI analyzes demand trends, estimates forecast confidence, calculates operational risk, generates business recommendations, visualizes historical performance, and allows users to test alternative operational scenarios through an interactive dashboard.

The project uses historical retail and operational data to train a Random Forest Regression model for store-level sales forecasting. The machine learning pipeline includes data understanding, feature engineering, model training, prediction, evaluation, and integration with a decision-support system.

One of the key components of the project is the Decision Engine. The predicted demand is combined with information such as demand trends, forecast reliability, promotional activity, and operational conditions. Based on these factors, the system calculates a risk score and produces an interpretable recommendation for decision-makers.

The project also includes a What-If Scenario Simulator. This feature allows users to modify operational conditions, such as activating or deactivating a promotion, and rerun the prediction pipeline. The system then compares the baseline forecast with the simulated forecast and displays the absolute change, percentage impact, change in risk score, demand trend, and recommendation.

Main Features:

Store-level retail demand forecasting using machine learning.
Random Forest Regression for sales prediction.
Historical sales trend visualization.
Actual vs predicted sales comparison.
Demand trend classification into Rising, Falling, or Stable conditions.
Forecast confidence estimation based on historical prediction performance.
Operational risk scoring.
Rule-based decision recommendation engine.
Interactive What-If Scenario Simulator.
Baseline vs scenario forecast comparison.
Interactive Streamlit dashboard.
Modular project architecture separating prediction, decision logic, data processing, and user interface components.

Technology Stack:

Python, Pandas, NumPy, Scikit-learn, Joblib, Streamlit, Jupyter Notebook, and machine learning techniques for regression and decision support.

Project Workflow:

The project begins with historical retail data exploration and preprocessing. Relevant features are then prepared for model training. A Random Forest Regression model is trained to predict sales demand. The trained model and supporting artifacts are saved and loaded by the prediction pipeline.

When a user selects a store and date through the dashboard, the system retrieves the corresponding operational data and sends it through the prediction pipeline. The predicted sales value is then analyzed by the Decision Engine, which determines the demand trend, forecast confidence, operational risk score, and recommendation.

The dashboard displays the prediction results together with recent sales history and an actual-versus-predicted sales comparison.

The What-If Scenario Simulator creates an independent copy of the selected operational conditions, modifies the selected scenario variable, and sends the modified data through the same prediction and decision pipeline. This ensures that baseline and scenario results can be directly compared.

Why This Project Matters:

Most beginner machine learning projects stop after displaying a prediction or accuracy score. SupplySense-AI was designed around a broader question: how can a machine learning prediction actually support a business decision?

The system connects forecasting with risk assessment, explainable recommendations, historical visualization, and scenario analysis. This makes the project closer to a decision-support prototype rather than a standalone prediction model.

Future Scope:

The project can be expanded with inventory optimization, reorder-point recommendations, safety stock calculation, SKU-level forecasting, supplier lead-time risk analysis, probabilistic forecasting, automated retraining pipelines, SHAP-based model explanations, multi-variable scenario simulation, and cloud deployment.

Project Vision:

Predicting demand tells us what may happen. Risk analysis tells us how seriously we should respond. Decision intelligence helps determine what action should be considered.

SupplySense-AI brings these three layers together in a single machine learning-powered supply chain decision-support system.
