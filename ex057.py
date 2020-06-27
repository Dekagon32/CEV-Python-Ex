c = '0'
sx = '0'
while c.lower().strip()[0] not in 'mf':
    c = str(input('Digite seu sexo(M\F): ')).lower()
    if c.strip()[0] == 'm':
        sx = 'Masculino'
    elif c.strip()[0] == 'f':
        sx = 'Feminino'
print(f'O sexo é: {sx}')