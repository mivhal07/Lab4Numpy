import numpy as np

list = np.arange(1, 26, 1)
list[1] = 1
for i in range(2, 25, 1):
    list[i] = list[i - 1] + list[i - 2]
macierz = list.reshape([5, 5])
print(macierz)
