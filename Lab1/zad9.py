print("Cennik:\n1.Dla osób poniżej 4 roku życia wstęp jest bezpłatny,\n2.Dla dzieci powyżej 4 lat bilet kosztuje 10zł,\n3.Dla dorosłych bilet kosztuje 20zł,\n4.Dorośli uczący się (studenci) mają 25% zniżki")

taryfa=input("Wpisz odpowiadający ci numer: ")

cena=20

if taryfa=="1":
    print("Jedziesz za darmo")
elif taryfa=="2":
    print("Cena:",cena-10, "zł")
elif taryfa=="3":
    print("Cena:",cena,"zł")
elif taryfa=="4":
    print("Cena:",cena*0.75,"zł")
else:
    print("Zły numer")