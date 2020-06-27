player = {}
player['nome'] = input('Nome: ')
player['qpartidas'] = int(input('Partidas jogadas: '))
player['jogos'] = []
for jogo in range(1,player['qpartidas']+1):
    player['jogos'].append(int(input(f'  Gols{jogo}: ')))

print('-+'*15)

print('nome: {}\nPartidas jogadas: {}'.format(player['nome'],player['qpartidas']))
for e,c in enumerate(player['jogos']):
    print(f'  Partida {e+1}: {c}')
print('Total: {}'.format(sum(player['jogos'])))
