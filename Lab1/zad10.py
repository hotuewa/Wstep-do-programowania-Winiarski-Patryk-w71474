x=int(input("Podaj 1 liczbe:"))
y=int(input("Podaj 2 liczbe:"))
z=int(input("Podaj 3 liczbe:"))

if x<y and x<z:
    print(x)
    if y<z:
        print(y,"\n",z)
    else:
        print(z,"\n",y)
elif y<x and y<z:
    print(y)
    if x < z:
        print(x,"\n",z)
    else:
        print(z,"\n",x)
elif z<x and z<y:
    print(z)
    if x < y:
        print(x,"\n",y)
    else:
        print(y,"\n",x)