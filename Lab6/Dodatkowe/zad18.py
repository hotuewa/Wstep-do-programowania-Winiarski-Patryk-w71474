import pandas as pd
import matplotlib.pyplot as plt


file_path = 'sprzedaz.xlsx'
df_sales = pd.read_excel(file_path)


print("Podstawowe informacje o danych:")
print(df_sales.info())
print("\nPodstawowe statystyki opisowe:")
print(df_sales.describe())



print("Podgląd danych:")
print(df_sales.head())

total_sales = df_sales['Ilość'].sum()
print(f"Suma sprzedaży: {total_sales}")

average_price = df_sales['Cena'].mean()
print(f"Średnia cena produktu: {average_price:.2f}")



sales_by_category = df_sales.groupby('Kategoria')['Ilość'].sum()


sales_by_category.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Ilość sprzedanych produktów w poszczególnych kategoriach')
plt.xlabel('Kategoria')
plt.ylabel('Ilość sprzedanych produktów')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


plt.scatter(df_sales['Cena'], df_sales['Ilość'], color='blue', alpha=0.6)
plt.title('Zależność ceny od ilości sprzedanych produktów')
plt.xlabel('Cena produktu (PLN)')
plt.ylabel('Ilość sprzedanych produktów')
plt.grid(True)
plt.show()



correlation = df_sales['Cena'].corr(df_sales['Ilość'])
print(f"Korelacja między ceną a ilością sprzedanych produktów: {correlation:.2f}")

