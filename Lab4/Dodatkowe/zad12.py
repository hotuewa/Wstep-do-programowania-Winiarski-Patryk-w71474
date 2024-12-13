#Napisz funkcję, która jako argument przyjmuje imię, a następnie zwraca wynik „kobieta” lub „mężczyzna”. Następnie zdefiniuj tablicę z 5 różnymi imionami i wykorzystując stworzoną funkcję stwórz słownik zawierający pary imię: płeć.

def okresl_plec(imie):
    """
    Funkcja określa płeć na podstawie imienia.
    Argument:
        imie (str): Imię do określenia płci.
    Zwraca:
        str: "kobieta" lub "mężczyzna".
    """
    imiona_kobiece = {"Anna", "Maria", "Katarzyna", "Joanna", "Zofia"}
    imiona_meskie = {"Piotr", "Jan", "Krzysztof", "Michał", "Tomasz"}

    if imie in imiona_kobiece:
        return "kobieta"
    elif imie in imiona_meskie:
        return "mężczyzna"
    else:
        return "nieznana"  # Gdy imienia nie ma w bazie.

# Tablica z 5 różnymi imionami
imiona = ["Anna", "Piotr", "Katarzyna", "Tomasz", "Joanna"]

# Tworzenie słownika zawierającego pary imię: płeć
slownik_imion = {imie: okresl_plec(imie) for imie in imiona}

# Wyświetlenie słownika
print(slownik_imion)

