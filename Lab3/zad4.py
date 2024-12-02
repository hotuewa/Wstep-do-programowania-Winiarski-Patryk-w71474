import random

# Wczytanie danych od użytkownika
n = int(input("Podaj liczbę elementów w liście (n): "))
x = int(input("Podaj maksymalną długość ciągu znakowego (x): "))

# Tworzenie listy z losowymi ciągami znaków
lista = []
for i in range(n):
    dlugosc = random.randint(1, x)  # Losowa długość ciągu
    ciag = ""
    for j in range(dlugosc):
        ciag += chr(random.randint(97, 122))  # Losowy znak od 'a' do 'z'
    lista.append(ciag)

print("Wygenerowana lista:", lista)

# Przekonwertowanie listy na krotkę
krotka = tuple(lista)
print("Krotka:", krotka)


# a) Liczba wszystkich znaków w krotce
ilosc_znakow = 0
for ciag in krotka:
    ilosc_znakow += len(ciag)
print("a) Ilość znaków w krotce:", ilosc_znakow)

# b) Liczba liter 'k' w krotce
ilosc_k = 0
for ciag in krotka:
    for znak in ciag:
        if znak == 'k':
            ilosc_k += 1
print("b) Ilość liter 'k' w krotce:", ilosc_k)

# c) Liczba ciągów zawierających 'kt'
ilosc_kt = 0
for ciag in krotka:
    if 'kt' in ciag:
        ilosc_kt += 1
print("c) Ilość ciągów zawierających 'kt':", ilosc_kt)

# d) Liczba ciągów dłuższych niż s
s = int(input("Podaj wartość s: "))
ilosc_dluzszych = 0
for ciag in krotka:
    if len(ciag) > s:
        ilosc_dluzszych += 1
print("d) Ilość ciągów dłuższych niż", s, ":", ilosc_dluzszych)