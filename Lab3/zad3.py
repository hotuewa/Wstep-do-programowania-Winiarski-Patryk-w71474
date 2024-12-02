ciąg = input("Podaj zdanie:")

ciąg_2=''.join(ciąg.lower().split())


if ciąg_2 == ciąg_2[::-1]:
    print(f"{ciąg} od tyłu to też {ciąg} a więc jest palindromem")
else:
    print("Nie jest palindromem")
