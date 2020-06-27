print('-'*30)
print('CAIXA ELETRÔNICO')
print('-'*30)
n100 = n50 = n20 = n10 = n5 = n2 = m1 = 0
saque = int(input('Digite o valor de saque(Números inteiros): '))
while True:
    while True:
        if saque >= 100:
            saque -= 100
            n100 += 1
            break
        if saque >= 50:
            saque -=50
            n50 += 1
            break
        if saque >= 20:
            saque -= 20
            n20 += 1
            break
        if saque >= 10:
            saque -= 10
            n10 += 1
            break
        if saque >= 5:
            saque -= 5
            n5 += 1
            break
        if saque >= 2:
            saque -= 2
            n2 += 1
            break
        if saque >= 1:
            saque -= 1
            m1 += 1
            break
    if saque == 0:
        break

if n100 > 0:
    print('{} notas de R$100'.format(n100))
if n50 > 0:
    print('{} notas de R$50'.format(n50))
if n20 > 0:
    print('{} notas de R$20'.format(n20))
if n10 > 0:
    print('{} notas de R$10'.format(n10))
if n5 > 0:
    print('{} notas de R$5'.format(n5))
if n2 > 0:
    print('{} notas de R$2'.format(n2))
if m1 > 0:
    print('{} moedas de R$1'.format(m1))