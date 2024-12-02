

cyfry=input("Podaj 5 cyfr rozdzielonych przecinkiem: ")

# a) Tworzymy tablice - liste
lista_cyfr=cyfry.split(",")

print("a) Stworzona lista: ",lista_cyfr)

# b) Sprawdzamy czy podane zostało 5 liczb

if len(lista_cyfr)==5:
    # c) zamieniamy liste na set który jest nieuporządkowany
    lista_cyfr=set(lista_cyfr)
    x=lista_cyfr.pop()
    print("Wylosowana liczba to: ",x)
    if x==max(lista_cyfr):
        print(x, "Jest największą cyfrą")
    elif x==min(lista_cyfr):
        print(x,"Jest najmniejszą cyfrą")
    else:
        print(" ")

