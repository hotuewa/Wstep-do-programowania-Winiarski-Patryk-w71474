
x=int(input("Podaj liczbe wierszy:"))

print("a)\n")
for j in range(x):
    for i in range(0,x):
        print("*",end=" ")
    print(" ")

print("\nb)\n")

for j in range(x):
    for i in range(1+j):
        print("*", end=" ")
    print(" ")


print("\nc)\n")

for j in range(x):
    print((x-1-j)*" ",end="")
    for i in range(j+1):
        print("*", end=" ")
    print(" ")
