import numpy as np
import scipy.stats as stats

sample = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
average = 200
t_calculated = (np.mean(sample) - average) / (np.std(sample, ddof=1) / np.sqrt(len(sample)))
print(t_calculated)

t_tabulated = stats.t.ppf(0.995, 10 - 1)
print(t_tabulated)

# поскольку тест двусторонний, t_tabulated принимает отрицательное и положительное значения, 
# таким образом, t_calculated лежит в области между этими двумя значениями, т.е. в области нулевой гипотезы, 
# значит делаем вывод, что нулевая гипотеза верна
