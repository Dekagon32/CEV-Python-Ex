from random import randint

def lin():
    print('-'*15)
def con():
    continuarug = input('digite <enter> para continuar...')

o = 'bunda'
t = 1
lin()
print('Advine'+'-'*9)
lin()
print('Este programa vai pensar em um número e você vai tentar acertá-lo.')
lin()
con()
rang = int(input('Range1: '))
rang2 = int(input('Range2: '))
rnum = randint(rang,rang2)

while o != rnum:
    o = int(input('Digite o número: '))
    if o == rnum:
        break
    else:
        t += 1
        print('Errou...')

print('Você acertou!!!!!\nO número era {}\nVocê conseguiu em {} tentativa(s)'.format(rnum,t))