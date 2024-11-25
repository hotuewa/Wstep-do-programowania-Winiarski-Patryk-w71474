imie = input("Jak masz na imie:")

print(f"Witaj {imie}")

wiek = input("Ile masz lat:")

print(f"Twój wiek to {wiek}")

nazwisko = input("Jak masz na nazwisko:")

print(f"Twoje inicjały to: {imie[0].upper()}.{nazwisko[0].upper()}")

zdanie1 = input("Wpisz zdanie:")
zdanie2 = input("Wpisz zdanie:")

zdanie3 = zdanie1+zdanie2

print(zdanie3)
zdanie4=zdanie1[0:int(len(zdanie1)/2)]+zdanie2[int(len(zdanie1)/2)::1]
print(zdanie4)

