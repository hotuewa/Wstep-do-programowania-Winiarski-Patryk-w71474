import matplotlib.pyplot as plt


czas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
predkosc = [0, 5, 15, 30, 45, 50, 55, 60, 62, 63]


plt.scatter(czas, predkosc, color='red', label='Prędkość')
plt.plot(czas, predkosc, linestyle='--', color='blue', alpha=0.7, label='Linia trendu')
plt.title('Prędkość chwilowa pojazdu w czasie')
plt.xlabel('Czas (s)')
plt.ylabel('Prędkość (km/h)')
plt.legend()
plt.grid(True)
plt.show()
