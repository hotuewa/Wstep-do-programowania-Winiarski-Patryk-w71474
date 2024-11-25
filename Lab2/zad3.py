N = int(input("Podaj liczbe naturalną:"))


if N >0:
    a = int(input("Podaj liczbe :"))
    r = int(input("Podaj liczbe:"))
    for i in range(a-1,N+1):
        print(a+(i-1)*r, end=" ")

else: print("Podana liczba N nie jest naturalna")
