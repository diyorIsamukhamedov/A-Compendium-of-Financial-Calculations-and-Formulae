# Статистическая база | Statistics prerequisites

Отклонение, дисперсия и стандартное отклонение идут цепочкой: отклонение возводится в квадрат, из квадратов получается дисперсия, из корня дисперсии получается стандартное отклонение. Эти же понятия лежат в основе линейной регрессии: наклон считается через отклонения, а R² через суммы квадратов отклонений.

Deviation, variance and standard deviation form a chain: the deviation is squared, the squares give the variance, and the root of the variance gives the standard deviation. The same concepts underpin linear regression: the slope is calculated from deviations, and R² from sums of squared deviations.

## 1. Отклонение | Deviation

### Определение | Definition

Отклонение - это разница между отдельным значением и средним арифметическим набора данных. Оно показывает, на сколько конкретное значение выше или ниже среднего. Положительное отклонение указывает на то, что значение выше среднего, а отрицательное - на то, что значение ниже среднего.

A deviation is the difference between a single value and the arithmetic mean of a dataset. It shows how far above or below the mean a particular value lies. A positive deviation indicates that the value is above the mean, while a negative deviation indicates that the value is below the mean.

### Формула | Formula

$$x_i - \bar{x}$$

| Элемент \| Element | Обозначение \| Meaning | Что означает \| What it means |
|---|---|---|
| $x_i$ | i-е значение из набора данных \| The i-th value in the dataset | Отдельное наблюдение \| A single observation |
| $\bar{x}$ | Среднее арифметическое \| The arithmetic mean | Сумма всех значений, делённая на их количество \| The sum of all values divided by their count |
| $x_i - \bar{x}$ | Отклонение от среднего \| The deviation from the mean | Показывает, насколько значение отклоняется от среднего \| Shows how far a value deviates from the mean |

### Что показывает знак отклонения | What the sign of the deviation shows

- $x_i - \bar{x} > 0$: значение выше среднего | the value is above the mean.
- $x_i - \bar{x} < 0$: значение ниже среднего | the value is below the mean.
- $x_i - \bar{x} = 0$: значение равно среднему | the value equals the mean.

### Важное свойство | A key property

Сумма всех отклонений всегда равна нулю: $\sum (x_i - \bar{x}) = 0$. Положительные и отрицательные отклонения всегда гасят друг друга. Именно поэтому, чтобы измерить разброс, отклонения сначала возводят в квадрат - так получается дисперсия, а затем стандартное отклонение.

The sum of all deviations is always equal to zero: $\sum (x_i - \bar{x}) = 0$. Positive and negative deviations cancel each other out. This is exactly why, in order to measure the spread, the deviations are squared - this gives the variance, and then the standard deviation.

## 2. Выборка и генеральная совокупность | Sample and population

| Термин \| Term | Объяснение \| Explanation |
|---|---|
| Выборка \| Sample | Подмножество данных, которое мы выбрали из большой группы (например, 50 человек из 10 000) \| A subset of data that we have selected from a large group (for example, 50 people out of 10,000) |
| Генеральная совокупность \| Population | Вся группа, которую мы могли бы изучить (например, все жители города) \| The entire group we could study (for example, all the residents of a city) |

Важно различать. Если вы работаете с выборкой, используйте $\frac{1}{n-1}$. Это поправка Бесселя: выборка обычно занижает разброс, и мы добавляем поправку, чтобы не занижать дисперсию. Если вы анализируете всю совокупность, используйте $\frac{1}{n}$.

It is important to distinguish. If you are working with a sample, use $\frac{1}{n-1}$. This is Bessel's correction: a sample usually understates the spread, so we add a correction in order not to underestimate the variance. If you are analysing the whole population, use $\frac{1}{n}$.

## 3. Дисперсия | Variance

### Определение | Definition

Дисперсия - это средний квадрат отклонений от среднего. То есть, насколько значения "в среднем" удалены от среднего, но в квадратных единицах.

Variance is the average squared deviation from the mean. That is, how far the values are "on average" from the mean, but in squared units.

### Формулы | Formulae

Для выборки | For a sample:

$$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}$$

Для генеральной совокупности | For a population:

$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}$$

| Элемент \| Element | Обозначение \| Meaning |
|---|---|
| $s^2$ | Дисперсия выборки \| Sample variance |
| $\sigma^2$ | Дисперсия совокупности \| Population variance |
| $\sum$ | Сигма, знак суммы \| Sigma, the summation sign |
| $x_i$ | i-е значение из набора данных \| The i-th value in the dataset |
| $(x_i - \bar{x})^2$ | Квадрат отклонения от среднего арифметического \| The squared deviation from the mean |
| $\frac{1}{n-1}$ | Нормирующий коэффициент \| Normalising coefficient |

### Почему квадрат | Why square

1. Чтобы избавиться от отрицательных отклонений.
2. Чтобы усилить эффект отклонений (например, -3 и 3 дают одинаковый вклад: 9).
3. Но из-за квадрата результат не в тех же единицах, что исходные данные.

1. To get rid of negative deviations.
2. To strengthen the effect of the deviations (for example, -3 and 3 give the same contribution: 9).
3. But because of the square, the result is not in the same units as the original data.

## 4. Стандартное отклонение | Standard deviation

### Определение | Definition

Стандартное отклонение - это статистическая мера, которая показывает, насколько значения в наборе данных разбросаны относительно среднего значения. Небольшое стандартное отклонение указывает на то, что данные близки к среднему значению, а большое - на то, что данные более разбросаны.

Standard deviation is a measure of the spread of data in a dataset, indicating how much the data points deviate from the mean. A low standard deviation suggests that data points are clustered tightly around the mean, while a high standard deviation indicates that the data is more dispersed.

### Формула (для выборки) | Formula (for a sample)

$$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

| Элемент \| Element | Обозначение \| Meaning | Что делает \| What it does |
|---|---|---|
| $s$ | Стандартное отклонение \| Standard deviation | Итоговая мера разброса данных \| The final measure of the spread of the data |
| $\sqrt{\phantom{x}}$ | Арифметический квадратный корень \| Arithmetic square root | Возвращает результат к исходному масштабу данных \| Brings the result back to the original scale of the data |
| $\frac{1}{n-1}$ | Нормирующий коэффициент \| Normalising coefficient | Делит сумму на число наблюдений минус один \| Divides the sum by the number of observations minus one |
| $\sum$ | Сигма, знак суммы \| Sigma, the summation sign | Складывает всё выражение в скобках \| Adds up the whole expression in the brackets |
| $x_i$ | i-е значение из набора данных \| The i-th value in the dataset | Отдельное наблюдение \| A single observation |
| $\bar{x}$ | Среднее арифметическое \| The arithmetic mean | Сумма всех значений, делённая на их количество \| The sum of all values divided by their count |
| $(x_i - \bar{x})^2$ | Квадрат отклонения от среднего \| The squared deviation from the mean | Показывает, насколько значение отклоняется от среднего \| Shows how far a value deviates from the mean |

### Почему потом берём корень | Why we then take the root

Чтобы вернуться к тем же единицам измерения, что и исходные данные. Пример: если зарплата в долларах, то дисперсия будет в (долларах)², а стандартное отклонение снова в долларах.

To return to the same units of measurement as the original data. Example: if a salary is in dollars, the variance will be in (dollars)², and the standard deviation will again be in dollars.
