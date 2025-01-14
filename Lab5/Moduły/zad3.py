import time

def sekundnik(czas_w_sekundach):
    """
    Funkcja odlicza czas w sekundach, wyświetlając liczbę sekund pozostałą do końca.

    czas_w_sekundach: Całkowita liczba sekund do odliczenia.
    """
    while czas_w_sekundach > 0:
        print(f"Pozostało: {czas_w_sekundach} sekund")
        time.sleep(1)
        czas_w_sekundach -= 1

    print("Koniec odliczania!")


czas = int(input("Podaj czas odliczania w sekundach: "))
sekundnik(czas)
