val = []
spc = list(range(0,5))

for c in spc:
    n = int(input('Digite o valor: '))

    if c == 0:
        val.append(n)
        print('Adicionado no primeiro slot')
    elif n > val[-1]:
        val.append(n)
        print('Adicionado no ultimo slot')
    else:
        pos = 0
        while pos < len(val):
            if n <= val[pos]:
                val.insert(pos,n)
                break
            pos += 1
        print(f'Adicionado no slot {pos}')
print('A lista foi: ')
print('_'*11)
for en,num in enumerate(val):
    if en == 0:
        print('|',end='')
    print(f'{num}',end='|')
print('')
print('¯'*11)