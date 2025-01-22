import matplotlib.pyplot as plt



oceny = [4.5, 3.0, 5.0, 4.0, 2.5, 3.5, 4.0, 3.0, 4.5, 5.0]


plt.hist(oceny, bins=[2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5], edgecolor='black', color='lightgreen')
plt.title('Rozkład ocen studentów')
plt.xlabel('Ocena')
plt.ylabel('Liczba studentów')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
