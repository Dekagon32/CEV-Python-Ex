pessoas = []
dado = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    r = str(input('Continuar? '))
    if r.lower().strip() == 'n':
        break

for c,pessoa in enumerate(pessoas):
    if c == 0:
        maior = pessoas[c]
        menor = pessoas[c]
    else:
        if pessoa[1] > maior[1]:
            maior = pessoa
        if pessoa[1] < menor[1]:
            menor = pessoa



print('Foram cadastradas {} pessoa'.format(len(pessoas)),end='s\n' if len(pessoas) > 1 else '\n')
print('A lista é: {}'.format(pessoas))
print('O maior é {} com {}Kgs.'.format(maior[0],maior[1]))
print('O menor é {} com {}Kgs.'.format(menor[0],menor[1]))