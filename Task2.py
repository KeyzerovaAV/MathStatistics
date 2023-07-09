import numpy as np
import scipy.stats as stats
x1 = 2.72
x2 = 2.63
n1 = n2 = 200
s1 = 0.71
s2 = 0.73
t = (x1 - x2) / np.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)
print(t)
t1 = stats.t.ppf(0.975, 400 - 2)
print(t1)
