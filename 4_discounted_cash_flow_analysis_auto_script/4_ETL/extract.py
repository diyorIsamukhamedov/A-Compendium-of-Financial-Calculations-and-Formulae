import yfinance as yf
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_financial_data(ticker_symbol: str) -> dict:
    """Fetches financial statements from Yahoo Finance API."""
    logger.info(f"Fetching data for {ticker_symbol}...")
    try:
        ticker = yf.Ticker(ticker_symbol)
        
        income_stmt = ticker.financials
        balance_sheet = ticker.balance_sheet
        cash_flow = ticker.cashflow
        
        if income_stmt.empty or balance_sheet.empty or cash_flow.empty:
            logger.warning(f"Incomplete data for {ticker_symbol}")
            return None
            
        return {
            'income_statement': income_stmt,
            'balance_sheet': balance_sheet,
            'cash_flow': cash_flow
        }
    except Exception as e:
        logger.error(f"Error fetching data for {ticker_symbol}: {e}")
        return None