import yfinance as yf
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_financial_data(ticker_symbol: str) -> dict:
    """Fetches financial statements from Yahoo Finance API."""
    logger.info(f"Fetching data for {ticker_symbol}...")
    try: