import random,math

list= []

a=int(input("Podaj dolny przedział: "))
b=int(input("Podaj górny przedział: "))

for i in range(10):
    x=random.randint(a,b)
    list.append(x)

newtuple = tuple(list)

print(newtuple)
p=1
for i in newtuple:
    p*=i

sr_geo=math.pow(p,1/len(newtuple))

print(sr_geo)