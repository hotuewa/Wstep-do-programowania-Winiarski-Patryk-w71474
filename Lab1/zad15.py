print("Napisz program rozwiązywania równania liniowego 0=ax+b, gdzie a i b są współczynnikami podawanymi przez użytkownika.\n")

a=float(input('Podaj a: '))
b=float(input('Podaj b: '))

if a != 0:
    print(-b/a)
else: print("Współczynnik a nie może być zerem")