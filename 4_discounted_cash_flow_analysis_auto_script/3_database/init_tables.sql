-- Create a new database
CREATE DATABASE IF NOT EXISTS discounted_cash_flow_analysis
    WITH OWNER = postgres	-- owner of the database
	ENCODING = 'UTF8'		-- encoding to support international text
	TEMPLATE = template0	-- base template for a clean database
    CONNECTION LIMIT = -1;	-- unlimitted connections allowed

-- Create schema inside the database (to organise all tables under one namespace)
CREATE SCHEMA IF NOT EXISTS dcf_schema;

/*
	Drop existing tables if they exist inside schema "project_budgeting"
	This ensures the script can be re-run without conflicts.
	The order is chosen carefully to avoid foreign key dependency issues.
*/
DROP TABLE IF EXISTS dcf_schema.companies CASCADE;
DROP TABLE IF EXISTS dcf_schema.financial_statements CASCADE;
DROP TABLE IF EXISTS dcf_schema.historical_metrics CASCADE;
DROP TABLE IF EXISTS dcf_schema.dcf_valuations CASCADE;

-- Table 1: Companies (Tickers and basic information)
CREATE TABLE companies (
    ticker VARCHAR(10) PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    sector VARCHAR(100),
    industry VARCHAR(100),
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 2: Financial Statements (Raw data from Income Statement, Balance Sheet, Cash Flow)
-- Storing annual data
CREATE TABLE financial_statements (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) REFERENCES companies(ticker),
    fiscal_year INT NOT NULL,
    revenue NUMERIC(20, 2),
    cogs NUMERIC(20, 2),
    gross_profit NUMERIC(20, 2),
    operating_expenses NUMERIC(20, 2),
    ebit NUMERIC(20, 2),
    interest_expense NUMERIC(20, 2),
    tax_expense NUMERIC(20, 2),
    net_income NUMERIC(20, 2),
    total_assets NUMERIC(20, 2),
    total_liabilities NUMERIC(20, 2),
    total_equity NUMERIC(20, 2),
    cash_and_equivalents NUMERIC(20, 2),
    short_term_debt NUMERIC(20, 2),
    long_term_debt NUMERIC(20, 2),
    depreciation_and_amortization NUMERIC(20, 2),
    capital_expenditure NUMERIC(20, 2),
    net_working_capital NUMERIC(20, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (ticker, fiscal_year)
);

-- Table 3: Derived Metrics (Calculated historical metrics like FCF, Margins, Growth)
CREATE TABLE historical_metrics (
    id SERIAL PRIMARY KEY,
    statement_id INT REFERENCES financial_statements(id),
    revenue_growth_rate NUMERIC(10, 4),
    ebit_margin NUMERIC(10, 4),
    tax_rate NUMERIC(10, 4),
    nopat NUMERIC(20, 2),
    fcff NUMERIC(20, 2), -- Free Cash Flow to Firm
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 4: DCF Valuation Results (The final output of the model)
CREATE TABLE dcf_valuations (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) REFERENCES companies(ticker),
    valuation_date DATE NOT NULL,
    wacc NUMERIC(10, 4),
    terminal_growth_rate NUMERIC(10, 4),
    enterprise_value NUMERIC(20, 2),
    equity_value NUMERIC(20, 2),
    shares_outstanding NUMERIC(20, 2),
    implied_share_price NUMERIC(10, 2),
    current_market_price NUMERIC(10, 2),
    upside_downside_pct NUMERIC(10, 4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);