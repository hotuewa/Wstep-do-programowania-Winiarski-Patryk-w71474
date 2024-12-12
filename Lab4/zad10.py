def hanoi(n,b,d,p):
    """
    funkcja opiera się na 4 zmiennych:
    n - która określa liczbę dysków
    b - jest to drążek z którego startujemy
    d - jest to drążek na który chcemy przełożyć dyski
    p - jest to drążek pomocniczy
    """
    if n==1:
        print(f'Przenieś krążek 1 z {b} do {d}')
    else:
        hanoi(n-1,b,p,d)
        print(f'Przenieś krążek {n} z {b} do {d}')
        hanoi(n-1,p,d,b)


n=5

hanoi(n,"A","B","C")
