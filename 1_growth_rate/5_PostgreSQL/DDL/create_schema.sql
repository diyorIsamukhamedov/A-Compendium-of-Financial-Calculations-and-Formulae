-- Create a new database for the growth rate analysis
CREATE DATABASE growth_rate
	WITH OWNER = postgres	-- owner of the database
	ENCODING = 'UTF8'		-- encoding to support international text
	TEMPLATE = template0	-- base template for a clean database
    CONNECTION LIMIT = -1;	-- unlimited connections allowed

CREATE SCHEMA IF NOT EXISTS growth_rate;

DROP TABLE IF EXISTS growth_rate.observations;
DROP TABLE IF EXISTS growth_rate.portfolios;
DROP TABLE IF EXISTS growth_rate.indicators;

CREATE TABLE IF NOT EXISTS growth_rate.portfolios (
    portfolio_id INT PRIMARY KEY NOT NULL,
    portfolio_name VARCHAR(255) NOT NULL UNIQUE,
	description TEXT	-- short description of the portfolio
);
 
CREATE TABLE IF NOT EXISTS growth_rate.indicators (
	indicator_id INT PRIMARY KEY NOT NULL,
	indicator_code VARCHAR(50) NOT NULL UNIQUE,	
	indicator_name VARCHAR(255) NOT NULL
);
 
-- Table: observations (stores indicator values per portfolio per reporting date)
CREATE TABLE IF NOT EXISTS growth_rate.observations (
	observation_id INT PRIMARY KEY NOT NULL,
	portfolio_id INT,			-- reference to the portfolio
	indicator_id INT,			-- reference to the indicator
	report_date DATE NOT NULL,	-- reporting date (e.g., 2024-01-01)
	value NUMERIC(18, 2) NOT NULL,
	unit VARCHAR(20) NOT NULL DEFAULT 'UZS bn',
	currency VARCHAR(10) NOT NULL DEFAULT 'UZS',
	CONSTRAINT fk_observations_portfolio
		FOREIGN KEY (portfolio_id)
		REFERENCES growth_rate.portfolios (portfolio_id)
		ON DELETE CASCADE	-- if portfolio is deleted, remove its observations too
		ON UPDATE CASCADE,	-- if portfolio_id changes, update observations accordingly
	CONSTRAINT fk_observations_indicator
		FOREIGN KEY (indicator_id)
		REFERENCES growth_rate.indicators (indicator_id)
		ON DELETE CASCADE	-- if indicator is deleted, remove its observations too
		ON UPDATE CASCADE,	-- if indicator_id changes, update observations accordingly
	CONSTRAINT uq_observation
		UNIQUE (portfolio_id, indicator_id, report_date)	-- no duplicate observations
);

-- Seed data: portfolios
INSERT INTO growth_rate.portfolios (portfolio_id, portfolio_name, description) VALUES
	(1, 'Retail Deposit Portfolio', 'Synthetic retail deposit portfolio of a commercial bank');
 
-- Seed data: indicators
INSERT INTO growth_rate.indicators (indicator_id, indicator_code, indicator_name) VALUES
	(1, 'total_portfolio', 'Total portfolio'),
	(2, 'fx_component',    'Foreign currency component'),
	(3, 'sum_component',   'Sum-denominated component');
 
-- Seed data: observations (synthetic data for 01.01.2024 and 01.01.2025)
INSERT INTO growth_rate.observations (observation_id, portfolio_id, indicator_id, report_date, value) VALUES
	(1, 1, 1, '2024-01-01', 1250),
	(2, 1, 2, '2024-01-01', 320),
	(3, 1, 3, '2024-01-01', 930),
	(4, 1, 1, '2025-01-01', 1475),
	(5, 1, 2, '2025-01-01', 290),
	(6, 1, 3, '2025-01-01', 1185);
 











