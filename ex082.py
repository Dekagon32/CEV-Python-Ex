l = []
lp = []
li = []
while True:
    l.append(int(input('Digite um valor: ')))
    r = str(input('Vai continuar?[S/N] ')).lower()
    if r == 'n':
        break

for num in l:
    if num[-1]%2 == 0:
        lp.append(num)
    elif num[-1]%2 == 1:
        li.append(num)

print('A lista de pares é: {}\nA lista de ímpares é: {}'.format(lp,li))