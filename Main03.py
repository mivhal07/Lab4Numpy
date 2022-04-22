import numpy as np


def funkcja(n):
    array = np.arange(1, (n * n) + 1, 1)
    array2 = array.reshape(n, n)
    return array2


print(funkcja(3))
