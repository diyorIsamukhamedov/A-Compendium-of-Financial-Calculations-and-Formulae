CREATE SCHEMA IF NOT EXISTS npl_ratio;

DROP TABLE IF EXISTS npl_ratio.loans;
DROP TABLE IF EXISTS npl_ratio.clients;

-- Parent table
CREATE TABLE IF NOT EXISTS npl_ratio.clients (
	client_id INTEGER PRIMARY KEY, -- id comes from the CSV, not auto-generated
	client_name VARCHAR(100) NOT NULL,
	segment VARCHAR(20) NOT NULL CHECK(segment IN ('Retail', 'SME', 'Corporate')),
	industry VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS npl_ratio.loans (
	loan_id INTEGER PRIMARY KEY, -- id also comes from the CSV
	client_id INTEGER NOT NULL REFERENCES npl_ratio.clients(client_id),
	report_quarter VARCHAR(7) NOT NULL,
	currency CHAR(3) NOT NULL CHECK (currency IN ('UZS', 'USD')),
	outstanding_amount NUMERIC(15, 2) NOT NULL CHECK (outstanding_amount >= 0),
	days_overdue INTEGER NOT NULL DEFAULT 0 CHECK (days_overdue >= 0),
	provision_amount NUMERIC(15, 2) NOT NULL DEFAULT 0 CHECK (provision_amount >= 0)
);



























