#Napisz funkcję pozwalającą na odnalezienie największego wspólnego dzielnika dwóch liczb.

def nwd(a,b):
    """
    Wykorzystujemy tutaj tzw. algorytm Euklidesa
    """
    #dzielimy z resztą a przez b
    reszta=a%b
    #warunek do zakonczenia rekurencji
    if reszta==0:
        return b
    else:
        a=b
        b=reszta
        return nwd(a,b)

a=int(input("Podaj 1 liczbe: "))
b=int(input("Podaj 2 liczbe: "))

print(nwd(a,b))