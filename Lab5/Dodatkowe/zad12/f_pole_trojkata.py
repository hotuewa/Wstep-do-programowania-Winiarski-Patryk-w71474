import math

def czy_istnieje(a,b,kat):
    """
    Sprawdza, czy trójkąt istnieje na podstawie długości boków i kąta
    """
    return (a>0 and b>0 and 0<kat<180)

def czy_ostrokatny(a,b,c):
    """
    Sprawdza czy trójkąt jest ostrokątny
    """
    return (a**2 + b**2 > c**2)

def licz_pole_trojkata(a,b,kat):
    """
    Oblicza pole trójkąta na podstawie boków a,b i kąta między nimi
    """

    if not czy_istnieje(a,b,kat):
        return "Podane dane nie tworzą trójkąta."

    kat_radiany =math.radians(kat)

    c=math.sqrt(a**2+b**2-2*a*b*math.cos(kat_radiany))

    if not czy_ostrokatny(a,b,c):
        return "Trójkąt nie jest ostrokątny"

    pole=0.5*a*b*math.sin(kat_radiany)
    return f"Pole trójkąta o bokach {a} i {b} i kącie {kat} wynosi {pole:.2f}"

