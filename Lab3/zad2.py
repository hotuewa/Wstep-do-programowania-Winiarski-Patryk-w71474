
# Wczytanie zdania od użytkownika
zdanie = input("Wpisz zdanie: ")

# a) Wypisz wszystkie występujące litery w kolejności alfabetycznej i brakujące litery
wystepujace_litery = sorted(set(filter(str.isalpha, zdanie.lower())))


print("a) Występujące litery w kolejności alfabetycznej:", "".join(wystepujace_litery))

# b) Usuń znaki o nieparzystych indeksach
wynik_b = zdanie[::2]
print("b) Zdanie po usunięciu znaków o nieparzystych indeksach:", wynik_b)

# c) Każdy wyraz zaczyna się i kończy wielką literą
wyrazy = zdanie.split()


# d) Najdłuższe słowo i jego długość
najdluzsze_slowo = ""
max_dlugosc = 0
for slowo in wyrazy:
    if len(slowo) > max_dlugosc:
        najdluzsze_slowo = slowo
        max_dlugosc = len(slowo)
print("d) Najdłuższe słowo:", najdluzsze_slowo)
print("   Długość najdłuższego słowa:", max_dlugosc)

# e) Zamień każdy znak, który się powtórzy na @
nowe_zdanie = ""
licznik = {}
for znak in zdanie:
    licznik[znak] = licznik.get(znak, 0) + 1
for znak in zdanie:
    if licznik[znak] > 1:
        nowe_zdanie += "@"
    else:
        nowe_zdanie += znak
print("e) Zdanie z zamienionymi powtarzającymi się znakami:", nowe_zdanie)







