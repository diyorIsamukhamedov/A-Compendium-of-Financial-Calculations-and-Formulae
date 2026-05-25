-- Calculate the structural shift of the portfolio between two reporting dates.
-- Reproduces Step 4 of the handwritten notes.
-- For each part (FX, Sum) computes its share in the whole on both dates
-- and the change in share between the periods (in percentage points).
WITH portfolio_data AS (
	SELECT
		p.portfolio_name,
		i.indicator_code,
		o.report_date,
		o.value
	FROM growth_rate.observations o
	INNER JOIN growth_rate.portfolios p
		ON p.portfolio_id = o.portfolio_id
	INNER JOIN growth_rate.indicators i
		ON i.indicator_id = o.indicator_id
	WHERE p.portfolio_name = 'Retail Deposit Portfolio'
),
wholes AS (
	SELECT
		portfolio_name,
		report_date,
		value AS whole_value
	FROM portfolio_data
	WHERE indicator_code = 'total_portfolio'
),
parts AS (
	SELECT
		portfolio_name,
		indicator_code,
		report_date,
		value AS part_value
	FROM portfolio_data
	WHERE indicator_code IN ('fx_component', 'sum_component')
),
shares AS (
	SELECT
		parts.portfolio_name,
		parts.indicator_code,
		parts.report_date,
		ROUND((parts.part_value / wholes.whole_value) * 100, 2) AS share_percent
	FROM parts
	INNER JOIN wholes
		ON wholes.portfolio_name = parts.portfolio_name
		AND wholes.report_date = parts.report_date
)
SELECT
	portfolio_name,
	indicator_code,
	MAX(CASE WHEN report_date = '2024-01-01' THEN share_percent END) AS share_v0,
	MAX(CASE WHEN report_date = '2025-01-01' THEN share_percent END) AS share_v1,
	ROUND(
		MAX(CASE WHEN report_date = '2025-01-01' THEN share_percent END)
		- MAX(CASE WHEN report_date = '2024-01-01' THEN share_percent END),
		2
	) AS delta_pp
FROM shares
GROUP BY portfolio_name, indicator_code
ORDER BY indicator_code;
