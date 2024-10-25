

wiek = int(input("Podaj swój wiek (1-99): "))

if wiek <18:
    print("Nie jesteś pełnoletni")
elif wiek >= 18 and wiek<=99:
    print("Jesteś pełnoletni")
else:
    print("Podaj prawdziwy wiek")
