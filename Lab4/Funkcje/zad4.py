def bmi(m,w):
    if m>0 and m<1000 and w>50 and w<250:
        w=w/100
        wbmi=m/w**2
        print(f'Osoba o masie {m} kg i wzroście {w} m ma bmi równe {wbmi}')

        if wbmi <16:
            print("Niedowaga")
        elif wbmi >=16 and wbmi <=16.9:
            print("wychudzenie")
        elif wbmi >= 17 and wbmi <= 18.5:
            print("niedowaga")
        elif wbmi >= 18.5 and wbmi <= 24.9:
            print("waga prawidłowa")
        elif wbmi >=25 and wbmi <=29.9:
            print("nadwaga")
        elif wbmi >=30 and wbmi <=34.9:
            print("otyłość I stopnia")
        elif wbmi >= 35 and wbmi <= 39.9:
            print("otyłość II stopnia")
        elif wbmi >=40:
            print("otyłość III stopnia")
    else:
        print("Podaj prawidłowe wartości")


masa=int(input("Podaj ile ważysz: "))
wzrost=int(input("Podaj swój wzrost: "))


bmi(masa,wzrost)

