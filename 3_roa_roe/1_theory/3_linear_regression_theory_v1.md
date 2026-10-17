# Линейная регрессия | Linear regression

Метод предсказания целевой величины по признакам.

A method for predicting a target value from features.

## 1. Что такое линейная регрессия | What linear regression is

Линейная регрессия - это метод машинного обучения, который находит прямую линию, наилучшим образом описывающую связь между признаком и целевой величиной. Каждая точка - это один объект (актив): по горизонтали его признак, по вертикали целевая величина. По найденной линии модель предсказывает цель для новых данных.

Linear regression is a machine learning method that finds the straight line which best describes the relationship between a feature and a target value. Each point is one object (asset): its feature on the horizontal axis, the target value on the vertical. From the fitted line the model predicts the target for new data.

## 2. Где используется и для чего | Where it is used and why

| Область \| Area | Задача \| Purpose |
|---|---|
| Кредитный скоринг \| Credit scoring | Оценка риска заёмщика по его признакам \| Assessing a borrower's risk from their features |
| Прогнозирование \| Forecasting | Прогноз объёма, дохода и потерь портфеля \| Forecasting portfolio volume, income and losses |
| Ценообразование \| Pricing | Расчёт ставки или суммы по характеристикам \| Setting a rate or amount from characteristics |

## 3. Формулы | Formulae

### Предсказание | Prediction

$$\hat{y} = b_0 + b_1 x_1 + b_2 x_2 + \dots + b_n x_n$$

Для одного признака | For one feature:

$$\hat{y} = b_0 + b_1 x$$

### Обучение - метод наименьших квадратов | Training - least squares

Модель подбирает коэффициенты так, чтобы сумма квадратов ошибок была минимальной.

The model chooses the coefficients so that the sum of squared errors is as small as possible.

$$\text{minimise} \sum (y - \hat{y})^2$$

### Коэффициенты (для одного признака) | Coefficients (for one feature)

$$b_1 = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sum (x - \bar{x})^2} \qquad b_0 = \bar{y} - b_1 \bar{x}$$

Числитель наклона строится из отклонений $x$ и $y$ от их средних, знаменатель - из квадратов отклонений $x$. Это те же отклонения, что и в статистической базе.

The numerator of the slope is built from the deviations of $x$ and $y$ from their means, the denominator from the squared deviations of $x$. These are the same deviations as in the statistics prerequisites.

### Оценка качества | Quality score

$$R^2 = 1 - \frac{SS_{\text{ост}}}{SS_{\text{общ}}}$$

$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$$

где | where:

$$SS_{\text{ост}} = SS_{\text{res}} = \sum (y - \hat{y})^2 \qquad SS_{\text{общ}} = SS_{\text{tot}} = \sum (y - \bar{y})^2$$

$SS_{\text{общ}}$ - это числитель дисперсии $y$: разброс фактических значений вокруг среднего. $SS_{\text{ост}}$ - разброс, который модель не объяснила. $R^2$ показывает долю разброса, которую модель объяснила.

$SS_{\text{tot}}$ is the numerator of the variance of $y$: the spread of the actual values around the mean. $SS_{\text{res}}$ is the spread the model did not explain. $R^2$ shows the share of the spread the model explained.

## 4. Обозначения | Notation

| Символ \| Symbol | Значение \| Meaning |
|---|---|
| $\hat{y}$ | Предсказание модели \| Model prediction |
| $y$ | Реальное значение, факт \| The actual value |
| $x$ | Признак (вход) \| Feature (input) |
| $b_0$ | Сдвиг: значение $\hat{y}$ при $x = 0$ \| Intercept: the value of $\hat{y}$ at $x = 0$ |
| $b_1 \dots b_n$ | Коэффициенты (веса) признаков \| Coefficients (weights) of the features |
| $n$ | Число признаков \| Number of features |
| $\bar{x}, \bar{y}$ | Средние значения $x$ и $y$ \| Means of $x$ and $y$ |
| $\sum$ | Сумма по всем объектам \| Sum over all objects |
| $SS_{\text{ост}} \mid SS_{\text{res}}$ | Сумма квадратов ошибок \| Sum of squared errors |
| $SS_{\text{общ}} \mid SS_{\text{tot}}$ | Разброс вокруг среднего \| Variation around the mean |
| $R^2$ | Доля объяснённого разброса \| Share of explained variation |
