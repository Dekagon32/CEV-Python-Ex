def fatorial(n,show=False):
    cont = n - 1
    while cont > 0:
        n *= cont
        cont -= 1
    return n
print(fatorial(6))
print(fatorial(int(input('Digite o fatorial: '))))
