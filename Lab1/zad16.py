import math

print("Napisz program obliczający obwód oraz pole trójkąta o danych bokach i wyświetli wyniki w konsoli.\n")

a=float(input('Podaj a: '))
b=float(input('Podaj b: '))
c=float(input('Podaj c: '))

obw=a+b+c

print("Obwód tego trójkąta wynosi", obw)

p=obw/2

P1=p*(p-a)*(p-b)*(p-c)

P=math.sqrt(P1)

print("Pole tego trójkąta wynosi", P)
