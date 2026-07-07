from pathlib import Path
from decision_engine import make_decision

import joblib
import pandas as pd


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


# Load saved artifacts
model = joblib.load(
    MODEL_DIR / "random_forest_sales_model.joblib"
)

feature_cols = joblib.load(
    MODEL_DIR / "feature_columns.joblib"
)

store_errors = pd.read_csv(
    MODEL_DIR / "store_error_profile.csv"
)


print("SupplySense-AI predictor initialized")
print("-----------------------------------")
print("Model:", type(model).__name__)
print("Expected features:", len(feature_cols))
print("Store risk profiles:", len(store_errors))
print("Error profile columns:", store_errors.columns.tolist())
def predict_and_decide(feature_row, store_id):
        # Convert a single pandas Series into a one-row DataFrame
    if isinstance(feature_row, pd.Series):
        feature_row = feature_row.to_frame().T

    # Validate and order features exactly as model expects
    missing_cols = [
        col for col in feature_cols
        if col not in feature_row.columns
    ]

    if missing_cols:
        raise ValueError(
            f"Missing required features: {missing_cols}"
        )

    X = feature_row[feature_cols]

    # Generate sales prediction
    predicted_sales = model.predict(X)[0]

    # Get store-specific historical model error
    store_profile = store_errors[
        store_errors["Store"] == store_id
    ]

    if store_profile.empty:
        relative_mae = store_errors["RelativeMAE_pct"].median()
    else:
        relative_mae = store_profile["RelativeMAE_pct"].iloc[0]

    # Extract decision signals
    sales_momentum = feature_row["SalesMomentum"].iloc[0]
    sales_trend = feature_row["SalesTrend"].iloc[0]
    promo = feature_row["Promo"].iloc[0]

    # Reconstruct holiday state from one-hot columns
    holiday_cols = [
        col for col in feature_row.columns
        if col.startswith("StateHoliday_")
        and feature_row[col].iloc[0] == 1
    ]

    state_holiday = (
        holiday_cols[0].replace("StateHoliday_", "")
        if holiday_cols
        else "0"
    )

    # Send forecast to decision engine
    decision = make_decision(
        predicted_sales=predicted_sales,
        sales_momentum=sales_momentum,
        sales_trend=sales_trend,
        promo=promo,
        state_holiday=state_holiday,
        relative_mae=relative_mae
    )

    decision["store_id"] = int(store_id)

    return decision
if __name__ == "__main__":

    DATA_PATH = (
        BASE_DIR
        / "data"
        / "processed"
        / "model_data.pkl"
    )

    print("\nLoading test data...")

    df = pd.read_pickle(DATA_PATH)

    # Use one genuine row
    test_row = df.iloc[0].copy()

    store_id = int(test_row["Store"])

    result = predict_and_decide(
        feature_row=test_row,
        store_id=store_id
    )

    print("\nEnd-to-End Prediction Test")
    print("--------------------------")

    for key, value in result.items():
        print(f"{key}: {value}")