from datetime import datetime

# Daty ostatnich laboratoriów i przyszłego kolokwium
data_laboratoriow = datetime(2024, 12, 12)
data_kolokwium = datetime(2025, 1, 23)

# Obecna data
dzisiaj = datetime.now()

# Obliczenia
dni_od_laboratoriow = (dzisiaj - data_laboratoriow).days
dni_do_kolokwium = (data_kolokwium - dzisiaj).days


nazwa_miesiaca = dzisiaj.strftime("%B")  # Nazwa miesiąca w języku angielskim

# Wynik
print( f"Dziś jest {dzisiaj.strftime('%d')} {nazwa_miesiaca} {dzisiaj.year}. Od ostatnich laboratoriów minęło {dni_od_laboratoriow} dni, a do kolokwium pozostało {dni_do_kolokwium} dni.")

