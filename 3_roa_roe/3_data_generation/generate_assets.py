"""Synthetic asset ledger generator for the 3_roa_roe topic."""

from typing import Optional
from pathlib import Path
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
CURRENCY: str = "currency"
TERM_MONTHS: str = "term_months"
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
BASE_BY_TYPE: dict[str, float] = {
    "loan": 1000.0,     # synthetic num, chosen by me
    "security": 900.0,  # synthetic num, chosen by me
    "interbank": 800.0, # synthetic num, chosen by me
    "cash": 700.0       # synthetic num, chosen by me
}
RATE_CENTRE: float = 12.0
RATE_COEFFICIENT: float = -24.0
TERM_COEFFICIENT: float = 2.0
NOISE_SD: float = 50.0
WEIGHT_FLOOR: float = 1.0

# Money scale and invariant tolerance
MONEY_SCALE_DP: int = 6
INVARIANT_TOLERANCE: float = 1e-4

# Noise fractions
WHITESPACE_FRACTION: float = 0.05
CASE_NOISE_FRACTION: float = 0.05
NULL_FRACTION: float = 0.03
DUPLICATE_FRACTION: float = 0.02

# Columns that may receive nulls. Never amount, asset_id or report_date
NULLABLE_COLUMNS: list[str] = [CURRENCY]

# Messy display headers used in the saved CSV
MESSY_HEADERS: dict[str, str] = {
    ASSET_ID: "Asset ID",
    REPORT_DATE: "Report Date",
    ASSET_TYPE: "Asset Type",
    CURRENCY: "Currency",
    TERM_MONTHS: "Term Months",
    INTEREST_RATE: "Interest Rate",
    AMOUNT: "Amount"
}

# Output file location for the messy ledger.
# I build the path from this file's own location, so it works no matter which
# folder I launch python from. This file sits in 3_data_generation, and I want
# the CSV one level up, in 3_roa_roe/data.
OUTPUT_CSV_PATH: str = str(Path(__file__).resolve().parent.parent / "data" / "assets_messy.csv")


# dataset generation
def split_total(
    weights: np.ndarray,
    period_total: float,
    money_scale_dp: int
) -> np.ndarray:
    """Distribute a period total across rows in proportion to the weights."""
    # I turn the period total into a per-weight factor
    scale = period_total / weights.sum()
    # I scale every weight, so a bigger weight gives a bigger amount
    amounts = weights * scale
    # I round each amount to my money scale
    amounts = np.round(amounts, money_scale_dp)
    # I drop the whole rounding remainder into the last row, so my sum is exact
    amounts[-1] = round(period_total - amounts[:-1].sum(), money_scale_dp)
    return amounts


def pick_categories(
    rng: np.random.Generator,
    categories: list[str],
    count: int,
    probabilities: Optional[np.ndarray]
) -> np.ndarray:
    """Draw a categorical column of the given length from the categories."""
    # I draw 'count' values from my list, equal odds unless I pass probabilities
    return rng.choice(categories, size=count, p=probabilities)


def build_clean_ledger(rng: np.random.Generator) -> pd.DataFrame:
    """Build the full clean asset ledger across all reporting dates."""
    # I collect one table per date, then glue them together at the end
    frames = []
    next_id = 1

    for i in range(len(REPORT_DATES)):
        date = REPORT_DATES[i]
        period_total = TOTALS_BY_DATE[date]

        # I draw the features for this date
        term = rng.integers(TERM_MIN_MONTHS, TERM_MAX_MONTHS + 1, COUNT_PER_DATE)
        rate = np.round(rng.uniform(RATE_MIN, RATE_MAX, COUNT_PER_DATE), RATE_DP)
        asset_type = pick_categories(rng, ASSET_TYPES, COUNT_PER_DATE, None)
        currency = pick_categories(rng, CURRENCIES, COUNT_PER_DATE, None)

        # I build the base part of the weight from the asset type
        base = np.empty(COUNT_PER_DATE)
        for j in range(COUNT_PER_DATE):
            base[j] = BASE_BY_TYPE[asset_type[j]]

        # I build the raw weight: base + rate effect + term effect + noise
        noise = rng.normal(0.0, NOISE_SD, COUNT_PER_DATE)
        weights = base + RATE_COEFFICIENT * (rate - RATE_CENTRE) + TERM_COEFFICIENT * term + noise
        # I keep every weight positive so my amounts stay positive
        weights = np.maximum(weights, WEIGHT_FLOOR)

        # I turn the weights into amounts that sum exactly to the period total
        amount = split_total(weights, period_total, MONEY_SCALE_DP)

        # I number the assets of this date
        asset_id = np.arange(next_id, next_id + COUNT_PER_DATE)
        next_id = next_id + COUNT_PER_DATE

        # I assemble this date's table
        frame = pd.DataFrame({
            ASSET_ID: asset_id,
            REPORT_DATE: date,
            ASSET_TYPE: asset_type,
            CURRENCY: currency,
            TERM_MONTHS: term,
            INTEREST_RATE: rate,
            AMOUNT: amount
        })
        frames.append(frame)

    # I stack all six dates into one ledger
    return pd.concat(frames, ignore_index=True)


