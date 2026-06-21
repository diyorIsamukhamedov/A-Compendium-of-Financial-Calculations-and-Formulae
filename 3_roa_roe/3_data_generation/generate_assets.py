"""Synthetic asset ledger generator for the 3_roa_roe topic.

This module builds a reproducible 300,000-row asset ledger, embeds a real
relationship between the features and the amount, enforces the per-date total
assets invariant on the clean data, injects a controlled noise typology and
writes the resulting messy ledger to a CSV file for the ETL stage.
"""

from typing import Optional
import numpy as np
import pandas as pd

# consts


# my seed is the starting value used to initialise a pseudorandom number generator.
# num 42 is a common default in the DS world
SEED: int = 42


# COUNT_PER_DATE is the number of rows for one reporting date (one quarter).
# Formula: all dataset rows divided by 6:
# 300,000 / 6 = 50,000
COUNT_PER_DATE: int = 50_000

# I have 6 quarters, listed explicitly
REPORT_DATES: list[str] = [
    "2024-Q1",
    "2024-Q2",
    "2024-Q3",
    "2024-Q4",
    "2025-Q1",
    "2025-Q2",
]

# End-of-period total assets per reporting date, in mln UZS (Uzbekistan).
# 2024-Q3 and 2024-Q4 are fixed by my handwritten konspekt so that the 2024-Q4
# average assets reconcile to (11,600 + 12,400) / 2 = 12,000 from the data itself.
# The other dates form a sensible upward trend
TOTALS_BY_DATE: dict[str, float] = {
    "2024-Q1": 10_800.0, # synthetic num, chosen by me
    "2024-Q2": 11_200.0, # synthetic num, chosen by me
    "2024-Q3": 11_600.0, # fixed by me
    "2024-Q4": 12_400.0, # fixed by me
    "2025-Q1": 12_800.0, # synthetic num, chosen by me
    "2025-Q2": 13_200.0  # synthetic num, chosen by me
}

# types of assets for data modelling, used later in the DB (PostgreSQL)
ASSET_TYPES: list[str] = ["loan", "security", "interbank", "cash"]

# in a standard banking currency architecture, currencies are split into at
# least 3 main ones: the local one (UZS) and the foreign ones (USD, EUR)
CURRENCIES: list[str] = ["UZS", "USD", "EUR"]

# standardised column names by me, for matching later in ETL
ASSET_ID: str = "asset_id"
REPORT_DATE: str = "report_date"
ASSET_TYPE: str = "asset_type"
CURRENCY: str = "currenncy"
TERM_MONTHS: str = "term_month"
INTEREST_RATE: str = "interest_rate"
AMOUNT: str = "amount"

# Feature range
TERM_MIN_MONTHS: int = 1
# 10 years is a reasonable upper bound for an asset term
# Formula: max months divided by 12:
# 120 / 12 = 10 yrs
TERM_MAX_MONTHS: int = 120
RATE_MIN: float = 0.0
RATE_MAX: float = 24.0
# round to 2 decimal places
RATE_DP: int = 2

# Feature-to-amount relationship, applied to the raw weights before scaling:
# weight = base_by_type + RATE_COEFFICIENT * (rate - RATE_CENTRE) + TERM_COEFFICIENT * term + noise
# Tune NOISE_SD so the ML stage reaches an R-squared near 0.6, and keep every
# weight strictly positive so all amounts stay positive after scaling.
BASE_BY_TYPE: dict[str, float] = {
    "loan": 1000.0,     # synthetic num, chosen by me
    "security": 900.0,  # synthetic num, chosen by me
    "interbank": 800.0, # synthetic num, chosen by me
    "cash": 700.0       # synthetic num, chosen by me
}
RATE_CENTRE: float = 12.0
RATE_COEFFICIENT: float = -24
TERM_COEFFICIENT: float = 2.0
NOISE_SD: float = 50.0
WEIGHT_FLOOR: float = 1.0

# Money scale and invariant tolerance. Six decimals on mln uzs keep the
# last-row rounding remainder negligible relative to a single row's amount.
MONEY_SCALE_DP: int = 6
INVARIANT_TOLERANCE: float = 1e-4

# Noise fractions
WHITESPACE_FRACTION: float = 0.05
CASE_NOISE_FRACTION: float = 0.05
NULL_FRACTION: float = 0.03
DUPLICATE_FRACTION: float = 0.02

# Columns that may receive nulls. Never amount, asset_id or report_date.
# Currency is a non-feature, so imputing it does not weaken the ML signal.
NULLABLE_COLUMNS: list[str] = [CURRENCY]

# Messy display headers used in the saved CSV.
MESSY_HEADERS: dict[str, str] = {
    ASSET_ID: "Assed ID",
    REPORT_DATE: "Report Date",
    ASSET_TYPE: "Asset Type",
    CURRENCY: "Currency",
    TERM_MONTHS: "Term Month",
    INTEREST_RATE: "Interest Rate",
    AMOUNT: "Amount"
}

# Output file location for the messy ledger
MESSY_CSV_PATH: str = "../data/assets_messy.csv"

# dataset generation
def split_total(
    weights: np.ndarray,
    period_total: float,
    money_scale_dp: int        
) -> np.ndarray:
    pass