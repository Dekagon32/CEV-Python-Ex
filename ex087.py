matrix = []
pares = []
soma3 = []
maior2 = []
i = 1
j = 1
for c in range(0,3*3):
    matrix.append(int(input('Digite o valor de a{}{}: '.format(i,j))))
    if i == 2:
        maior2.append(matrix[c])
    if matrix[c]%2 == 0:
        pares.append(matrix[c])
    if j < 3:
        j += 1
    elif j == 3:
        j = 1
        i += 1
        soma3.append(matrix[c])
    
j = i = 1
print('')
for c in matrix:
    if j == 1:
        print('|',end='')
    print(c,end=' ')
    if j < 3:
        j += 1
    else:
        j = 1
        i += 1
        print('|')
somapar = 0
somaterça = 0
maiorda2 = 0
for par in pares:
    somapar += par
for num in soma3:
    somaterça += num

for en,num in enumerate(maior2):
    if en == 0:
        maiorda2 = num
    elif num > maiorda2:
        maiorda2 = num

print('A soma dos pares é: {}'.format(somapar))
print('A soma da terceira coluna é: {}'.format(somaterça))
print('O maior da segunda linha é: {}'.format(maiorda2))
print(matrix,maior2,maiorda2)