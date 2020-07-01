from time import sleep

print('-'*30)
print('CADASTRO INTELIGENTE do Dévoli')
print('-'*30,end='\n \n')
resposta = 0
pessoas = 0
names = []
ages = []
sexes = []
LISTA = [names, ages, sexes]
while True:
    print('-'*30)
    print('[1]Cadastrar\n[2]Deletar\n[3]Lista\n[4]Estatísticas\n[5]Carregar\n[6]Salvar\n[7]Sair')
    while resposta not in ['1','2','3','4','5','6','7']:
        resposta = str(input('Digite sua escolha: '))
    
    if resposta == '1':
        print('-'*15)
        print('CADASTRO')
        print('-'*15,end='\n \n')
        name = str(input('Nome: ')).title().strip()
        age = input('Idade: ')
        sex = input('Gênero[M/F]: ').strip().upper()[0]
        sex = 'Masculino' if sex == 'M' else 'Feminino'
        names.append(name)
        ages.append(age)
        sexes.append(sex)
        pessoas += 1
        print('\nCadastro Concluído!')
        sleep(1.5)
        print('\n')
    
    if resposta == '2':
        if pessoas == 0:
            print('Não existe ninguém cadastrado.')
            sleep(1.5)
        else:
            print('-'*16)
            print('Pessoas Cadastradas: {}'.format(pessoas))
            print('-'*16)
            for c in range(0,pessoas):
                print('Número {}\n \nNome: {}\nIdade: {}\nSexo: {}'.format(c+1,names[c],ages[c],sexes[c]))
                print('-'*16)
            resposta = int(input('Deletar Número: '))
            if resposta > pessoas or resposta <= 0:
                break
            for c in range(0,3):
                del(LISTA[(c)][resposta-1])
            pessoas -= 1
            print('Deletado com sucesso!')
            sleep(1.5)

    if resposta == '3':
        print('-'*16)
        print('Pessoas Cadastradas: {}'.format(pessoas))
        print('-'*16)
        for c in range(0,pessoas):
            print('Número {}\n \nNome: {}\nIdade: {}\nSexo: {}'.format(c+1,names[c],ages[c],sexes[c]))
            print('-'*16)
        sleep(3)
    
    if resposta == '4':
        esidade = 0
        for c in range(0,len(ages)):
            if int(ages[c]) >= 18:
                esidade += 1
        eshome = 0
        for c in range(0,len(ages)):
            if sexes[c] == 'Masculino':
                eshome += 1
        esmuié20 = 0
        for c in range(0,pessoas):
            if sexes[c] == 'Feminino':
                if int(ages[c]) < 20:
                    esmuié20 += 1
        print('-'*16)
        print('Estatísticas')
        print('-'*16)
        print('Pessoas com mais de 18 anos: {}\nHomens cadastrados: {}\nMulheres com menos de 20 anos: {}'.format(esidade,eshome,esmuié20))
    if resposta in ['5','6']:
        print('Opção ainda não disponível')
        sleep(2)
    if resposta == '7':
        break
    resposta = '0'
