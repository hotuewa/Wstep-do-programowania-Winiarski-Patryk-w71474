a = int(input("podaj a:"))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

print("Podpunkt a)\n")
if a > 0:
    print(2*a)
elif a==0:
    print(0)
elif a<0:
    print(-3*a)

print("\nPodpunkt b)\n")
if b>=1:
    print(b**2)
elif b<1:
    print(b)
print("\nPodpunkt c)\n")
if c>2:
    print(2+c)
elif c==2:
    print(8)
elif c<2:
    print(c-4)


