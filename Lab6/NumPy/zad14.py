import numpy as np

macierz = np.random.randint(1, 100, size=(5, 5))


elementy_wieksze = macierz[macierz > 20]
liczba_elementow = elementy_wieksze.size


srednia = np.mean(macierz)


print(f"Macierz:\n{macierz}")
print(f"Elementy większe niż 20: {elementy_wieksze}")
print(f"Liczba elementów większych niż 20: {liczba_elementow}")
print(f"Średnia wartość: {srednia}")
