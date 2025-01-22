import numpy as np

macierz = np.zeros((5, 5))
macierz[0, :] = 1
macierz[-1, :] = 1
macierz[:, 0] = 1
macierz[:, -1] = 1

def zamiana(macierz):
    return np.where(macierz == 0, 1, 0)

print(f"Macierz początkowa:\n{macierz}")
print(f"Macierz po zamianie:\n{zamiana(macierz)}")
