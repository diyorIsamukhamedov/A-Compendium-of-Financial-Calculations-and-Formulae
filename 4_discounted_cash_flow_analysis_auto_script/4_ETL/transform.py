import pandas as pd
import numpy as np

def clean_and_combine_statements(raw_data: dict, ticker: str) -> pd.DataFrame:
    """Transforms raw yfinance data into a normalized DataFrame matching our DB schema."""
    if not raw_data:
        return pd.DataFrame()
        
    inc = raw_data['income_statement'].T
    bs = raw_data['balance_sheet'].T
    cf = raw_data['cash_flow'].T
    
    # Basic data alignment by index (Date)
    df = pd.concat([inc, bs, cf], axis=1)
    df = df.loc[:,~df.columns.duplicated()] # Remove duplicate columns
    
    df['ticker'] = ticker
    df['fiscal_year'] = df.index.year
    
    columns_mapping = {
        'Total Revenue': 'revenue',
        'Cost Of Revenue': 'cogs',
        'Gross Profit': 'gross_profit',
        'Operating Expense': 'operating_expenses',
        'EBIT': 'ebit',
        'Interest Expense': 'interest_expense',
        'Tax Provision': 'tax_expense',
        'Net Income': 'net_income',
        'Total Assets': 'total_assets',
        'Total Liabilities Net Minority Interest': 'total_liabilities',
        'Stockholders Equity': 'total_equity',
        'Cash And Cash Equivalents': 'cash_and_equivalents',
        'Current Debt': 'short_term_debt',
        'Long Term Debt': 'long_term_debt',
        'Depreciation And Amortization': 'depreciation_and_amortization',
        'Capital Expenditure': 'capital_expenditure'
    }
    
    transformed_df = pd.DataFrame()
    transformed_df['ticker'] = df['ticker']
    transformed_df['fiscal_year'] = df['fiscal_year']
    
    for yf_col, db_col in columns_mapping.items():
        transformed_df[db_col] = df.get(yf_col, 0.0)
            
    # Calculate NWC (Net Working Capital approximation)
    total_ca = df.get('Total Current Assets', 0)
    total_cl = df.get('Total Current Liabilities', 0)
    cash = transformed_df.get('cash_and_equivalents', 0)
    st_debt = transformed_df.get('short_term_debt', 0)
    
    if 'Total Current Assets' in df.columns and 'Total Current Liabilities' in df.columns:
        transformed_df['net_working_capital'] = (total_ca - cash) - (total_cl - st_debt)
    else:
        transformed_df['net_working_capital'] = 0.0
        
    return transformed_df.reset_index(drop=True)