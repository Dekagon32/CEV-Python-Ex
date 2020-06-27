pe = 1
lst = []
soma = 0
while pe != 0:
    pe = int(input('Digite um valor (0) para parar: '))
    lst.append(pe)
for c in range(0,len(lst)):
    soma += lst[c]
print(soma)