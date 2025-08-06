from random import randint
from operator import itemgetter
from time import sleep
jogo = {'player01': randint(1,6), 'player02': randint(1,6), 'player03': randint(1,6), 'player04': randint(1,6)}
print('Valores sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.5)

ranking = {}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)
print('-' * 30)
print('Resultados: ')
for c in range(0, len(ranking)):
    print(f'Em {c + 1}º lugar: {ranking[c][0]} com {ranking[c][1]} pontos')