

znak = str(input("Podaj jendą litere: "))

if len(znak) == 1:

    if ord(znak) >= 97 and ord(znak) <= 122:
        print("Wprowadziłeś małą litere")
    elif ord(znak) >= 65 and ord(znak) <= 90:
        print("Wprowadziłeś dużą litere")
    else : print("To nie jest litera")
else: print("Podany ciąg znakow jest za długi")