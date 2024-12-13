def fibonacci(n):

    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n=int(input("Który wyraz ciągu fibonacciego chcesz obliczyć: "))

print(f'{n}-ty wyraz ciągu fibbonaciego jest równy {fibonacci(n)}')

