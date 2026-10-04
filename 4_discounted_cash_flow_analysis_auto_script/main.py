import argparse
import yfinance as yf
from src.extract import fetch_financial_data
from src.transform import clean_and_combine_statements
from src.dcf_model import DCFModel
from src.load import get_db_engine, load_financials_to_db, load_valuation_to_db

def main(ticker_symbol: str, wacc: float, growth_rate: float):
    print(f"--- Starting DCF Analysis for {ticker_symbol} ---")
    
    raw_data = fetch_financial_data(ticker_symbol)
    if not raw_data:
        print("Failed to fetch data.")
        return
        
    clean_df = clean_and_combine_statements(raw_data, ticker_symbol)
    print(f"Transformed data: {len(clean_df)} years of history.")
    
    model = DCFModel(wacc=wacc, terminal_growth_rate=growth_rate)
    hist_metrics_df = model.calculate_historical_metrics(clean_df)
    
    ticker_info = yf.Ticker(ticker_symbol).info
    current_price = ticker_info.get('currentPrice', ticker_info.get('regularMarketPrice', 0))
    shares_out = ticker_info.get('sharesOutstanding', 0)
    
    valuation_results = model.project_and_value(hist_metrics_df, current_price, shares_out)
    
    if "error" in valuation_results:
        print(f"Valuation Error: {valuation_results['error']}")
        return
        
    print("\n--- VALUATION RESULTS ---")
    print(f"Implied Share Price: ${valuation_results['implied_share_price']:.2f}")
    print(f"Current Market Price: ${valuation_results['current_market_price']:.2f}")
    print(f"Upside/Downside: {valuation_results['upside_downside_pct']*100:.2f}%")
    
    # engine = get_db_engine()
    # load_financials_to_db(clean_df, engine)
    # load_valuation_to_db(ticker_symbol, valuation_results, engine)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", type=str, default="AAPL")
    parser.add_argument("--wacc", type=float, default=0.09)
    parser.add_argument("--growth", type=float, default=0.02)
    
    args = parser.parse_args()
    main(args.ticker, args.wacc, args.growth)