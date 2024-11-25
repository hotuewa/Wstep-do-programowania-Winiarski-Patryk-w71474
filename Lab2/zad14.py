import math

boll= True

while bool:
    dana=int(input("Podaj liczbe:"))

    if dana<0:
        print("Dziękujemy za skorzystanie z naszej aplikacji!")
        bool = False
        continue

    print(f'{dana} jest liczbą dodatnią')

    print(f'Pierwiastek {dana} = {math.sqrt(dana)}')