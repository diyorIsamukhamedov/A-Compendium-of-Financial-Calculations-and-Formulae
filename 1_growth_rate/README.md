# Growth Rate

> **Disclaimer.** All datasets, financial figures, and business cases used in this repository are **fully synthetic** and created exclusively for educational purposes. They do not represent any real organisation, commercial bank, or actual market data. Any resemblance to real entities or transactions is coincidental.

---
 
## Overview
 
This repository contains a structured study of financial calculations and quantitative formulae, implemented through `Python`, `PostgreSQL`, `Microsoft Excel`, and applied mathematics.

The current edition is dedicated to the **Growth Rate** indicator. Each topic in the repository follows a uniform methodological cycle:
 
1. Theoretical foundations: definition, economic meaning, formula derivation.
2. Practical task with a step-by-step solution.
3. Reusable `Python` implementation of the formula.
4. Statistical analysis and visualisation in a `Jupyter Notebook`.
5. `SQL`-based implementation on a normalised schema in `PostgreSQL`.
6. `Excel` model replicating the same calculation for cross-validation.
7. Original handwritten notes preserved as scanned images.
All theory notes and task solutions inside the repository are provided in both English and Russian in parallel.
 
---
 
## Formula
 
```
ΔP = ((V₁ − V₀) / V₀) × 100%
```
 
Where:
* `V₀` is the value of the indicator in the base period.
* `V₁` is the value of the indicator in the reporting period.
* `ΔP` is the relative growth rate, expressed in percent.
The indicator reflects the dynamics of the value under study. A positive value indicates growth, a negative one indicates a decline. Unlike absolute increment (expressed in monetary or natural units), the growth rate allows for comparing the dynamics of indicators of different scales and conducting comparative analysis between periods, organisations, or market segments.
 
---
 
## Project Structure
 
```
├── requirements.txt
├── .gitignore
│
└── 1_growth_rate/
    ├── theory/                 Theoretical foundations (.md, RU + EN)
    │   └── growth_rate.md
    │
    ├── tasks/                  Tasks with step-by-step solutions (.md, RU + EN)
    │   └── task_01_deposit_portfolio.md
    │
    ├── python/
    │   └── formulas/           Reusable Python implementation of the formula
    │       └── growth_rate.py
    │
    ├── notebooks/              Jupyter notebook with final statistics
    │   │                       (imports functions from python/formulas/)
    │   └── 01_growth_rate_analysis.ipynb
    │
    ├── PostgreSQL/
    │   ├── DDL/                Schema and table creation scripts
    │   └── DML/                Analytical SQL queries
    │
    ├── excel/                  Excel model for cross-validation
    │   └── growth_rate.xlsx
    │
    ├── data/                   Synthetic datasets in CSV
    │
    ├── handwritten/            Scanned original handwritten notes
    │   └── growth_rate_page_01.jpg
    │
    ├── README.md
    └── docs/                   ERD diagrams, screenshots, supplementary materials
```
 
---
 
## How to Run
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/diyorIsamukhamedov/1_growth-rate.git
cd 1_growth-rate
```
 
### 2. Set Up Python Environment
 
```bash
python -m venv venv
source venv/bin/activate          # Linux / macOS
venv\Scripts\activate             # Windows
pip install -r requirements.txt
```
 
### 3. Initialise the PostgreSQL Database
 
Run the DDL scripts in your SQL IDE (DBeaver or psql):
 
```bash
\i 1_growth_rate/PostgreSQL/DDL/create_schema.sql
```
 
### 4. Open the Notebook
 
```bash
jupyter notebook
```
 
Open `1_growth_rate/notebooks/01_growth_rate_analysis.ipynb` to view the final statistical analysis.
 
---
 
## Example: Multi-Tool Implementation
 
**Python implementation** in `1_growth_rate/python/formulas/growth_rate.py`:
 
```python
def growth_rate(v0: float, v1: float) -> float:
    """
    Calculate the relative growth rate between two periods.
 
    :param v0: value of the indicator in the base period
    :param v1: value of the indicator in the reporting period
    :return: growth rate, %
    """
    if v0 == 0:
        raise ValueError("Base-period value cannot be zero.")
    return ((v1 - v0) / v0) * 100
```
 
**Notebook usage** in `1_growth_rate/notebooks/01_growth_rate_analysis.ipynb`:
 
```python
from python.formulas.growth_rate import growth_rate
 
# Retail deposit portfolio (synthetic data, UZS bn)
result = growth_rate(v0=1250, v1=1475)
print(f"Total portfolio growth rate: {result:.2f}%")
# Output: Total portfolio growth rate: 18.00%
```
 
**SQL implementation** in `1_growth_rate/PostgreSQL/DML/growth_rate.sql`:
 
```sql
-- Compute period-over-period growth rate for each indicator
WITH periods AS (
    SELECT
        indicator_name,
        SUM(CASE WHEN period_date = '2024-01-01' THEN value END) AS v0,
        SUM(CASE WHEN period_date = '2025-01-01' THEN value END) AS v1
    FROM growth_rate.indicators
    GROUP BY indicator_name
)
SELECT
    indicator_name,
    v0,
    v1,
    ROUND(((v1 - v0) / v0) * 100, 2) AS growth_rate_percent
FROM periods
WHERE v0 IS NOT NULL AND v0 <> 0;
```
 
---
 
## Handwritten Notes
 
Original handwritten notes are preserved in `1_growth_rate/handwritten/` as scanned images. These represent the initial draft stage of each topic before transcription into the structured digital format presented above. They are included as supplementary material to document the full learning process and may be useful for visualising step-by-step manual derivations alongside the formal Markdown notes in `theory/` and `tasks/`.
 
---
 
## Technologies Used
 
* `Python` (NumPy, Pandas, Matplotlib, Jupyter) for formula implementation and statistical analysis.
* `PostgreSQL` for database design and analytical SQL queries.
* `Microsoft Excel` for financial modelling and cross-validation of calculations.
* `DBeaver` as the SQL IDE and ERD generator.
* `Git` and `GitHub` for version control and public documentation.
* `Markdown` for bilingual theory notes and task solutions.
---
 
## Key Outcomes
 
| Objective | Approach | Outcome |
|---|---|---|
| Build a personal reference of financial formulas | Document each formula with theory, task, and solution in bilingual Markdown | Structured, searchable archive |
| Develop applied analytical skills in the FinTech sector | Solve realistic FinTech-sector tasks step-by-step on synthetic data | Strengthened applied competencies |
| Practise multi-tool implementation of the same calculation | Reproduce each formula in Python, SQL, and Excel | Results cross-validated across three environments |
| Preserve the full learning process | Store original handwritten notes alongside digital materials | Transparent record from manual draft to final implementation |
| Maintain a professional public portfolio | Clean code, documentation, and reproducible structure | Public-facing portfolio for recruiters |
 
---
 
## Author
 
Developed by: [Diyor Isamuxamedov](https://github.com/diyorIsamukhamedov/)