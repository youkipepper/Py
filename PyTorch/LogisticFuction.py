# 饱和函数

import matplotlib.pyplot as plt
import numpy as np

e = np.exp(1)

x = np.linspace(-10, +10)
y = 1/(1+e ** (-x))

plt.figure()
plt.plot(x, y)
plt.show()
