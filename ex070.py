print('-'*30)
print('Lojão do Dévoli')
print('-'*30)
isa = 's'
prod = []
preç = []
soma = 0
mais1000 = 0
menor = 0
while True:
    product = str(input('Digite o nome do produto: '))
    prod.append(product)
    preço = float(input('Digite o preço do produto: R$'))
    preç.append(float(preço))
    print('-'*30)
    isa = str(input('Quer continuar? ')).strip().lower()
    print('-'*30)
    if isa[0] == 'n':
        break
print('Os produtos são: {}\nO preço final é: '.format(prod),end='')
for c in range(0,len(preç)):
    soma += preç[c]
print('R$'+str(soma))
for c in range(0,len(preç)):
    if preç[c] > 1000:
        mais1000 += 1
print(f'Produtos com preço maior que R$1000: {mais1000}')
for c in range(0,len(preç)):
    if c == 0:
        menor = preç[0]
        prodbar = 0
    else:
        if preç[c] < menor:
            menor = preç[c]
            prodbar += 1
print('O produto mais barato foi -{}- e custou: R${:.2f}'.format(prod[prodbar],menor))
continuarug = input('Obrigado por comprar!!!')