# Задачи: статистическая база | Tasks: statistics prerequisites

Обе задачи решаются на одном наборе данных, поэтому результаты переходят из задачи в задачу.

Both tasks use the same dataset, so the results carry over from one task to the next.

## Задача 1. Отклонения и их сумма | Task 1. Deviations and their sum

### Дано | Given

$$x = [7, 9, 13, 10, 6]$$

### Найти | Find

Отклонения от среднего и их сумму.

The deviations from the mean and their sum.

### Шаг 1. Среднее арифметическое | Step 1. The arithmetic mean

$$\bar{x} = \frac{7 + 9 + 13 + 10 + 6}{5} = \frac{45}{5} = 9$$

### Шаг 2. Отклонения от среднего | Step 2. Deviations from the mean

| $x_i$ | $x_i - \bar{x}$ |
|---|---|
| 7 | 7 - 9 = -2 |
| 9 | 9 - 9 = 0 |
| 13 | 13 - 9 = 4 |
| 10 | 10 - 9 = 1 |
| 6 | 6 - 9 = -3 |

### Шаг 3. Сумма отклонений | Step 3. The sum of the deviations

$$\sum (x_i - \bar{x}) = -2 + 0 + 4 + 1 - 3 = 0$$

### Вывод | Conclusion

Сумма отклонений равна нулю, как и следует из ключевого свойства: положительные и отрицательные отклонения гасят друг друга. Поэтому для измерения разброса отклонения возводят в квадрат.

The sum of the deviations is zero, as the key property states: positive and negative deviations cancel each other out. This is why the deviations are squared to measure the spread.

## Задача 2. Дисперсия и стандартное отклонение выборки | Task 2. Sample variance and standard deviation

### Дано | Given

$$x = [7, 9, 13, 10, 6]$$

### Найти | Find

$s$ по формуле выборки.

$s$ using the sample formula.

$$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

### Шаг 1. Среднее арифметическое | Step 1. The arithmetic mean

$$\bar{x} = \frac{45}{5} = 9$$

### Шаг 2. Отклонения от среднего | Step 2. Deviations from the mean

Из задачи 1: -2, 0, 4, 1, -3.

From Task 1: -2, 0, 4, 1, -3.

### Шаг 3. Квадраты отклонений | Step 3. Squared deviations

| № | $(x_i - \bar{x})^2$ |
|---|---|
| 1 | $(-2)^2 = 4$ |
| 2 | $0^2 = 0$ |
| 3 | $4^2 = 16$ |
| 4 | $1^2 = 1$ |
| 5 | $(-3)^2 = 9$ |

### Шаг 4. Сумма квадратов | Step 4. The sum of squares

$$\sum (x_i - \bar{x})^2 = 4 + 0 + 16 + 1 + 9 = 30$$

### Шаг 5. Дисперсия выборки | Step 5. Sample variance

$$s^2 = \frac{30}{5 - 1} = \frac{30}{4} = 7{,}5$$

$$s^2 = \frac{30}{5 - 1} = \frac{30}{4} = 7.5$$

### Шаг 6. Стандартное отклонение | Step 6. Standard deviation

$$s = \sqrt{7{,}5} \approx 2{,}74$$

$$s = \sqrt{7.5} \approx 2.74$$

### Ответ | Answer

Дисперсия выборки $s^2 = 7{,}5$, стандартное отклонение $s \approx 2{,}74$.

Sample variance $s^2 = 7.5$, standard deviation $s \approx 2.74$.

### Вывод | Conclusion

В среднем значения отклоняются от среднего 9 примерно на 2,74 единицы. Дисперсия 7,5 выражена в квадратных единицах, корень возвращает результат к исходным единицам данных.

On average the values deviate from the mean of 9 by about 2.74 units. The variance of 7.5 is in squared units, and the root brings the result back to the original units of the data.
