-- Create schema inside the database (to organise all tables under one namespace)
CREATE SCHEMA IF NOT EXISTS roa_roe;
-- ================================================================================

-- Table: assets
-- One row per asset position from the clean ledger.

/*
	Drop existing table(s) if they exist inside schema "roa_roe"
	This ensures the script can be re-run without conflicts.
	The order is chosen carefully to avoid foreign key dependency issues.
*/
DROP TABLE IF EXISTS roa_roe.assets;

CREATE TABLE roa_roe.assets (
	asset_id INTEGER PRIMARY KEY,													
	report_date VARCHAR(7) NOT NULL CHECK (report_date ~ '^\d{4}-Q[1-4]$'),			-- quarter label, e.g. 2024-Q4
	asset_type VARCHAR(20) NOT NULL CHECK (asset_type IN ('loan', 'cash', 'security', 'interbank')),	
	currency VARCHAR(3) NOT NULL CHECK (currency IN ('uzs', 'usd', 'eur')),			
	term_months INTEGER NOT NULL CHECK (term_months BETWEEN 1 AND 120),				-- matches TERM_MIN/TERM_MAX
	interest_rate NUMERIC(5, 2) NOT NULL,											-- 2 decimals, matches RATE_DP
	amount NUMERIC(18, 6) NOT NULL													-- 6 decimals, matches MONEY_SCALE_DP
);
-- ================================================================================