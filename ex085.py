números_ímpares = []
números_pares = []
números = [números_ímpares,números_pares]

for c in range(1,8):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n%2 == 0:
        números_pares.append(n)
    elif n%2 == 1:
        números_ímpares.append(n)

sorted(números_ímpares)
sorted(números_pares)
print('\nOs pares são: {}'.format(números_pares))
print('Os ímpares são: {}'.format(números_ímpares))