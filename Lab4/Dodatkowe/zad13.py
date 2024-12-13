#Napisz funkcję, która otrzymuje dwa obiekty iterowalne (sekwencje) i zwraca listę wspólnych dla obu obiektów wartości.

def ws_wartosci(a,b):
    return list(set(a) & set(b))


print(ws_wartosci("abcd","cdef"))