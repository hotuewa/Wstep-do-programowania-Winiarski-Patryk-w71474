import pomiary

def srednie_cisnienie(pogoda):
    """
    funkcja liczy średnią wartość ciśnienia atmosferycznego i je zwraca
    """
    suma_hpa = 0
    for i in range(len(pogoda)):
        suma_hpa += pogoda[i][2]

    return suma_hpa / len(pogoda)



print(f"25 stopni celsjusza to {pomiary.c_to_f(25)} stopni fahrenheita")

print(f"10 metrów na sekunde to {pomiary.predkosc_wiatru(10)} kilometrów na godzine ")

print(f"Ciśnienie atmosferyczne 1013 hPa w milimetrach na słupie rtęci to: {pomiary.cisnienie_atmosferyczne(1013):.2f} mmHg")


pogoda_ex = [[25,15,998],[19,24,1016],[23,7,986]]



print(f"Średnia wartość ciśnienia atmosferycznego z 3 dni wynosi {srednie_cisnienie(pogoda_ex):.2f} hPa")