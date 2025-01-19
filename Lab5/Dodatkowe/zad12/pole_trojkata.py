import f_pole_trojkata

a = int(input("Podaj bok a: "))
b= int(input("Podaj bok b: "))
kat = int(input("Podaj kat (w stopniach): "))


pole=f_pole_trojkata.licz_pole_trojkata(a,b,kat)

print(pole)