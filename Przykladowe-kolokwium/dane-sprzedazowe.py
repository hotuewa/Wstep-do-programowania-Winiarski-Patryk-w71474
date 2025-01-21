def dodaj_produkt():
    """
    funkcja dodaje produkt do bazy danych
    """
    nazwa = str(input("Nazwa produktu: "))
    wynik_sprzedazy = []
    for i in range(3):
        wynik_sprzedazy.append(int(input(f"Podaj wynik sprzedaży z {i + 1} tygodnia:")))
    dane_sprzedazowe.update({nazwa.lower(): wynik_sprzedazy})
    print(dane_sprzedazowe)

def czy_jest_w_bazie(produkt):
    """
    funkcja zwraca warunek który sprawdza  czy podany element jest w bazie danych
    """
    return produkt.lower() in dane_sprzedazowe

def suma_sprzedazy(pr):
    """
    funkcja liczy sume sprzedaży pojedynczego produktu
    """
    lista_sprzedazy = dane_sprzedazowe[pr]
    sumaryczna_sprzedaz = 0
    for i in lista_sprzedazy:
        sumaryczna_sprzedaz += i
    return sumaryczna_sprzedaz

def max_suma(dane_sprzedaz):
    """
    funkcja tworzy nowy słownik z policzoną sumą sprzedaży, później sprawdza do których elementów w słowniku należy największa suma i je wypisuje
    """
    dict_max={}
    for i in dane_sprzedaz.keys():
        dict_max[i]=suma_sprzedazy(i)

    x = max(dict_max.values())

    wynik = ""
    for y in dict_max:
        if dict_max[y]==x:
            wynik+=" , "+y

    return wynik


def srednia_sprzedaz(produkt):
    """
   funkcja liczy średnią sprzedaż każdego elementu i ją wyświetla
    """
    dict_max = {}
    for i in produkt.keys():
        dict_max[i] = suma_sprzedazy(i)/3

    for x, y in dict_max.items():
        print(f"Średnia suma sprzedaży {x} wynosi  {y:.2f}")


def prog(dane_sprzedaz,xy):
    """
    funkcja tworzy nowy słownik z policzoną sumą sprzedaży, później porownoje ich wynik z progiem podanym przez uzytkownika
    """
    dict_max={}
    for i in dane_sprzedaz.keys():
        dict_max[i]=suma_sprzedazy(i)

    wynik = []
    for x, y in dict_max.items():
        if y<xy:
            wynik.append(x)

    return wynik








dane_sprzedazowe = {"nike pro": [22, 33, 10], "mis":[55,55,55], "klocki":[55,55,55]}

stop = True
while stop:

    x = """
        Wpisz:
        1 - aby dodać nowy produkt
        2 - aby wyświetlić sumaryczną sprzedaż
        3 - aby usunąć produkt
        4 - aby zakończyć działanie programu
        5 - aby znaleźć produkt z największą sprzedażą
        6 - aby wyświetlić średnią sprzedaż produktów
        7 - aby wyświetlić produkty ponizej podanego progu

    """
    print(x)

    opcja = int(input("Wpisz tutaj:"))

    if opcja == 1:
        dodaj_produkt()

    elif opcja == 2:
        produkt = str(input("Podaj produkt: "))
        if czy_jest_w_bazie(produkt):
            sumaa=suma_sprzedazy(produkt)
            print(f"Sumaryczna sprzedaż {produkt} wynosi {sumaa} ")
        else:
            print("Podany produkt nie znajduje się w bazie danych")

    elif opcja == 3:
        produkt = str(input("Podaj produkt: "))
        if czy_jest_w_bazie(produkt):
            dane_sprzedazowe.pop(produkt)
        else:
            print("Podany produkt nie znajduje się w bazie danych")

    elif opcja == 4:
        stop = False

    elif opcja == 5:
        print(f" Największą sprzedaż ma/mają: {max_suma(dane_sprzedazowe)}")

    elif opcja ==6:
        srednia_sprzedaz(dane_sprzedazowe)

    elif opcja==7:
        xy=int(input("Podaj próg sprzedaży:"))
        w=prog(dane_sprzedazowe,xy)

        print(f"Produkty z sumaryczną sprzedażą poniżej {xy} to {w}")

    else:
        continue



