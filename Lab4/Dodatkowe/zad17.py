#Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
#Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.

def wyswietl_parametry(*args):
    """
    Funkcja wyświetla wartości przekazanych parametrów.
    Argumenty:
        *args: Zmienna liczba parametrów.
        maks: Największy parametr.
    """
    maks=0
    for param in args:
        if param>maks:
            maks=param
        print(param, end=" ")

    print(f'Największy parametr z podanych to {maks}')


wyswietl_parametry(5,44564,456,67,46,1,76,532)