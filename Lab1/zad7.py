from random import *

spalanie = float(input("Podaj średnie spalanie samochodu (na 100km) !!!koniecznie oddzielone kropką a nie przecinkiem!!!\n"))

cena=6.5

droga=randint(10,1244)
zuzycie=droga/100*spalanie
koszta=zuzycie*cena

print(f"Przewidywane zużycie paliwa to {zuzycie} l, co generuje koszta w wysokości {koszta} zł")

#wylosowana liczba jest pseudolosowa gdyż algorytmy pseudolosujące są najczęściej zaopatrzone w specjalne "ziarna" (ang. "seed"),
# które kontrolują sekwencję zwracanych "niby losowych" wartości. Jeśli ziarno jest cały czas takie samo, to każda wartość losowana z tych samych przedziałów w tej samej kolejności, będzie zawsze taka sama