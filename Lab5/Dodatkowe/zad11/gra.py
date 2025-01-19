import f_gry

a=int(input("Podaj dolny (min 1) :  "))
b=int(input("Podaj górny przedział (min 10): "))

dobra_liczba = f_gry.losowanie(a,b)
#print(dobra_liczba)
proby = 3
while proby>0:
    liczba = int(input("Podaj liczbe: "))
    if liczba==dobra_liczba:
        print("Gratulacje wygrałeś prawidłowa liczba to ",dobra_liczba)
        break
    else:
        f_gry.wskazowki(liczba,dobra_liczba)
        proby-=1

print(f"Nie udało się prawidłowa liczba to {dobra_liczba}")


