# Задача: качество кредитного портфеля / Task: Loan Portfolio Quality

## Условие / Task

Финтех-кредитор «DigitalLoan» отслеживает кредитный портфель за шесть кварталов. Нужно рассчитать NPL Ratio и Coverage Ratio по каждому кварталу и оценить динамику качества портфеля. Данные синтетические.

A fintech lender, "DigitalLoan", tracks its loan portfolio across six quarters. The task is to calculate the NPL ratio and coverage ratio for each quarter and assess the trend in portfolio quality. The data is synthetic.

## Данные / Data

Все суммы в миллиардах. / All amounts are in billions.

| Квартал | Портфель | NPL | Резервы |
|---|---|---|---|
| 2024-Q4 | 100 | 4,0 | 3,0 |
| 2025-Q1 | 110 | 5,5 | 4,0 |
| 2025-Q2 | 125 | 7,5 | 5,0 |
| 2025-Q3 | 140 | 9,8 | 6,0 |
| 2025-Q4 | 150 | 12,0 | 7,0 |
| 2026-Q1 | 160 | 14,4 | 8,0 |

| Quarter | Portfolio | NPL | Provisions |
|---|---|---|---|
| 2024-Q4 | 100 | 4.0 | 3.0 |
| 2025-Q1 | 110 | 5.5 | 4.0 |
| 2025-Q2 | 125 | 7.5 | 5.0 |
| 2025-Q3 | 140 | 9.8 | 6.0 |
| 2025-Q4 | 150 | 12.0 | 7.0 |
| 2026-Q1 | 160 | 14.4 | 8.0 |

## Решение / Solution

### NPL Ratio = (NPL / Портфель) × 100% / (NPL / Portfolio) × 100%

```
2024-Q4:  (4,0  / 100) × 100% = 4,0%      2024-Q4:  (4.0  / 100) × 100% = 4.0%
2025-Q1:  (5,5  / 110) × 100% = 5,0%      2025-Q1:  (5.5  / 110) × 100% = 5.0%
2025-Q2:  (7,5  / 125) × 100% = 6,0%      2025-Q2:  (7.5  / 125) × 100% = 6.0%
2025-Q3:  (9,8  / 140) × 100% = 7,0%      2025-Q3:  (9.8  / 140) × 100% = 7.0%
2025-Q4:  (12,0 / 150) × 100% = 8,0%      2025-Q4:  (12.0 / 150) × 100% = 8.0%
2026-Q1:  (14,4 / 160) × 100% = 9,0%      2026-Q1:  (14.4 / 160) × 100% = 9.0%
```

### Coverage Ratio = (Резервы / NPL) × 100% / (Provisions / NPL) × 100%

```
2024-Q4:  (3,0 / 4,0)  × 100% = 75,0%     2024-Q4:  (3.0 / 4.0)  × 100% = 75.0%
2025-Q1:  (4,0 / 5,5)  × 100% ≈ 72,7%     2025-Q1:  (4.0 / 5.5)  × 100% ≈ 72.7%
2025-Q2:  (5,0 / 7,5)  × 100% ≈ 66,7%     2025-Q2:  (5.0 / 7.5)  × 100% ≈ 66.7%
2025-Q3:  (6,0 / 9,8)  × 100% ≈ 61,2%     2025-Q3:  (6.0 / 9.8)  × 100% ≈ 61.2%
2025-Q4:  (7,0 / 12,0) × 100% ≈ 58,3%     2025-Q4:  (7.0 / 12.0) × 100% ≈ 58.3%
2026-Q1:  (8,0 / 14,4) × 100% ≈ 55,6%     2026-Q1:  (8.0 / 14.4) × 100% ≈ 55.6%
```

### Итоговая таблица / Summary table

| Квартал / Quarter | NPL Ratio | Coverage Ratio |
|---|---|---|
| 2024-Q4 | 4,0% / 4.0% | 75,0% / 75.0% |
| 2025-Q1 | 5,0% / 5.0% | 72,7% / 72.7% |
| 2025-Q2 | 6,0% / 6.0% | 66,7% / 66.7% |
| 2025-Q3 | 7,0% / 7.0% | 61,2% / 61.2% |
| 2025-Q4 | 8,0% / 8.0% | 58,3% / 58.3% |
| 2026-Q1 | 9,0% / 9.0% | 55,6% / 55.6% |

## Вывод / Conclusion

За шесть кварталов доля проблемных кредитов выросла с 4% до 9%, и портфель перешёл из зоны нормы в зону внимания. Одновременно покрытие резервами снизилось с 75% до 55,6%: резервы в абсолютном выражении росли, но их доля относительно проблемных кредитов падала, то есть NPL рос быстрее, чем банк наращивал резервы. Это двойной сигнал риска. Рекомендуется ужесточить кредитный скоринг, нарастить резервы и притормозить рост портфеля.

Over six quarters the share of non-performing loans rose from 4% to 9%, moving the portfolio from the normal zone into the watch zone. At the same time, reserve coverage fell from 75% to 55.6%: provisions grew in absolute terms, but their share relative to non-performing loans declined, meaning NPLs grew faster than the bank built reserves. This is a double risk signal. The recommended actions are to tighten credit scoring, increase provisions, and slow portfolio growth.