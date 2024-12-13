def hanoi(p):
    if p==1:
        return 1
    elif p>1:
        return 2*hanoi(p-1)+1



p=int(input("Ile mamy krążków? "))

print(f'Do przełożenia {p} krążków potrzebujemy minimum {hanoi(p)} ruchów')





