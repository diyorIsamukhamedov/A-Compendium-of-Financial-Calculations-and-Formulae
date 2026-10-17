# Задачи: ROA и ROE | Tasks: ROA and ROE

## Задача 1. Расчёт за 2024-Q4 | Task 1. Calculation for 2024-Q4

### Дано | Given

| Показатель | Начало | Конец | Среднее |
|---|---|---|---|
| Активы, млн сум | 11 600 | 12 400 | 12 000 |
| Капитал, млн сум | 1 420 | 1 580 | 1 500 |
| Чистая прибыль, млн сум | - | 60 | 60 × 4 = 240 |

| Indicator | Begin | End | Average |
|---|---|---|---|
| Assets, mln UZS | 11,600 | 12,400 | 12,000 |
| Equity, mln UZS | 1,420 | 1,580 | 1,500 |
| Net income, mln UZS | - | 60 | 60 × 4 = 240 |

ROA и ROE - годовые показатели, поэтому квартальную прибыль умножаем на 4.

ROA and ROE are annual metrics, so quarterly profit is multiplied by 4.

### Найти | Find

ROA, ROE, финансовый рычаг и проверку DuPont.

ROA, ROE, financial leverage and the DuPont check.

### Шаг 1. Расчёт ROA | Step 1. Calculating ROA

$$\text{Средние активы} = \frac{11\ 600 + 12\ 400}{2} = 12\ 000$$

$$\text{ROA} = \frac{60 \times 4}{12\ 000} \times 100\% = 2{,}00\%$$

$$\text{Average assets} = \frac{11{,}600 + 12{,}400}{2} = 12{,}000$$

$$\text{ROA} = \frac{60 \times 4}{12{,}000} \times 100\% = 2.00\%$$

Каждые 100 единиц активов приносят 2 единицы прибыли в год.

Every 100 units of assets earn 2 units of profit per year.

### Шаг 2. Расчёт ROE | Step 2. Calculating ROE

$$\text{Средний капитал} = \frac{1\ 420 + 1\ 580}{2} = 1\ 500$$

$$\text{ROE} = \frac{60 \times 4}{1\ 500} \times 100\% = 16{,}00\%$$

$$\text{Average equity} = \frac{1{,}420 + 1{,}580}{2} = 1{,}500$$

$$\text{ROE} = \frac{60 \times 4}{1{,}500} \times 100\% = 16.00\%$$

Каждые 100 единиц капитала акционеров приносят 16 единиц прибыли в год.

Every 100 units of shareholders' capital earn 16 units of profit per year.

### Шаг 3. Финансовый рычаг | Step 3. Financial leverage

$$\text{Рычаг} = \frac{12\ 000}{1\ 500} = 8{,}00$$

$$\text{Leverage} = \frac{12{,}000}{1{,}500} = 8.00$$

На каждую 1 единицу капитала приходится 8 единиц активов - банк работает на привлечённые деньги.

Each 1 unit of capital supports 8 units of assets - so the bank runs on borrowed money.

### Шаг 4. Проверка DuPont | Step 4. DuPont check

$$\text{ROE} = 2{,}00\% \times 8{,}00 = 16{,}00\%$$

$$\text{ROE} = 2.00\% \times 8.00 = 16.00\%$$

Декомпозиция сходится точно.

The decomposition reconciles exactly.

### Ответ | Answer

| Показатель | Значение |
|---|---|
| ROA | 2,00% |
| ROE | 16,00% |
| Финансовый рычаг | 8,00 |

| Indicator | Value |
|---|---|
| ROA | 2.00% |
| ROE | 16.00% |
| Financial leverage | 8.00 |

### Вывод | Conclusion

В 2024-Q4 ROA = 2,00%, финансовый рычаг = 8,00, ROE = 16,00%. ROE превышает ROA в 8 раз - это и есть финансовый рычаг. Декомпозиция DuPont сходится точно: 2,00% × 8,00 = 16,00%. Значения устойчивы для банка и говорят об эффективном использовании активов и капитала.

In 2024-Q4 ROA = 2.00%, financial leverage = 8.00 and ROE = 16.00%. ROE exceeds ROA eight times - this is the financial leverage. The DuPont decomposition reconciles exactly: 2.00% × 8.00 = 16.00%. The values are sound for a bank and point to efficient use of assets and capital.

## Задача 2. Динамика по кварталам | Task 2. Quarterly trend

### Дано | Given

Итоги активов на конец квартала берутся из реестра активов (сумма `amount` по дате). Капитал и прибыль берутся из таблицы `equity_income`. Для 2024-Q1 активы на начало (10 400) и капитал на начало (1 240) - входящие остатки на конец 2023-Q4.

End-of-quarter asset totals come from the asset ledger (the sum of `amount` per date). Equity and net income come from the `equity_income` table. For 2024-Q1, assets at the start (10,400) and equity at the start (1,240) are the opening balances at the end of 2023-Q4.

### Найти | Find

ROA, ROE и рычаг за каждый из шести кварталов.

ROA, ROE and leverage for each of the six quarters.

### Решение | Solution

Для каждого квартала применяются формулы из задачи 1. Активы на начало квартала равны активам на конец предыдущего квартала, капитал так же.

For each quarter the formulae from Task 1 are applied. Assets at the start of a quarter equal assets at the end of the previous quarter, and the same holds for equity.

