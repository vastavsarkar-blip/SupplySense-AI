import sys
from pathlib import Path

import pandas as pd
import streamlit as st

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = BASE_DIR / "src"

sys.path.append(str(SRC_DIR))

from predictor import predict_and_decide


st.set_page_config(
    page_title="SupplySense-AI",
    page_icon="📦",
    layout="wide"
)

st.title("SupplySense-AI")
st.subheader("AI-Powered Supply Chain Decision Support System")

st.markdown("---")

DATA_PATH = BASE_DIR / "data" / "processed" / "model_data.pkl"


@st.cache_data
def load_data():
    return pd.read_pickle(DATA_PATH)


df = load_data()

st.sidebar.header("Decision Controls")

store_id = st.sidebar.selectbox(
    "Select Store",
    sorted(df["Store"].unique())
)

store_data = df[df["Store"] == store_id].copy()

selected_date = st.sidebar.selectbox(
    "Select Date",
    sorted(store_data["Date"].unique(), reverse=True)
)

selected_rows = store_data[
    store_data["Date"] == selected_date
]

if selected_rows.empty:
    st.error("No data found for this store and date.")
    st.stop()

selected_row = selected_rows.iloc[0].copy()


if st.sidebar.button("Generate Decision"):

    result = predict_and_decide(
        feature_row=selected_row,
        store_id=store_id
    )
    st.session_state["result"] = result
    st.success("Decision generated successfully")

if "result" in st.session_state:

    result = st.session_state["result"]

    # all result-dependent UI goes here:
    # metrics
    # recommendation
    # charts if they depend on result
    # operational risk alert

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Predicted Sales",
        f"{result['predicted_sales']:,.0f}"
    )

    col2.metric(
        "Demand Trend",
        result["demand_trend"]
    )

    col3.metric(
        "Forecast Confidence",
        result["forecast_confidence"]
    )

    col4.metric(
        "Risk Score",
        result["risk_score"]
    )

    st.markdown("---")

    st.subheader("AI Recommendation")

    st.info(result["recommendation"])
st.markdown("---")
st.subheader("Recent Sales History")

history = (
    store_data[
        store_data["Date"] <= selected_date
    ]
    .sort_values("Date")
    .tail(30)
)

chart_data = (
    history[
        ["Date", "Sales"]
    ]
    .set_index("Date")
)

st.line_chart(chart_data)
st.markdown("---")
st.subheader("Actual vs Predicted Sales")

comparison_rows = (
    store_data[
        store_data["Date"] <= selected_date
    ]
    .sort_values("Date")
    .tail(30)
)

comparison_results = []

for _, row in comparison_rows.iterrows():

    prediction_result = predict_and_decide(
        feature_row=row.copy(),
        store_id=store_id
    )

    comparison_results.append({
        "Date": row["Date"],
        "Actual Sales": row["Sales"],
        "Predicted Sales": prediction_result["predicted_sales"]
    })


comparison_df = pd.DataFrame(comparison_results)

comparison_df = comparison_df.set_index("Date")

st.line_chart(
    comparison_df[
        ["Actual Sales", "Predicted Sales"]
    ]
)
# --------------------------------------------------
# RISK ALERT PANEL
# --------------------------------------------------

st.markdown("---")
st.subheader("Operational Risk Alert")

risk_score = result["risk_score"]

if risk_score >= 75:
    risk_level = "CRITICAL"
    risk_message = (
        "Immediate attention required. Demand conditions and forecast "
        "uncertainty indicate significant operational risk."
    )
    st.error(f"🔴 {risk_level} RISK — Score: {risk_score}/100")
    st.error(risk_message)

elif risk_score >= 50:
    risk_level = "HIGH"
    risk_message = (
        "Elevated operational risk detected. Review inventory, staffing, "
        "and replenishment plans."
    )
    st.warning(f"🟠 {risk_level} RISK — Score: {risk_score}/100")
    st.warning(risk_message)

elif risk_score >= 25:
    risk_level = "MODERATE"
    risk_message = (
        "Some uncertainty is present. Continue monitoring demand signals "
        "and forecast performance."
    )
    st.warning(f"🟡 {risk_level} RISK — Score: {risk_score}/100")
    st.info(risk_message)

else:
    risk_level = "LOW"
    risk_message = (
        "Current demand conditions appear stable. Maintain normal operations "
        "and continue routine monitoring."
    )
    st.success(f"🟢 {risk_level} RISK — Score: {risk_score}/100")
    st.success(risk_message)
    # --------------------------------------------------
# WHAT-IF SCENARIO SIMULATOR
# --------------------------------------------------

st.markdown("---")
st.subheader("What-If Scenario Simulator")

st.write(
    "Test how changing operational conditions affects "
    "the forecast and decision recommendation."
)

scenario_promo = st.toggle(
    "Activate Promotion",
    value=bool(selected_row["Promo"])
)

if st.button("Run Scenario Simulation"):

    # Create an independent scenario copy
    scenario_row = selected_row.copy()

    # Modify scenario input
    scenario_row["Promo"] = int(scenario_promo)
    st.write("Original Promo:", selected_row["Promo"])
    st.write("Scenario Promo:", scenario_row["Promo"])

    # Run scenario through the actual ML pipeline
    scenario_result = predict_and_decide(
    feature_row=scenario_row,
    store_id=store_id
)

    baseline_sales = result["predicted_sales"]
    scenario_sales = scenario_result["predicted_sales"]

    sales_change = scenario_sales - baseline_sales

    if baseline_sales != 0:
        percentage_change = (
            sales_change / baseline_sales
        ) * 100
    else:
        percentage_change = 0

    st.markdown("### Scenario Impact")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Baseline Forecast",
        f"{baseline_sales:,.0f}"
    )

    col2.metric(
        "Scenario Forecast",
        f"{scenario_sales:,.0f}",
        delta=f"{sales_change:+,.0f}"
    )

    col3.metric(
        "Forecast Impact",
        f"{percentage_change:+.2f}%"
    )

    st.markdown("### Decision Comparison")

    comparison_col1, comparison_col2 = st.columns(2)

    with comparison_col1:
        st.write("**Baseline Decision**")
        st.write(f"Risk Score: {result['risk_score']}")
        st.write(
            f"Demand Trend: {result['demand_trend']}"
        )
        st.info(result["recommendation"])

    with comparison_col2:
        st.write("**Scenario Decision**")
        st.write(
            f"Risk Score: {scenario_result['risk_score']}"
        )
        st.write(
            f"Demand Trend: "
            f"{scenario_result['demand_trend']}"
        )
        st.info(
            scenario_result["recommendation"]
        )