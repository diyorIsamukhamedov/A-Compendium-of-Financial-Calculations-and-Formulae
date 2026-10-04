# math core

import pandas as pd
import numpy as np
from typing import Dict

class DCFModel:
    def __init__(self, wacc: float, terminal_growth_rate: float, forecast_years: int = 5):
        self.wacc = wacc
        self.g = terminal_growth_rate
        self.forecast_years = forecast_years
        
    def calculate_historical_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.sort_values('fiscal_year').reset_index(drop=True)
        
        # Tax Rate (capped at 35%)
        df['tax_rate'] = np.where(df['ebit'] > 0, df['tax_expense'] / df['ebit'], 0)
        df['tax_rate'] = df['tax_rate'].clip(lower=0, upper=0.35)
        
        df['nopat'] = df['ebit'] * (1 - df['tax_rate'])
        df['delta_nwc'] = df['net_working_capital'].diff().fillna(0)
        
        capex_adj = np.where(df['capital_expenditure'] < 0, df['capital_expenditure'], -df['capital_expenditure'])
        
        df['fcff'] = df['nopat'] + df['depreciation_and_amortization'] + capex_adj - df['delta_nwc']
        df['revenue_growth_rate'] = df['revenue'].pct_change().fillna(0)
        df['ebit_margin'] = np.where(df['revenue'] > 0, df['ebit'] / df['revenue'], 0)
        
        return df

    def project_and_value(self, historical_df: pd.DataFrame, current_price: float, shares_out: float) -> Dict:
        if historical_df.empty or len(historical_df) < 2:
            return {"error": "Not enough historical data"}
            
        recent = historical_df.iloc[-1]
        
        # Projections based on historical averages
        avg_rev_growth = historical_df['revenue_growth_rate'].mean()
        avg_ebit_margin = historical_df['ebit_margin'].mean()
        avg_tax_rate = historical_df['tax_rate'].mean()
        da_pct = (historical_df['depreciation_and_amortization'] / historical_df['revenue']).mean()
        capex_pct = (np.abs(historical_df['capital_expenditure']) / historical_df['revenue']).mean()
        nwc_pct = (historical_df['net_working_capital'] / historical_df['revenue']).mean()
        
        projected_fcff = []
        last_rev = recent['revenue']
        last_nwc = recent['net_working_capital']
        
        # 1. Forecast Period
        for year in range(1, self.forecast_years + 1):
            rev = last_rev * (1 + avg_rev_growth)
            ebit = rev * avg_ebit_margin
            nopat = ebit * (1 - avg_tax_rate)
            da = rev * da_pct
            capex = -(rev * capex_pct)
            nwc = rev * nwc_pct
            delta_nwc = nwc - last_nwc
            
            fcff = nopat + da + capex - delta_nwc
            projected_fcff.append(fcff)
            last_rev, last_nwc = rev, nwc
            
        # 2. Discount Forecasted FCFF
        pv_fcff = sum([fcff / ((1 + self.wacc) ** t) for t, fcff in enumerate(projected_fcff, 1)])
        
        # 3. Terminal Value
        terminal_fcff = projected_fcff[-1] * (1 + self.g)
        terminal_value = terminal_fcff / (self.wacc - self.g) if self.wacc > self.g else 0
        pv_tv = terminal_value / ((1 + self.wacc) ** self.forecast_years)
        
        # 4. Valuation
        enterprise_value = pv_fcff + pv_tv
        net_debt = recent['short_term_debt'] + recent['long_term_debt'] - recent['cash_and_equivalents']
        equity_value = enterprise_value - net_debt
        
        implied_share_price = equity_value / shares_out if shares_out > 0 else 0
        upside = (implied_share_price / current_price) - 1 if current_price > 0 else 0
        
        return {
            'wacc': self.wacc, 'terminal_growth_rate': self.g,
            'enterprise_value': enterprise_value, 'equity_value': equity_value,
            'shares_outstanding': shares_out, 'implied_share_price': implied_share_price,
            'current_market_price': current_price, 'upside_downside_pct': upside
        }