import numpy as np


def wielokrotnosci(number):
    przekątna = np.array([x for x in np.arange(2, number * 2 + 2, 2)])
    result = np.zeros([number, number])
    for i in range(0, number, 1):
        result[i] = np.roll(przekątna, i)
    return result


print(wielokrotnosci(4))
