import numpy as np
import scipy.stats as stats
z = (178.5 - 179.5) / (3 / np.sqrt(100))
print(z)
z1 = stats.norm.ppf(0.01)
print(z1)