| Квартал | Активы начало | Активы конец | Активы сред. | Капитал начало | Капитал конец | Капитал сред. | Прибыль кварт. | Прибыль год. | ROA | ROE | Рычаг |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-Q1 | 10 400 | 10 800 | 10 600 | 1 240 | 1 300 | 1 270 | 48 | 192 | 1,81% | 15,12% | 8,35 |
| 2024-Q2 | 10 800 | 11 200 | 11 000 | 1 300 | 1 360 | 1 330 | 51 | 204 | 1,85% | 15,34% | 8,27 |
| 2024-Q3 | 11 200 | 11 600 | 11 400 | 1 360 | 1 420 | 1 390 | 54 | 216 | 1,89% | 15,54% | 8,20 |
| 2024-Q4 | 11 600 | 12 400 | 12 000 | 1 420 | 1 580 | 1 500 | 60 | 240 | 2,00% | 16,00% | 8,00 |
| 2025-Q1 | 12 400 | 12 800 | 12 600 | 1 580 | 1 640 | 1 610 | 62 | 248 | 1,97% | 15,40% | 7,83 |
| 2025-Q2 | 12 800 | 13 200 | 13 000 | 1 640 | 1 700 | 1 670 | 63 | 252 | 1,94% | 15,09% | 7,78 |

| Quarter | Assets begin | Assets end | Assets avg. | Equity begin | Equity end | Equity avg. | Profit qtr. | Profit annual | ROA | ROE | Leverage |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-Q1 | 10,400 | 10,800 | 10,600 | 1,240 | 1,300 | 1,270 | 48 | 192 | 1.81% | 15.12% | 8.35 |
| 2024-Q2 | 10,800 | 11,200 | 11,000 | 1,300 | 1,360 | 1,330 | 51 | 204 | 1.85% | 15.34% | 8.27 |
| 2024-Q3 | 11,200 | 11,600 | 11,400 | 1,360 | 1,420 | 1,390 | 54 | 216 | 1.89% | 15.54% | 8.20 |
| 2024-Q4 | 11,600 | 12,400 | 12,000 | 1,420 | 1,580 | 1,500 | 60 | 240 | 2.00% | 16.00% | 8.00 |
| 2025-Q1 | 12,400 | 12,800 | 12,600 | 1,580 | 1,640 | 1,610 | 62 | 248 | 1.97% | 15.40% | 7.83 |
| 2025-Q2 | 12,800 | 13,200 | 13,000 | 1,640 | 1,700 | 1,670 | 63 | 252 | 1.94% | 15.09% | 7.78 |

### Вывод | Conclusion

ROE держится около 15% и достигает пика 16,00% в 2024-Q4. Рычаг плавно снижается с 8,35 до 7,78: капитал растёт быстрее активов, и банк становится менее зависим от привлечённых средств. Тождество DuPont выполняется в каждом квартале с точностью до округления, а в 2024-Q4 сходится точно.

ROE stays around 15% and peaks at 16.00% in 2024-Q4. Leverage declines steadily from 8.35 to 7.78: equity grows faster than assets, and the bank becomes less dependent on borrowed funds. The DuPont identity holds in every quarter up to rounding, and reconciles exactly in 2024-Q4.

## Задача 3 (FinTech). Конвейер данных | Task 3 (FinTech). Data pipeline

### Постановка | Statement

Построить конвейер, который рассчитывает ROA, ROE и рычаг по шести кварталам из синтетического реестра активов банка, и подтвердить результат тремя независимыми способами: SQL, Python и Excel.

Build a pipeline that calculates ROA, ROE and leverage across six quarters from a synthetic bank asset ledger, and confirm the result in three independent ways: SQL, Python and Excel.

### Входные данные | Input data

| Файл | Содержимое |
|---|---|
| `1_assets_messy_v1.csv` | Грязный реестр: 306 000 строк, грязные заголовки, пробелы, разный регистр, пропуски в валюте, около 2% точных дубликатов |
| `2_assets_clean_v1.csv` | Чистый реестр: 300 000 строк (6 кварталов по 50 000 активов) |
| `3_equity_income_v1.csv` | Капитал и прибыль: 6 строк, по одной на квартал |

| File | Contents |
|---|---|
| `1_assets_messy_v1.csv` | Messy ledger: 306,000 rows, messy headers, whitespace, inconsistent case, nulls in currency, about 2% exact duplicates |
| `2_assets_clean_v1.csv` | Clean ledger: 300,000 rows (6 quarters of 50,000 assets each) |
| `3_equity_income_v1.csv` | Equity and net income: 6 rows, one per quarter |

### Этапы | Stages

1. Генерация: синтетический реестр, в котором сумма `amount` по каждой дате точно равна итогу активов на конец квартала.
2. ETL: очистка заголовков, пробелов, регистра, заполнение пропусков валюты модой, удаление дубликатов. После очистки суммы по датам снова равны итогам.
3. PostgreSQL: схема `roa_roe`, таблицы `assets` и `equity_income`, загрузка через `COPY`.
4. Расчёт: ROA, ROE, рычаг и проверка DuPont в SQL, Python и Excel.

1. Generation: a synthetic ledger in which the sum of `amount` per date equals the end-of-quarter total assets exactly.
2. ETL: clean the headers, whitespace and case, fill missing currency with the mode, drop duplicates. After cleaning, the per-date sums equal the totals again.
3. PostgreSQL: schema `roa_roe`, tables `assets` and `equity_income`, loaded with `COPY`.
4. Calculation: ROA, ROE, leverage and the DuPont check in SQL, Python and Excel.

### Контрольные точки | Control points

- Суммы `amount` по датам: 10 800, 11 200, 11 600, 12 400, 12 800, 13 200.
- Строка 2024-Q4 во всех трёх расчётах: ROA 2,00%, ROE 16,00%, рычаг 8,00.
- SQL, Python и Excel дают одинаковые значения по всем шести кварталам.

- Sums of `amount` per date: 10,800, 11,200, 11,600, 12,400, 12,800, 13,200.
- The 2024-Q4 row in all three calculations: ROA 2.00%, ROE 16.00%, leverage 8.00.
- SQL, Python and Excel give identical values for all six quarters.
