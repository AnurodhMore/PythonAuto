
import pandas as pd

df = pd.read_csv("/Users/anurodhmore/Downloads/mass_income_practice_dataset.csv")

# Estimate weighted yield for each portfolio
df["weighted_yield_contribution"] = (
    df["weight_pct"] * df["indicative_yield_pct"] / 100
)

summary = (
    df.groupby("model_portfolio")
    .agg(
        total_allocation_pct=("weight_pct", "sum"),
        estimated_yield_pct=("weighted_yield_contribution", "sum"),
        average_volatility_pct=(
            "illustrative_annualized_volatility_pct", "mean"
        )
    )
    .round(2)
)

print(summary)
