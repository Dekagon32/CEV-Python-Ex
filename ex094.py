peopleList = []
idades = 0
while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo[M/F]: ')[0].upper()
        if pessoa['sexo'] not in ['M','F']:
            print('Por favor, insira um valor correto.')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']
    peopleList.append(pessoa.copy())
    del pessoa
    while True:
        respond = input('Quer continuar? ')[0].upper()
        if respond not in ['S','N']:
            print('Por favor, insira somente \'Não\' ou \'Sim\'.')
        else:
            break
    if respond == 'N':
        break

mi = idades/len(peopleList)
print('Pessoas Cadastradas: {}'.format(len(peopleList)))
print('Média de Idade: {:.2f}'.format(mi))
print('Mulheres Cadastradas: ',end='')
for people in peopleList:
    if people['sexo'] == 'F':
        print(people['nome'],end=' ')
print('\nIdade Acima da média: ',end='')
for c in peopleList:
    if c['idade'] > mi:
        print('{}({}) '.format(c['nome'],c['idade']),end='')
print()
print('{:^10}|{:^10}|{:^10}'.format('NOME','SEXO','IDADE'))
for p in peopleList:
    print('{:^10}|{:^10}|{:^10}'.format(c['nome'],c['sexo'],c['idade']))
