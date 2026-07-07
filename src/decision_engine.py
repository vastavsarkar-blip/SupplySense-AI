def classify_forecast_confidence(relative_mae):
    """
    Convert historical store-level forecast error
    into an interpretable confidence level.
    """

    if relative_mae <= 8:
        return "HIGH"
    elif relative_mae <= 15:
        return "MEDIUM"
    else:
        return "LOW"


def classify_demand_trend(sales_momentum, sales_trend):
    """
    Identify the direction of recent demand.
    """

    if sales_momentum > 1.10 and sales_trend > 0:
        return "RISING"

    elif sales_momentum < 0.90 and sales_trend < 0:
        return "FALLING"

    else:
        return "STABLE"


def calculate_risk_score(
    confidence,
    demand_trend,
    promo,
    state_holiday
):
    """
    Calculate an operational attention score from 0 to 100.
    Higher score means greater need for managerial attention.
    """

    score = 0

    # Forecast uncertainty
    if confidence == "LOW":
        score += 40
    elif confidence == "MEDIUM":
        score += 20

    # Demand movement
    if demand_trend == "RISING":
        score += 25
    elif demand_trend == "FALLING":
        score += 15

    # Promotion effect
    if promo == 1:
        score += 15

    # Holiday effect
    if str(state_holiday) != "0":
        score += 20

    return min(score, 100)


def generate_recommendation(
    demand_trend,
    confidence,
    risk_score
):
    """
    Generate an explainable operational recommendation.
    """

    if confidence == "LOW":
        return (
            "Forecast uncertainty is high. "
            "Review recent store performance before making major operational decisions."
        )

    if demand_trend == "RISING" and risk_score >= 40:
        return (
            "Demand is rising. Prepare additional operational capacity "
            "and monitor short-term demand closely."
        )

    if demand_trend == "FALLING":
        return (
            "Demand is declining. Avoid unnecessary capacity expansion "
            "and review promotion effectiveness."
        )

    return (
        "Demand is stable. Maintain current operating levels "
        "and continue monitoring demand signals."
    )


def make_decision(
    predicted_sales,
    sales_momentum,
    sales_trend,
    promo,
    state_holiday,
    relative_mae
):
    """
    Main decision-support pipeline.
    """

    confidence = classify_forecast_confidence(relative_mae)

    demand_trend = classify_demand_trend(
        sales_momentum,
        sales_trend
    )

    risk_score = calculate_risk_score(
        confidence,
        demand_trend,
        promo,
        state_holiday
    )

    recommendation = generate_recommendation(
        demand_trend,
        confidence,
        risk_score
    )

    return {
        "predicted_sales": round(float(predicted_sales), 2),
        "demand_trend": demand_trend,
        "forecast_confidence": confidence,
        "risk_score": risk_score,
        "recommendation": recommendation
    }
if __name__ == "__main__":

    test_cases = [
        {
            "name": "Rising demand",
            "predicted_sales": 8500,
            "sales_momentum": 1.18,
            "sales_trend": 950,
            "promo": 1,
            "state_holiday": "0",
            "relative_mae": 7.5
        },
        {
            "name": "Falling demand",
            "predicted_sales": 4200,
            "sales_momentum": 0.72,
            "sales_trend": -1200,
            "promo": 0,
            "state_holiday": "0",
            "relative_mae": 8.0
        },
        {
            "name": "Uncertain forecast",
            "predicted_sales": 6000,
            "sales_momentum": 1.02,
            "sales_trend": 100,
            "promo": 0,
            "state_holiday": "0",
            "relative_mae": 25.0
        },
        {
            "name": "Holiday and promotion",
            "predicted_sales": 12000,
            "sales_momentum": 1.35,
            "sales_trend": 2000,
            "promo": 1,
            "state_holiday": "a",
            "relative_mae": 12.0
        }
    ]

    for case in test_cases:

        name = case.pop("name")

        decision = make_decision(**case)

        print("\n" + "=" * 60)
        print(name)
        print("=" * 60)

        for key, value in decision.items():
            print(f"{key}: {value}")