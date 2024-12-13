import math

def poletrojkata(a,b,c):
    if a>0 and b>0 and c>0:
        maks=max(a,b,c)
        if maks==a and a<b+c or maks==b and b<c+a or maks==c and c<a+b:
            p=(a+b+c)/2
            pt=math.sqrt(p*(p-a)*(p-b)*(p-c))
            print(f"Trójkąt o bokach {a}, {b}, {c} ma pole {pt}")
        else:
            print("Z podanych boków nie zbudujemy trójkąta")

    else:
        print("Boki muszą być większe od 0")


a=int(input("Podaj bok a:"))
b=int(input("Podaj bok b:"))
c=int(input("Podaj bok c:"))

poletrojkata(a,b,c)