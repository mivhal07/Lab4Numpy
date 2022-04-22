import random
import string

import numpy as np

#przyznam się, że to zadanie podpatrzyłem od kolegów do nie miałem pojęcia jak to zrobić
def LosowaLitera(i):
    return random.choices(string.ascii_uppercase, k=i)


n = 5
poziomo = 'ROBOT'
row = np.array(list(poziomo))
pionowo = 'KOT'
col = np.array(list(pionowo))

skos = 'SOK'
diag = np.array(list(skos))
macierz = np.array(LosowaLitera(n * n)).reshape([n, n])
macierz[1] = row
macierz[:3, 3] = np.flip(col)
np.fill_diagonal(macierz, diag)
print(macierz)
