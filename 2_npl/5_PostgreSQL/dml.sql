SELECT * FROM npl_ratio.loans;
SELECT * FROM npl_ratio.clients;
SELECT * FROM npl_ratio.loans l LEFT JOIN npl_ratio.clients c ON l.client_id = c.client_id WHERE days_overdue >= 90;
# =====================================D==================================D====================================================

WITH marked_loans AS (
    SELECT 
        report_quarter,
        outstanding_amount,
        provision_amount,
        CASE WHEN days_overdue >= 90 THEN outstanding_amount ELSE 0 END AS npl_amount,
        CASE WHEN days_overdue >= 90 THEN provision_amount ELSE 0 END AS npl_provision
    FROM npl_ratio.loans
)
SELECT
    report_quarter,
    ROUND(SUM(npl_amount) / SUM(outstanding_amount) * 100, 1) AS npl_ratio_pct,
    ROUND(SUM(npl_provision) / SUM(npl_amount) * 100, 1) AS coverage_ratio_pct
FROM marked_loans
GROUP BY report_quarter
ORDER BY report_quarter;
# =====================================D==================================D====================================================

TRUNCATE npl_ratio.loans, npl_ratio.clients;