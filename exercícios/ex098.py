import time
def contador(ini,fim,passo):
    if ini > fim and str(passo)[0] != '-':
        passo = int('-'+str(passo))
    if passo != 0:
        print('-'*30)
        for c in range(ini,fim+(1 if str(passo)[0] != '-' else -1),passo):
            print(f'{c}',end='.. ')
            time.sleep(0.5)
        print('\n'+('-'*30))
    else:
        print('Erro!!! não é possível executar 0 passos!')
contador(0,10,1)
contador(10,0,2)
contador(int(input('Início: ')),int(input('Fim: ')),int(input('Passos: ')))