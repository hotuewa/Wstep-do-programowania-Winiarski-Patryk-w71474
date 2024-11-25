n = int(input("Podaj liczbe studentów:"))
i=1
suma_punkty=0
#while i<=n:
#    punkty=int(input("Podaj liczbe punktów:"))
#    if punkty<0 or punkty>100:
#        i+=1
#        continue
#    i+=1
#    suma_punkty += punkty

while True:
    if i>n:
        break
    punkty = int(input("Podaj liczbe punktów:"))
    if punkty<0 or punkty>100:
        i+=1
        continue
    i+=1
    suma_punkty += punkty

print(suma_punkty)
srednia = suma_punkty/n

print(srednia)