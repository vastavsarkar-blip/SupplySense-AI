I built SupplySense-AI, a retail demand forecasting and decision-support prototype. I used historical store-sales data and engineered calendar, competition, promotion, lag, rolling-statistics, momentum, and trend features. I used chronological validation rather than random splitting and compared the model against a Lag-7 baseline. The Random Forest reduced validation MAE from about 1,883 to 484 in our evaluation setup.

After training, I performed leakage checks and analyzed errors at both store and demand-segment levels. Because model reliability varied significantly across stores, I used store-level historical error profiles to create forecast-confidence categories.

I then built a transparent decision engine that combines forecast confidence, demand trend, promotion and holiday conditions into an operational attention score and recommendation. Finally, I connected everything through a Streamlit dashboard with historical analysis, actual-vs-predicted visualization, risk alerts, and a model-based what-if simulator.

The project is a decision-support prototype rather than a full supply-chain optimization system, because the dataset lacks inventory, SKU-level demand, lead times and cost constraints.
