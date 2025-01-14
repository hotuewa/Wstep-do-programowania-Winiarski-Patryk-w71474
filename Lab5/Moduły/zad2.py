import math,cmath

#podpunkt a)
print(f"Pierwiastek kwadratowy z 81 wynosi: {math.sqrt(81)} ")

#podpunkt b)
print(f'8 do potęgi 10 wynosi: {math.pow(8,10)}')

#podpunkt c)
suma=math.sqrt(2)+math.sqrt(3)+math.sqrt(6)

print(f"Suma pierwiastków kwadratowych 2,3 i 6 wynosi: {suma:2f}")


#podpunkt d)
#normalna biblioteka math zwróciła by w tym miejscu błąd dlatego używamy biblioteki cmath która umożliwia obliczenie pierwiastka z liczby ujemnej
print(f'Pierwiastek kwadratowy z -5 wynosi: {cmath.sqrt(-5)}')


#podpunkt e
#podnosimy liczbe do potęgi odwrotności stopnia pierwiastka
print(f'Pierwiastek sześcienny z 125 wynosi: {math.pow(125,1/3)}')


