#Napisz funkcję badającą czy dane słowo to palindrom.

def czy_palindrom(s):
    s=s.replace(' ','').lower()

    if s==s[::-1]:
        return "Jest to palindrom"
    else:
        return "Nie jest to palindrom"


s=input("Czy podane zdanie to palindrom?")

print(czy_palindrom(s))