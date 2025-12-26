import pandas as pd

def campaign_decision_agent(df: pd.DataFrame) -> pd.DataFrame:
    """
    Decide action for each campaign using business rule
    """

    def decide(row):
        if row["cpc"] < 3 and row["conversion_rate"] > 0.05:
            return "SCALE"
        elif row["cpc"] < 5:
            return "OPTIMIZE"
        else:
            return "PAUSE"

    df["action"] = df.apply(decide, axis=1)

    # Round numeric columns for display
    numeric_cols = ["cpc", "conversion_rate", "budget", "clicks", "conversions"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].round(2)

    return df
