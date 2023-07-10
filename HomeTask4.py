import numpy as np
import scipy.stats as stats

mothers_height = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169])
daughters_height = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])

print(stats.ttest_rel(mothers_height, daughters_height))

# при выборе уровня статистической значимости = 0.05, получается, что значение p-value больше, 
# что говорит о верности нулевой гипотезы, отсюда делаем вывод, что статистически значимых различий нет
