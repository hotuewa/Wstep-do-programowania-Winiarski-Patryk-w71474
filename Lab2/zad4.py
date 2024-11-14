nat = int(input("Podaj liczbe naturalną:"))

if nat>0:
    silnia=1
    for i in range(1,nat+1):
        silnia*=i

print(silnia)