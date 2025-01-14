def losowanie(a,b):
    """
    Funkcja losuje 1 liczbe z podanego przedziału jeśli przedział jest odpowiednio duży
    """

    if a >= 1 and b >= 10:
        spis_liczb = {i for i in range(a,b)}
        x=spis_liczb.pop()
        return x
    else:
        return "Podany przedział jest zbyt mały "

def wskazowki(liczba,dobra_liczba):

    """
    Funkcja sprawdza stosunki dwóch liczb i zwraca odpowiednie komunikaty
    liczba: jest to liczba podana przez użytkownika
    dobra_liczba: jest to wygrywająca liczba
    """
    if liczba > dobra_liczba:
        return "za dużo"
    if liczba < dobra_liczba:
        return "za mało"