def check_invariant(ledger: pd.DataFrame, tolerance: float) -> None:
    """Assert the per-date amount sum equals the target total for that date."""
    # I check, date by date, that my amounts add up to that date's target
    for i in range(len(REPORT_DATES)):
        date = REPORT_DATES[i]
        actual = ledger.loc[ledger[REPORT_DATE] == date, AMOUNT].sum()
        expected = TOTALS_BY_DATE[date]
        assert abs(actual - expected) <= tolerance, (
            f"invariant failed for {date}: {actual} vs {expected}"
        )


def inject_whitespace(
    rng: np.random.Generator,
    ledger: pd.DataFrame,
    fraction: float
) -> pd.DataFrame:
    """Return a copy with leading and trailing whitespace in some string cells."""
    # I copy the ledger so I do not change the clean one
    ledger = ledger.copy()
    # I pick a fraction of rows at random
    n = int(len(ledger) * fraction)
    idx = rng.choice(len(ledger), size=n, replace=False)
    # I pad my category cells with spaces
    for col in (ASSET_TYPE, CURRENCY):
        ledger.loc[idx, col] = " " + ledger.loc[idx, col].astype(str) + " "
    return ledger


def inject_case_noise(
    rng: np.random.Generator,
    ledger: pd.DataFrame,
    fraction: float
) -> pd.DataFrame:
    """Return a copy with inconsistent letter case in some categorical cells."""
    ledger = ledger.copy()
    n = int(len(ledger) * fraction)
    idx = rng.choice(len(ledger), size=n, replace=False)
    # I upper-case my category cells for the chosen rows
    for col in (ASSET_TYPE, CURRENCY):
        ledger.loc[idx, col] = ledger.loc[idx, col].astype(str).str.upper()
    return ledger


def inject_nulls(
    rng: np.random.Generator,
    ledger: pd.DataFrame,
    fraction: float
) -> pd.DataFrame:
    """Return a copy with nulls placed in the non-critical columns only."""
    ledger = ledger.copy()
    # I only blank out columns I marked as nullable, never amount or the keys
    for i in range(len(NULLABLE_COLUMNS)):
        col = NULLABLE_COLUMNS[i]
        n = int(len(ledger) * fraction)
        idx = rng.choice(len(ledger), size=n, replace=False)
        ledger.loc[idx, col] = np.nan
    return ledger


def inject_duplicates(
    rng: np.random.Generator,
    ledger: pd.DataFrame,
    fraction: float
) -> pd.DataFrame:
    """Return a copy enlarged with exact duplicate rows."""
    # I copy a fraction of the rows exactly and append them
    n = int(len(ledger) * fraction)
    idx = rng.choice(len(ledger), size=n, replace=False)
    duplicates = ledger.iloc[idx].copy()
    return pd.concat([ledger, duplicates], ignore_index=True)


def messify_headers(ledger: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with the clean column names replaced by messy headers."""
    # I rename my clean columns to messy display headers for ETL to fix later
    return ledger.rename(columns=MESSY_HEADERS)


def save_ledger(ledger: pd.DataFrame, output_path: str) -> None:
    """Write the ledger to a CSV file at the given path without an index."""
    # I make sure the target folder exists first
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    # I write my messy ledger to CSV, without the extra index column
    ledger.to_csv(output_path, index=False)


def main() -> None:
    """Run the full generation pipeline and write the messy ledger to disk."""
    # I create my single random generator
    rng = np.random.default_rng(SEED)

    # I build the clean ledger and check the invariant before any noise
    ledger = build_clean_ledger(rng)
    check_invariant(ledger, INVARIANT_TOLERANCE)

    # I add the noise in order: value noise first, duplicates last, then headers
    ledger = inject_whitespace(rng, ledger, WHITESPACE_FRACTION)
    ledger = inject_case_noise(rng, ledger, CASE_NOISE_FRACTION)
    ledger = inject_nulls(rng, ledger, NULL_FRACTION)
    ledger = inject_duplicates(rng, ledger, DUPLICATE_FRACTION)
    ledger = messify_headers(ledger)

    # I save the messy ledger for the ETL stage
    save_ledger(ledger, OUTPUT_CSV_PATH)


if __name__ == "__main__":
    main()