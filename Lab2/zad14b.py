import math


while True:
    dana=int(input("Podaj liczbe:"))

    if dana<0:
        print("Dziękujemy za skorzystanie z naszej aplikacji!")
        break

    print(f'{dana} jest liczbą dodatnią')

    print(f'Pierwiastek {dana} = {math.sqrt(dana)}')