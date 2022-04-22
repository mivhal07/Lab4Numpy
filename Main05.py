import numpy as np


def macierz(number):
    w = np.array([x for x in range(number, 0, -1)])
    v = np.diag(w)
    return v


print(macierz(4))
