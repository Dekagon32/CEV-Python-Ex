from random import randint
from time import sleep

print('-'*30)
print('IMPAR OU PAR')
print('-'*30, '\n')
while True:
    cont = 0
    ordchose = []
    ordp = []
    ordc = []
    while True:
        while True:
            ppi = str(input('Par ou Impar? [P/I]: '))
            if (ppi.strip())[0].lower() == 'i':
                ordchose.append('Impar')
                ppi = 1
                cpi = 0
                break
            elif (ppi.strip())[0].lower() == 'p':
                ordchose.append('Par')
                ppi = 0
                cpi = 1
                break
        while True:
            pnum = int(input('Digite o número: '))
            if pnum >= int(0):
                ordp.append(str(pnum))
                cnum = randint(0,pnum*2)
                ordc.append(str(cnum))
                break
        
        cp = pnum + cnum
        print('-'*30)
        print(f'O número digitado foi {pnum}.\nO escolhido pelo computador foi {cnum}.\nO total é {cp}.')
        print('-'*30)
        if cp % 2 == ppi:
            print('Parabéns, você ganhou!!!\nVamos novamente!')
            cont += 1
            print('-'*30)
        else:
            break
    print('-'*30)
    print('Que pena, você perdeu.\n \nVezes acertadas: {}\nOrdem de escolha: {}\nOrdem de números(P): {}\nOrdem de números(C): {}'.format(cont,ordchose,ordp,ordc))
    continuarug = str(input('Quer tentar novamente?[S/N]: '))
    if (continuarug.strip())[0].lower() == 'n':
        print('Obrigado por jogar!!!')
        sleep(1.5)
        break
