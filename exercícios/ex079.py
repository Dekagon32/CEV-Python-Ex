numbers = []
while True:
    n = int(input('Digite o termo: '))
    if n not in numbers:
        numbers.append(n)
        print('Valor adicionado com sucesso.')
    elif n in numbers:
        print('Valor já existe. Não adicionado')
    con = input('Quer continuar?[S/N]')
    if con in 'Nn':
        break
print('-'*38)
numbers = sorted(numbers)
print('Os valores adicionados foram {}'.format(numbers))
