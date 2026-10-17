# Задачи: линейная регрессия | Tasks: linear regression

## Задача 1 (FinTech). Регрессия на выборке из 5 активов | Task 1 (FinTech). Regression on a sample of 5 assets

### Постановка | Statement

В реестре активов банка предсказываем сумму актива по его процентной ставке методом линейной регрессии. Берём выборку из 5 активов, строим линейную модель, затем оцениваем её по $R^2$.

In the bank's asset ledger we predict an asset's amount from its interest rate using linear regression. We take a sample of 5 assets, build a linear model and then evaluate it with $R^2$.

$$\hat{y} = b_0 + b_1 x$$

$x$ - ставка (признак), $y$ - реальная сумма, $\hat{y}$ - предсказанная сумма.

$x$ is the rate (feature), $y$ is the actual amount, $\hat{y}$ is the predicted amount.

### Дано | Given

| asset_id | Ставка, % \| Rate, % | Сумма, млн \| Amount, mln |
|---|---|---|
| 1 | 10 | 380 |
| 2 | 11 | 300 |
| 3 | 12 | 260 |
| 4 | 13 | 300 |
| 5 | 14 | 260 |

### Шаг 1. Средние | Step 1. Means

$$\bar{x} = \frac{10 + 11 + 12 + 13 + 14}{5} = \frac{60}{5} = 12$$

$$\bar{y} = \frac{380 + 300 + 260 + 300 + 260}{5} = \frac{1\ 500}{5} = 300$$

$$\bar{y} = \frac{380 + 300 + 260 + 300 + 260}{5} = \frac{1{,}500}{5} = 300$$

$\bar{x}$ и $\bar{y}$ - средние значения ставки и суммы по выборке.

$\bar{x}$ and $\bar{y}$ are the mean rate and the mean amount over the sample.

### Шаг 2. Отклонения от среднего | Step 2. Deviations from the mean

Для каждого актива: $(x - \bar{x})$, $(y - \bar{y})$, их произведение и квадрат $(x - \bar{x})$.

For each asset: $(x - \bar{x})$, $(y - \bar{y})$, their product and the square of $(x - \bar{x})$.

| $x$ | $y$ | $x - \bar{x}$ | $y - \bar{y}$ | $(x - \bar{x})(y - \bar{y})$ | $(x - \bar{x})^2$ |
|---|---|---|---|---|---|
| 10 | 380 | -2 | 80 | -160 | 4 |
| 11 | 300 | -1 | 0 | 0 | 1 |
| 12 | 260 | 0 | -40 | 0 | 0 |
| 13 | 300 | 1 | 0 | 0 | 1 |
| 14 | 260 | 2 | -40 | -80 | 4 |
| $\sum$ | | | | -240 | 10 |

### Шаг 3. Наклон | Step 3. Slope

$$b_1 = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sum (x - \bar{x})^2} = \frac{-240}{10} = -24$$

Каждый +1% к ставке - сумма в среднем меньше на 24 млн сум.

Each +1% in the rate means about 24 mln UZS less on average.

### Шаг 4. Сдвиг | Step 4. Intercept

$$b_0 = \bar{y} - b_1 \bar{x} = 300 - (-24) \times 12 = 300 + 288 = 588$$

$b_0$ - высота, на которой линия пересекает ось, то есть $\hat{y}$ при ставке 0.

$b_0$ is the height where the line crosses the axis, that is $\hat{y}$ at a rate of 0.

### Шаг 5. Уравнение модели | Step 5. Model equation

$$\hat{y} = 588 - 24 \times \text{ставка}$$

$$\hat{y} = 588 - 24 \times \text{rate}$$

### Шаг 6. Предсказания | Step 6. Predictions

| Ставка \| Rate | $\hat{y} = 588 - 24 \times x$ |
|---|---|
| 10 | 588 - 24 × 10 = 348 |
| 11 | 588 - 24 × 11 = 324 |
| 12 | 588 - 24 × 12 = 300 |
| 13 | 588 - 24 × 13 = 276 |
| 14 | 588 - 24 × 14 = 252 |

Подставили каждую ставку в уравнение и получили предсказание $\hat{y}$.

I substituted each rate into the equation and got the prediction $\hat{y}$.

### Шаг 7. Остатки | Step 7. Residuals

Остаток = факт - предсказание = $y - \hat{y}$.

Residual = actual - prediction = $y - \hat{y}$.

| Сумма $y$ \| Amount $y$ | Предсказание $\hat{y}$ \| Prediction $\hat{y}$ | Остаток \| Residual $(y - \hat{y})$ |
|---|---|---|
| 380 | 348 | 32 |
| 300 | 324 | -24 |
| 260 | 300 | -40 |
| 300 | 276 | 24 |
| 260 | 252 | 8 |

