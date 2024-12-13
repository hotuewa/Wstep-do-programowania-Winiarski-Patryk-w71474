#Napisz funkcję informującą czy dwa podane słowa są anagramami.

def anagram(a,b):
    a=a.replace(' ','').lower()
    b=b.replace(' ','').lower()
    if sorted(a)==sorted(b):
        return "Podane słowa są anagramami"
    else:
        return "Podane słowa NIE są anagramami"

print("Wpisz 1 aby przerwać program")
while True:
    a=input("Podaj 1 słowo: ")
    if a=="1":
        break
    b=input("Podaj 2 słowo: ")

    print(anagram(a,b))