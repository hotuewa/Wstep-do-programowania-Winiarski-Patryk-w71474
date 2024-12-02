import random

#Generowanie losowych rozmiarów zbiorów
a=random.randint(3,7)
b=random.randint(3,7)
#Tworzenie zbiorów X i Y z losowymi wartosciami
X=set({})
Y=set({})
for i in range(a):
    element=random.randint(0,10)
    X.add(element)
for z in range(b):
    element_Y=random.randint(0,10)
    Y.add(element_Y)

print("Zbiór X: ",X)
print("Zbiór Y: ",Y)

# a) Czy zbiór X zawiera liczbę 5

if 5 in X:
    print("a) Zbiór X zawiera liczbę 5.")
else:
    print("a) Zbiór X nie zawiera liczby 5.")

# b) Czy zbiór X jest podzbiorem zbioru Y

if X.issubset(Y):
    print("b) Zbiór X jest podzbiorem zbioru Y.")
else:
    print("b) Zbiór X nie jest podzbiorem zbioru Y.")

# c) Czy zbiór Y jest podzbiorem zbioru X

if Y.issubset(X):
    print("c) Zbiór Y jest podzbiorem zbioru X.")
else:
    print("c) Zbiór Y nie jest podzbiorem zbioru X.")

# d) Suma zbiorów X oraz Y

suma_zbiorow = X.union(Y)
print("d) Suma zbiorów X oraz Y:", suma_zbiorow)

# e) Różnica zbiorów X oraz Y

roznica_X_Y = X.difference(Y)
print("e) Różnica zbiorów X oraz Y (X - Y):", roznica_X_Y)

# f) Różnica zbiorów Y oraz X

roznica_Y_X = Y.difference(X)
print("f) Różnica zbiorów Y oraz X (Y - X):", roznica_Y_X)

# g) Iloczyn zbiorów X oraz Y

iloczyn = X.intersection(Y)
print("g) Iloczyn zbiorów X oraz Y:", iloczyn)

# h) Największy element w obu zbiorach

najwiekszy = max(suma_zbiorow)
print("h) Najwyższy element w obu zbiorach:", najwiekszy)

# i) Usuń pierwszy element ze zbioru X i dołącz go do zbioru Y

Y.add(X.pop())
print("i) Po przeniesieniu elementu ze zbioru X do zbioru Y:")
print("   Zbiór X:", X)
print("   Zbiór Y:", Y)

# j) Przekopiuj wszystkie elementy zbioru X do zbioru Y
Y.update(X)
print("j) Po przekopiowaniu wszystkich elementów zbioru X do Y:")
print("   Zbiór X:", X)
print("   Zbiór Y:", Y)

# k) Wyczyść oba zbiory
X.clear()
Y.clear()
print("k) Po wyczyszczeniu zbiorów:")
print("   Zbiór X:", X)
print("   Zbiór Y:", Y)