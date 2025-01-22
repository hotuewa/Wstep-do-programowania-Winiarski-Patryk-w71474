import pandas as pd
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
columns = [
    "symboling", "normalized_losses", "make", "fuel_type", "aspiration", "num_doors",
    "body_style", "drive_wheels", "engine_location", "wheel_base", "length", "width",
    "height", "curb_weight", "engine_type", "num_cylinders", "engine_size",
    "fuel_system", "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
    "city_mpg", "highway_mpg", "price"
]
data = pd.read_csv(url, names=columns, na_values="?")

data.info()
print(data.describe())

avg_price_per_make = data.groupby("make")['price'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
avg_price_per_make.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Średnia cena samochodów w zależności od marki")
plt.xlabel("Marka")
plt.ylabel("Średnia cena")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data['horsepower'], data['city_mpg'], alpha=0.7, color='green', edgecolors='black')
plt.title("Zależność mocy silnika od zużycia paliwa (miasto)")
plt.xlabel("Moc silnika (HP)")
plt.ylabel("Zużycie paliwa (miasto MPG)")
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

top_countries = data['make'].value_counts().head(5)
plt.figure(figsize=(8, 8))
top_countries.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'pink', 'lightgreen', 'coral'])
plt.title("5 najczęściej występujących marek samochodów")
plt.ylabel("")
plt.tight_layout()
plt.show()

summary_by_body_style = data.groupby('body_style')[['price', 'horsepower', 'city_mpg']].mean()
print(summary_by_body_style)

plt.figure(figsize=(10, 6))
plt.scatter(data['length'], data['curb_weight'], alpha=0.7, color='purple', edgecolors='black')
plt.title("Zależność długości samochodu od jego wagi")
plt.xlabel("Długość samochodu")
plt.ylabel("Waga samochodu")
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()
