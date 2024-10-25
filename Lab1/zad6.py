droga = float(input("Podaj długość planowanej trasy (w km)\n"))
spalanie = float(input("Podaj średnie spalanie samochodu (na 100km) !!!koniecznie oddzielone kropką a nie przecinkiem!!!\n"))

cena=6.5

zuzycie=droga/100*spalanie
koszta=zuzycie*cena

print(f"Przewidywane zużycie paliwa to {zuzycie} co generuje koszta w wysokości {koszta} zł")