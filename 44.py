import matplotlib.pyplot as plt
import numpy as np

plt.plot([0, 4], [8, 0])
plt.plot([0, 6], [3, 0])
plt.plot([0, 0], [0, 8])
plt.plot([2, 2], [0, 8])

plt.arrow(0, 0, 1, 1)
plt.title('График функции')
# создание графика и его отображение
plt.show()
