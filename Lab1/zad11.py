import math

print("Równanie w postaci a*x**2 + b*x + c == 0")
a = int(input("podaj a:"))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
delta = (b ** 2 - 4 * a * c)
print(delta)
if int(delta) > 0:
    print("Pierwiastki równania kwadratowego: ")
    x1 = (- b - math.sqrt(int(delta))) / (2 * a)
    x2 = (- b + math.sqrt(int(delta))) / (2 * a)
    print("x1: ",  x1)
    print("x2: ", x2)
elif int(delta) == 0:
    print("Pierwiastki równania kwadratowego: ")
    x0 = - b / (2 * a)
    print("x0: ",  x0)
else:
    print("Delta jest ujemna, wiec nie liczymy miejsc zerowych.")