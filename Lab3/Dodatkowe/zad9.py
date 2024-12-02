#wymiary pola
szerokosc=6
wysokosc=5

#położenie podanych punktów
przeciwnicy=[(0,1),(2,3),(2,4),(3,4)]
monety=[(1,1),(2,0),(3,3),(5,3)]
rzeka=[(0,2),(1,2),(2,2),(3,2),(4,2),(5,2)]

for y in range(wysokosc):
    for x in range(szerokosc):
        if (x,y) in rzeka:
            print("=",end="")
        elif (x,y) in przeciwnicy:
            print("X",end="")
        elif (x,y) in monety:
            print("*",end="")
        else:
            print(".",end="")
    print()