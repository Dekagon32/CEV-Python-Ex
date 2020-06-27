num = 0
que = 'y'
lst = []
soma = 0
while que != 'n':
    num = int(input('Digite um número: '))
    lst.append(num)
    que = str(input('Quer continuar? '))

for c in range(0,len(lst)):
    soma += lst[c]
soma /= len(lst)
print(soma)