soma = cont = 0
roj = []
while True:
    number = int(input('Digite um número: '))
    if number == 999:
        break
    soma += number
    cont += 1
    roj.append(number)
print(f'Os {cont} números são:')
for c in range(0,len(roj)):
    print(f'{roj[c]}', end='')
    if c != len(roj)-1:
        print(', ',end='')
print(f'\nA soma é {soma}')