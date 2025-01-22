import matplotlib.pyplot as plt

kategorie = ['Elektronika', 'Odzież', 'Książki', 'Artykuły domowe']
sprzedane = [120, 95, 75, 110]

plt.bar(kategorie, sprzedane, color='skyblue', edgecolor='black')
plt.title('Ilość sprzedanych produktów w różnych kategoriach')
plt.xlabel('Kategorie')
plt.ylabel('Ilość sprzedanych produktów')
plt.show()
