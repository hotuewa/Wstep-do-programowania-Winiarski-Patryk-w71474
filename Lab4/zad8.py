def potegi(a,n):
    if n==0:
        return 1
    else:
        return a * potegi(a, n - 1)


liczba=int(input("Podaj liczbe:"))

potega=int(input("Do jakiej potęgi chcesz ją podnieść?"))

print(potegi(liczba,potega))
