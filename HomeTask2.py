import numpy as np
import scipy.stats as stats

average = 17
average_sample = 17.5
n = 100
d = 4
z_calculated = (average_sample - average) / (np.sqrt(d) / np.sqrt(n))
print(z_calculated)

z_tabulated = stats.norm.ppf(1 - 0.05)
print(z_tabulated)

# поскольку z_calculated больше, чем z_tabulated, делаем вывод, 
# что z_calculated лежит в области альтернативной гипотезы, т.е. нулевая гипотеза неверна
