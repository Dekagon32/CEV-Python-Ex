from datetime import datetime
now = datetime.now()

pessoa = {}

pessoa['nome'] = input('Nome: ')
pessoa['idade'] = now.year - int(input('Nascimento: '))
pessoa['carteira'] = int(input('Carteira de Trabalho: '))

if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Digite o salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - now.year)
print('-'*60)
for k,v in pessoa.items():
    if k != 'salário':
        print('{:.<15}:{}'.format(k.title(),v))
    else:
        print('{:.<15}:R${:.2f}'.format(k.title(),v))
