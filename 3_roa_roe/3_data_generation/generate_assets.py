"""
Generate a synthetic asset ledger for the ROA / ROE topic

The ledger holds granual asset-level records whose amounts sum,
per reporting date, to the total Assets figure from the handwritten text (the invariant)
noise is injected afterwards so the ETL pipline has a visible assertable effect. 
"""

# Configuration
SEED: int = 42

REPORT_DATES: list[str] = [
    "2024-Q1",
    "2024-Q2",
    "2024-Q3",
    "2024-Q4",
    "2025-Q1",
    "2025-Q2",
]

# TOtal Assets at each reporting date

import random
import pandas as pd
import numpy as np

def default_rng(df: pd.DataFrame, fraction: float) -> pd.DataFrame:
    """
    This function generates fixset duplicates

    formula: DataFrame length * fraction
    """
    n = round(len(df) * fraction)

    pass

def generate_assets(n: pd.DataFrame) -> pd.DataFrame:
    pass

rng = np.random.default_rng(42)