# Feature Engineering (feature_engineering.py)
import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add agent and ML ready features
    """
    df["cpc"] = df["budget"] / df["clicks"]
    df["conversion_rate"] = df["conversions"] / df["clicks"]

    return df

# 🧠 Concepts to MASTER, Feature engineering, Vectorized operations, Derived metrics

# 📌 This is used in Predictive models, Rule engines, Optimization agents