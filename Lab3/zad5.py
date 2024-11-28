ListaZakupow={"piwo":4,"czipsy":9,"kitkat":4,"redbull":7}

suma=0

for x in ListaZakupow:
    suma+=ListaZakupow[x]
    print(f"Na liście znajduje się {x} w cenie {ListaZakupow[x]}zł")

print(f"Twój koszyk kosztuje {suma} zł")