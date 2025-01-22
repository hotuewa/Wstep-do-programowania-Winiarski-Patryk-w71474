import numpy as np


macierz = np.random.randint(1, 100, size=(5, 5))


max_element = np.max(macierz)
min_element = np.min(macierz)


max_wiersze = np.max(macierz, axis=1)
max_kolumny = np.max(macierz, axis=0)

suma_wiersze = np.sum(macierz, axis=1)


print(f"Macierz:\n{macierz}")
print(f"Największy element: {max_element}")
print(f"Najmniejszy element: {min_element}")
print(f"Największe elementy w wierszach: {max_wiersze}")
print(f"Największe elementy w kolumnach: {max_kolumny}")
print(f"Suma wierszy: {suma_wiersze}")
