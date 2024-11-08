gol = float(input("Podaj liczbe bramek: "))

punkty = gol*10

if 5 < gol <= 10:
    bonus=5
    punkty+=5
    print(punkty)

elif gol > 10:
    bonus=10+5
    punkty+=bonus
    print(punkty)
else: print(punkty)
