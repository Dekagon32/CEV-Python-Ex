fat = int(input('Digite o número: '))
cal = 1
print('O fatorial de {} é:'.format(fat),end=' ')
for c in range(fat,0,-1):
    if fat > 0:
        print(c,end='')
        if c == 1:
            print(' = {}'.format(cal))

        elif c != 1:
            print(' X ',end='')
            cal *= c
    elif fat == 0:
        print('O fatorial de 0 é = 1')
        