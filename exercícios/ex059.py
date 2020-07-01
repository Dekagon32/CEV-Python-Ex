from os import system
from time import sleep


def lin(txt):
    print(txt+'-'*(30-int(len(txt))))

opt = '0'
chos = ['1','2','3','4','5']
lin('MenuPython')
while opt != '5':
    opt = '0'
    st = int(input('Digite o primeiro número: '))
    nd = int(input('Digite o segundo número: '))
    lin('')

    while opt not in ['4','5']:
        opt = str(input('(1)Somar\n(2)Multiplicar\n(3)Maior\n(4)Números diferentes\n(5)Sair\n\nDigite sua escolha: ')).strip()
        if opt not in chos:
            system('cls')
            print('Escolha uma opção válida.')

        if opt == '1':
            print('A soma de {} e {} é: {}.'.format(st,nd,st+nd))
        elif opt == '2':
            print('O produto de {} e {} é: {}.'.format(st,nd,st*nd))
        elif opt == '3':
            if st > nd:
                print('Entre {} e {}, {} é o maior.'.format(st,nd,st))
            elif nd > st:
                print('Entre {} e {}, {} é maior.'.format(st,nd,nd))
            elif nd == st:
                print('Os dois são iguais.')
        sleep(2)