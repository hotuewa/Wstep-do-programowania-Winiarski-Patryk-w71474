x = int(input("Podaj pierwszą liczbę:"))
y = int(input("Podaj drugą liczbę:"))

while x<=y:
    if x%2!=0:
        x+=1
        continue
    print(x, end=" ")
    x+=1
