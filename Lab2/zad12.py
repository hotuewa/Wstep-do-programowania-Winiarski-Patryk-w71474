n = int(input("Podaj liczbe studentów:"))
i=1
suma_punkty=0
while i<=n:
    punkty=int(input("Podaj liczbe punktów:"))
    i+=1
    suma_punkty += punkty

print(suma_punkty)
srednia = suma_punkty/n

print(srednia)