três = '\'Não escolhido\''
valores = (int(input('Digite um número: ')), int(input('Digite um número: ')), 
    int(input('Digite um número: ')), int(input('Digite um número: ')), )
nove = valores.count(9)
if valores.count(3) > 0:
    três = valores.index(3)
par = (valores[0] % 2, valores[1] % 2, valores[2] % 2, valores[3] % 2)
print('Os números são: ', valores)
print('Vezes que 9 foi escolhido: ', nove)
print('Primeira posição de 3: ', str(três+1), 'ª')
print('Números pares: ',end='')
for e,p in enumerate(par):
    if p == 0:
        print(valores[e],end=' ')