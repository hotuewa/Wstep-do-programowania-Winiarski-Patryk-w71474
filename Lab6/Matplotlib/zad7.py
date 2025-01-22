import matplotlib.pyplot as plt

udzial = [120, 95, 75, 110]
etykiety = ['Elektronika', 'Odzież', 'Książki', 'Artykuły domowe']

plt.pie(udzial, labels=etykiety, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'orange', 'pink'])
plt.title('Procentowy udział kategorii w sprzedaży')
plt.show()
