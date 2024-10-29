print("Wprowadź dwie liczby i co chcesz z nimi zrobic('+' , '-', '*' , '/' , '**' : \n")

l1=float(input("Podaj 1 liczbe: "))
l2=float(input("Podaj 2 liczbe: "))
pr=input("Co chcesz z nimi zrobić\n")

if pr == "+":
    print(l1+l2)
elif pr == "-":
    print(l1-l2)
elif pr == "*":
    print(l1*l2)
elif pr == "/":
    print(l1/l2)
elif pr == "**":
    print(l1**l2)
else:
    print("Wpisz poprawny znak")
