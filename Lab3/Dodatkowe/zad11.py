
#Lista alfabetu
alfabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Liczba od użytkownika
n=int(input("Podaj liczbe: "))
# Dzielimy listę na podlisty co n-ty element
podlisty = []
for i in range(0, len(alfabet), n):
    podlisty.append(alfabet[i:i+n])

# Wyświetlamy wynik
print(podlisty)

