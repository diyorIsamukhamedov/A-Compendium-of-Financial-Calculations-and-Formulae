# Growth Rate

Исследование финансовых вычислений и количественных формул, реализованное на Python, PostgreSQL, Microsoft Excel и прикладной математике. Текущая редакция посвящена показателю темпа прироста и построена на едином цикле для каждой темы: рукописный конспект, расшифровка теории в Markdown, практическая задача с пошаговым решением, Python-класс, Jupyter-ноутбук, эквивалент на SQL в нормализованной схеме PostgreSQL и Excel-модель для кросс-валидации.

A study of financial calculations and quantitative formulae, implemented through Python, PostgreSQL, Microsoft Excel, and applied mathematics. The current edition is dedicated to the Growth Rate indicator and follows a single cycle for each topic: handwritten notes, transcribed theory in Markdown, a practical task with a step-by-step solution, a Python class, a Jupyter notebook, equivalent SQL on a normalised schema in PostgreSQL, and an Excel model for cross-validation.

Все данные и цифры в репозитории синтетические и созданы только в учебных целях, ориентированных на реальную практику в сфере FinTech. Теоретические конспекты и решения задач представлены параллельно на английском и русском языках.

All datasets and figures in the repository are synthetic and created for real-world FinTech oriented practice purposes only. Theory notes and task solutions are provided in both English and Russian in parallel.

## Формула / Formula

```
ΔP = ((V₁ - V₀) / V₀) × 100%
```

где:

V₀ - значение показателя в базисном периоде;
V₁ - значение показателя в отчётном периоде;
ΔP - темп прироста, %.

where:

V₀ - value of the indicator in the base period;
V₁ - value of the indicator in the reporting period;
ΔP - growth rate, %.

Показатель отражает динамику изучаемой величины: положительное значение свидетельствует о росте, отрицательное - о сокращении. В отличие от абсолютного прироста (выраженного в денежных или натуральных единицах), темп прироста позволяет сопоставлять динамику разномасштабных показателей и проводить сравнительный анализ между периодами, организациями или сегментами рынка.

The indicator reflects the dynamics of the value under study. A positive value indicates growth, a negative one indicates a decline. Unlike absolute increment (expressed in monetary or natural units), the growth rate allows for comparing the dynamics of indicators of different scales and conducting comparative analysis between periods, organisations, or market segments.

## Структура проекта / Project Structure

```
├── LICENCE
├── requirements.txt
├── .gitignore
│
└── 1_growth_rate/
    ├── 1_theory/                 Теория / Theory (RU + EN)
    │   └── growth_rate.md
    │
    ├── 2_tasks/                  Задачи / Tasks (RU + EN)
    │   └── task_01_deposit_portfolio.md
    │
    ├── 3_python/
    │   └── formulas/             Реализация на Python / Python implementation
    │       ├── growth_rate.py
    │       └── structural_shift.py
    │
    ├── 4_notebooks/              Jupyter-ноутбук / Jupyter notebook
    │   └── growth_rate_analysis.ipynb
    │
    ├── 5_PostgreSQL/
    │   ├── DDL/                  Создание схемы / Schema scripts
    │   └── DML/                  Аналитические запросы / Analytical queries
    │
    ├── excel/                    Excel-модель / Excel model
    │   └── growth_rate.xlsx
    │
    ├── data/                     Синтетические данные / Synthetic datasets (CSV)
    │
    ├── handwritten/              Рукописные конспекты / Handwritten notes
    │
    └── docs/                     ERD-диаграммы и доп. материалы / ERD diagrams and supplementary materials
    ├── README.md
```

## Как запустить / How to Run

Склонировать репозиторий:

Clone the repository:

```bash
git clone https://github.com/diyorIsamukhamedov/1_growth-rate.git
cd 1_growth-rate
```

Настроить виртуальное окружение Python:

Set up the Python environment:

```bash
python -m venv venv
source venv/bin/activate          # Linux / macOS
venv\Scripts\activate             # Windows
pip install -r requirements.txt
```
Если venv не запускается, то применить:
```
pip3 install ipykernel notebook pandas # Linux / macOS
python3 -m ipykernel install --user --name=venv --display-name "your_venv_name"
```

Инициализировать схему PostgreSQL в DBeaver или psql:

Initialise the PostgreSQL schema in DBeaver or psql:

```bash
\i 1_growth_rate/5_PostgreSQL/DDL/create_schema.sql
```

Открыть ноутбук:

Open the notebook:

```bash
jupyter notebook
```

Затем открыть `1_growth_rate/4_notebooks/growth_rate_analysis.ipynb`.

Then open `1_growth_rate/4_notebooks/growth_rate_analysis.ipynb`.

## Пример / Example

Реализация на Python в `1_growth_rate/3_python/formulas/growth_rate.py`:

Python implementation in `1_growth_rate/3_python/formulas/growth_rate.py`:

```python
class GrowthRate:
    """Represents a growth rate calculation between two periods."""

    def __init__(self, v0: float, v1: float, name: str) -> None:
        if v0 == 0:
            raise ValueError("Base-period value cannot be zero.")

        self.v0 = v0
        self.v1 = v1
        self.name = name

    def percentage(self) -> float:
        return ((self.v1 - self.v0) / self.v0) * 100
```

Использование:

Usage:

```python
total = GrowthRate(v0=1250, v1=1475, name="Total Portfolio")
print(f"{total.name}: {total.percentage():+.2f}%")
# Output: Total Portfolio: +18.00%
```

Эквивалент на SQL в `1_growth_rate/5_PostgreSQL/DML/growth_rate.sql`:

SQL equivalent in `1_growth_rate/5_PostgreSQL/DML/growth_rate.sql`:

```sql
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

## Рукописные конспекты / Handwritten Notes

Оригинальные рукописные конспекты хранятся в `1_growth_rate/handwritten/` в виде отсканированных изображений. Они отражают этап ручной проработки темы до её перевода в Markdown и в режим имплементации в кодовом (цифровом) виде.

Original handwritten notes are kept in `1_growth_rate/handwritten/` as scanned images. They reflect the manual draft stage before transcription into Markdown.

## Технологии / Technologies

Python (NumPy, Pandas, Matplotlib, Jupyter), PostgreSQL, Microsoft Excel, DBeaver, Git/GitHub, Markdown.
---
Вывод / Conclusion
Совокупный розничный депозитный портфель банка продемонстрировал положительную динамику (+18%), однако рост обеспечен исключительно сумовой составляющей (+27,42%) на фоне сокращения валютной части (-9,38%). Зафиксирован структурный сдвиг в сторону девалютизации (десолларизации) портфеля: доля валютных депозитов снизилась на 5,94 п.п. Подобная динамика характерна для текущего этапа реформ банковского сектора Узбекистана и согласуется с политикой Центрального банка РУз, направленной на повышение привлекательности сумовых сбережений (через ставки, инструменты страхования вкладов и валютную либерализацию).

The bank's total retail deposit portfolio demonstrated positive dynamics (+18%); however, growth was driven exclusively by the sum-denominated component (+27.42%) against a contraction of the FX component (-9.38%). A structural shift towards portfolio de-dollarisation has been recorded: the share of FX deposits declined by 5.94 percentage points. Such dynamics are consistent with the current stage of banking sector reform in Uzbekistan and align with the policy of the Central Bank of the Republic of Uzbekistan aimed at enhancing the attractiveness of sum-denominated savings (through interest rates, deposit insurance instruments, and currency liberalisation).

## Автор / Author

[Diyor Isamuxamedov](https://github.com/diyorIsamukhamedov/)