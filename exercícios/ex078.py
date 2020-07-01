lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input('Digite um número em ({}): '.format(c))))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
posmaior = []
posmenor = []

for enum,val in enumerate(lista):
    if val == maior:
        posmaior.append(enum)
    if val == menor:
        posmenor.append(enum)


print(f'\nO maior foi [{maior}] ',end = 'na posição: ' if len(posmaior) == 1 else 'nas posições: ')
for pos in posmaior:
    print(pos,end = ' ')

print(f'\ne o menor foi [{menor}] ',end = 'na posição: ' if len(posmenor) == 1 else 'nas posições: ')
for pos in posmenor:
    print(pos,end='')
print(f'\n{lista}')
