import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_engine():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db = os.getenv('DB_NAME')
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

def load_financials_to_db(df: pd.DataFrame, engine):
    if df.empty: return
    try:
        df.to_sql('financial_statements', engine, if_exists='append', index=False)
    except Exception as e:
        print(f"Error loading financials: {e}")

def load_valuation_to_db(ticker: str, valuation: dict, engine):
    val_df = pd.DataFrame([valuation])
    val_df['ticker'] = ticker
    val_df['valuation_date'] = pd.Timestamp.now().date()
    try:
        val_df.to_sql('dcf_valuations', engine, if_exists='append', index=False)
    except Exception as e:
        print(f"Error loading valuation: {e}")