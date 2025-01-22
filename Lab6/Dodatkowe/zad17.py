import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "a1db0d600c180fa5ea040cbd276dda20"
CITIES = ["London", "New York", "Tokyo", "Sydney", "Berlin"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

data = []
for city in CITIES:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        data.append({
            "City": city,
            "Temperature": weather_data["main"]["temp"],
            "Min Temperature": weather_data["main"]["temp_min"],
            "Max Temperature": weather_data["main"]["temp_max"],
            "Humidity": weather_data["main"]["humidity"],
            "Pressure": weather_data["main"]["pressure"]
        })
    else:
        print(f"Failed to fetch data for {city}. Status code: {response.status_code}")

weather_df = pd.DataFrame(data)

print("Informacje o danych:")
print(weather_df.info())
print("\nPodstawowe statystyki:")
print(weather_df.describe())

missing_data = weather_df.isnull().sum()
print("\nBrakujące dane:")
print(missing_data)

plt.figure(figsize=(10, 6))
plt.bar(weather_df["City"], weather_df["Temperature"], color='skyblue')
plt.title("Średnia temperatura w miastach")
plt.xlabel("Miasto")
plt.ylabel("Temperatura (°C)")
plt.show()

weather_df.set_index("City")[["Min Temperature", "Max Temperature"]].plot(kind="bar", figsize=(10, 6))
plt.title("Porównanie temperatur minimalnych i maksymalnych")
plt.xlabel("Miasto")
plt.ylabel("Temperatura (°C)")
plt.legend(title="Typ temperatury")
plt.show()

