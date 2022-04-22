import numpy as np


def funkja(podstawa, ilość):
    potega = np.logspace(1, ilość + 1, ilość, False, podstawa)
    return potega


print(funkja(5, 3))
