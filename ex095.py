jogadores = []
while True:
    soma = 0
    player = {}
    player['nome'] = input('Nome: ').title()
    player['qpartidas'] = int(input('Partidas jogadas: '))
    player['jogos'] = []
    for c in range(1,1+player['qpartidas']):
        player['jogos'].append(int(input(f'  Gols na {c}ª partida: ')))
        soma += player['jogos'][c-1]
    player['somagol'] = soma
    jogadores.append(player.copy())
    res = input('Quer Continuar? [S/N] ').strip()[0].upper()
    if res == 'N':
        break
print('-'*30)
print('{:<3}|{:<20}|{:<20}|{:<5}'.format('COD','NOME','GOLS','TOTAL'))
for e,c in enumerate(jogadores):
    print(f'{e:<3}|{c["nome"]:<20}|{c["jogos"]!s
          :<15s}|{c["somagol"]:<5}')
print('-'*30)
while True:
    while True:
        dad = int(input('Mostrar dados de qual jogador? '))
        if dad > len(jogadores)-1:
            print(f'Não existe jogador com código {dad}')
        else:
            break
    if dad == 999:
        break
    print(' -- Levantamento de {}'.format(jogadores[dad]['nome']))
    for e,v in enumerate(jogadores[dad]):
        print('    {} gols no jogo {}'.format(v['jogos'][e],e+1))
