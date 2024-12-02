# Definicja słownika z rachunkami za prąd (wartości w zł)
rachunki = {
    "Styczeń": 150,
    "Luty": 200,
    "Marzec": 180,
    "Kwiecień": 220,
    "Maj": 210,
    "Czerwiec": 190
}

# a) Wyznaczanie wartości maksymalnej, minimalnej, sumy i średniej
maksymalna = max(rachunki.values())
minimalna = min(rachunki.values())
suma = sum(rachunki.values())
srednia = suma / len(rachunki)

print("a) Statystyki rachunków za prąd:")
print("   Maksymalny rachunek:", maksymalna, "zł")
print("   Minimalny rachunek:", minimalna, "zł")
print("   Suma rachunków:", suma, "zł")
print("   Średnia wartość rachunku:", round(srednia, 2), "zł")

# b) Sprawdzenie, czy ostatni miesiąc przekroczył średnią
ostatni_rachunek = rachunki["Czerwiec"]
if ostatni_rachunek > srednia:
    print("b) Trzeba zacisnąć pasa.")
else:
    print("b) Wszystko okay.")