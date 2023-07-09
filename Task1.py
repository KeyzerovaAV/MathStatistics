import numpy as np
import scipy.stats as stats
x = np.array([2.5, 2.2, 2.6, 2, 2.1, 1.8, 2.4, 2.3, 2.7, 2.7, 1.9])
y = np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])
print(stats.ttest_ind(x, y))
t = (np.mean(x) - np.mean(y)) / np.sqrt(np.var(x, ddof = 1) / len(x) + np.var(y, ddof = 1) / len(y))
print(t)
t1 = stats.t.ppf(0.95, 20)
print(t1)
