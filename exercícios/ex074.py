from random import randint as r

tupla = (r(0,10),r(0,10),r(0,10),r(0,10),r(0,10),)
maior = 0
menor = 0
p = 0
print('Os valores sorteados foram: ',end='')
for c in tupla:
    print(c,end=' ' if p != 4 else '\n')
    if p == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    p += 1
print(f'O maior é {maior} e o menor é {menor}')