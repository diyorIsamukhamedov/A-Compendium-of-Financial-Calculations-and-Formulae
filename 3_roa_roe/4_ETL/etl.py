"""ETL: clean the messy gen-synthatic asset ledger."""

from pathlib import Path
import pandas as pd

# I read the messy file that my generator wrote, and I write the clean one next to it
#absolute
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
#in
MESSY_CSV_PATH = str(DATA_DIR / "1_assets_messy_v1.csv")
#out
CLEAN_CSV_PATH = str(DATA_DIR / "2_assets_clean_v1.csv")

# mapping the messy headers back to my clean snake_case names
HEADER_RENAME: dict[str,str] = {
    "Asset ID": "asset_id",
    "Report Date": "report_date",
    "Asset Type": "asset_type",
    "Currency": "currency",
    "Term Month": "term_month",
    "Interest Rate": "interest_rate",
    "Amount": "amount"
}

# the text columns I need to tidy
CATEGORICAL_COLUMNS: list[str] = ["asset_type", "currency"]

def extract(path: str) -> pd.DataFrame:
    """Read the messy CSV into a DataFrame."""
    # I read the messy ledger from disk
    return pd.read_csv(path)

def transform(ledger: pd.DataFrame) -> pd.DataFrame:
    """Clean the ledger by undoing each kind of noise the generator added."""
    # 1. I rename the messy headers back to my snake_case names
    ledger = ledger.rename(columns=HEADER_RENAME)

    # 2. I tidy the text columns: strip the spaces and lower-case them.
    # This undoes the whitespace noise and the case noise in one pass.
    for i in range(len(CATEGORICAL_COLUMNS)):
        col = CATEGORICAL_COLUMNS[i]
        ledger[col] = ledger[col].str.strip().str.lower()
        
    # 3. I fill the missing currency values with the most common currency
    most_common = ledger["currency"].mode()[0]
    ledger["currency"] = ledger["currency"].fillna(most_common)

    # 4. I drop the exact duplicate rows. This also brings each date's amount
    # sum back to its target, because the duplicates were double-counted (approximately 2%).
    ledger = ledger.drop_duplicates().reset_index(drop=True)

    return ledger

def load(ledger: pd.DataFrame, file_path: str) -> None:
    """Write the clean ledger to CSV"""
    # I write the clean ledger, without the extra index column
    ledger.to_csv(file_path, index=False)

def main() -> None:
    """Run the ETL pipeline"""
    #Extract
    ledger = extract(MESSY_CSV_PATH)
    rows_before = len(ledger)

    # Transform
    ledger = transform(ledger)
    rows_after= len(ledger)

    #Load 
    load(ledger, CLEAN_CSV_PATH)

    #print a summary so I can see the cleaning worked correctly
    print("rows before     :", rows_before)
    print("rows after      :", rows_after, "(removed:", rows_before - rows_after, ")")
    print("nulls left      :", int(ledger.isna().sum().sum()))
    print("per-date amount sums:")
    dates = sorted(ledger["report_date"].unique())
    for i in range(len(dates)):
        date = dates[i]
        total = ledger.loc[ledger["report_date"] == date, "amount"].sum()
        print("  ", date, ":", round(total, 2)) 

if __name__=="__main__":
    main()