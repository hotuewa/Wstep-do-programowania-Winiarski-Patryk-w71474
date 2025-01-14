import random

szczesliwy_numerek=random.randint(1,17)

print(f"Szczęśliwy numerek to: {szczesliwy_numerek}")

tablica_rocznikow = [2001,2002,2003,2004,2005,2006,2007]

print(f"Szczęśliwy rocznik to: {random.choice(tablica_rocznikow)}")

kule = [i for i in range(1,50)]

losowanie_totka = random.sample(kule,6)

print(f"Zwycięska sekwencja to: {losowanie_totka}")
