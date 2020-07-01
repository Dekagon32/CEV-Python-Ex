aluno = {}

aluno['nome'] = input('Nome: ')
aluno['nota'] = float(input('Nota: '))
aluno['passou'] = 'passou' if aluno['nota'] >= 7.0 else False
if aluno['passou'] == False:
    if aluno['nota'] < 5:
        aluno['passou'] = 'lixo'
print('O aluno {}'.format(aluno['nome']),'passou' if aluno['passou'] == True else 'reprovou','com nota {}.'.format(aluno['nota']))
