numbertag = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','desesseis','desessete','desoito','desenove','vinte')
while True:
    num = int(input('Digite um número: '))
    try:
        print(f'Você digitou o número {numbertag[num]}.')
        break
    except:
        print('Você digitou um número errado, tente novamente.')