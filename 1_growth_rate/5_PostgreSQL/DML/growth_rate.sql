-- Calculate the growth rate of each portfolio component between two reporting dates.
-- Reproduces Steps 1-3 of the handwritten notes.
-- Formula: ((v1 - v0) / v0) * 100, rounded to 2 decimal places.
WITH periods AS (
	SELECT
		p.portfolio_name,
		i.indicator_name,
		MAX(CASE WHEN o.report_date = '2024-01-01' THEN o.value END) AS v0,
		MAX(CASE WHEN o.report_date = '2025-01-01' THEN o.value END) AS v1
	FROM growth_rate.observations o
	INNER JOIN growth_rate.portfolios p
		ON p.portfolio_id = o.portfolio_id
	INNER JOIN growth_rate.indicators i
		ON i.indicator_id = o.indicator_id
	WHERE p.portfolio_name = 'Retail Deposit Portfolio'
	GROUP BY p.portfolio_name, i.indicator_name
)
SELECT
	portfolio_name,
	indicator_name,
	v0,
	v1,
	ROUND(((v1 - v0) / v0) * 100, 2) AS growth_rate_percent
FROM periods
ORDER BY indicator_name;