### Шаг 8. Оценка $R^2$ | Step 8. Scoring $R^2$

$$SS_{\text{ост}} = \sum (y - \hat{y})^2 = 32^2 + 24^2 + 40^2 + 24^2 + 8^2 = 1\ 024 + 576 + 1\ 600 + 576 + 64 = 3\ 840$$

$$SS_{\text{общ}} = \sum (y - \bar{y})^2 = 80^2 + 0 + 40^2 + 0 + 40^2 = 6\ 400 + 1\ 600 + 1\ 600 = 9\ 600$$

$$R^2 = 1 - \frac{3\ 840}{9\ 600} = 1 - 0{,}4 = 0{,}6$$

$$SS_{\text{res}} = \sum (y - \hat{y})^2 = 32^2 + 24^2 + 40^2 + 24^2 + 8^2 = 1{,}024 + 576 + 1{,}600 + 576 + 64 = 3{,}840$$

$$SS_{\text{tot}} = \sum (y - \bar{y})^2 = 80^2 + 0 + 40^2 + 0 + 40^2 = 6{,}400 + 1{,}600 + 1{,}600 = 9{,}600$$

$$R^2 = 1 - \frac{3{,}840}{9{,}600} = 1 - 0.4 = 0.6$$

### Итоговая таблица | Summary table

| Ставка, % \| Rate, % | Факт $y$ \| Actual $y$ | Модель $\hat{y}$ \| Model $\hat{y}$ | Остаток \| Residual |
|---|---|---|---|
| 10 | 380 | 348 | 32 |
| 11 | 300 | 324 | -24 |
| 12 | 260 | 300 | -40 |
| 13 | 300 | 276 | 24 |
| 14 | 260 | 252 | 8 |

Модель: $\hat{y} = 588 - 24x$, $R^2 = 0{,}6$.

Model: $\hat{y} = 588 - 24x$, $R^2 = 0.6$.

### Вывод | Conclusion

Линейная регрессия нашла прямую, которая по ставке предсказывает сумму актива. $R^2 = 0{,}6$: модель объясняет 60% разброса суммы. Связь обратная: чем выше ставка, тем меньше актив.

Linear regression found the line that predicts an asset's amount from its rate. $R^2 = 0.6$: the model explains 60% of the variation. The relationship is inverse: the higher the rate, the smaller the asset.

## Задача 2 (FinTech). Регрессия на полном реестре | Task 2 (FinTech). Regression on the full ledger

### Постановка | Statement

На всех 300 000 активах чистого реестра предсказать сумму актива по ставке и сроку. Коэффициенты находит scikit-learn тем же методом наименьших квадратов, что и в задаче 1.

On all 300,000 assets of the clean ledger, predict an asset's amount from its rate and term. scikit-learn finds the coefficients by the same least-squares method as in Task 1.

$$\hat{y} = b_0 + b_1 \times \text{ставка} + b_2 \times \text{срок}$$

$$\hat{y} = b_0 + b_1 \times \text{rate} + b_2 \times \text{term}$$

### Входные данные | Input data

`2_assets_clean_v1.csv`: признаки `interest_rate` и `term_months`, цель `amount`.

`2_assets_clean_v1.csv`: features `interest_rate` and `term_months`, target `amount`.

### Порядок решения | Solution outline

1. Разделить строки на обучающую (80%) и тестовую (20%) части.
2. Обучить модель на обучающей части.
3. Вывести коэффициенты $b_0$, $b_1$, $b_2$.
4. Посчитать $R^2$ на тестовой части.

1. Split the rows into a training part (80%) and a test part (20%).
2. Fit the model on the training part.
3. Report the coefficients $b_0$, $b_1$, $b_2$.
4. Calculate $R^2$ on the test part.

### Контрольные точки | Control points

- $R^2$ на тестовой части около 0,61, близко к 0,6 из задачи 1.
- Коэффициент при ставке отрицательный: связь обратная, как в задаче 1.
- Коэффициент при ставке около -0,0059, а не -24. Средняя сумма строки в реестре около 0,24 млн сум (12 400 млн на 50 000 активов), а в задаче 1 суммы 260-380 млн. Масштаб другой, знак и метод те же.

- $R^2$ on the test part is about 0.61, close to the 0.6 of Task 1.
- The rate coefficient is negative: the relationship is inverse, as in Task 1.
- The rate coefficient is about -0.0059, not -24. The average row amount in the ledger is about 0.24 mln UZS (12,400 mln across 50,000 assets), while in Task 1 the amounts are 260-380 mln. The scale differs, the sign and the method are the same.
