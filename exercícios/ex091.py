from random import randint
from operator import itemgetter

players = {}
rank = dict()
print('Valores sorteados: ')
for c in range(1,5):
    players['p{}'.format(c)] = randint(1,6)
    print('O Player {} tirou {} pontos.'.format(c,players[f'p{c}']))
rank = sorted(players.items(),key=itemgetter(1), reverse=True)
print('-'*27)
for i,v in enumerate(rank):
    print(f'{i+1}º lugar: Player {v[0][1]} com {v[1]} pts.')