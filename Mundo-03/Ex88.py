from random import randint
lista = []
jogos = []
cont = 0
print('*' * 40)
print(f'{'SORTEADOR DA MEGA SENA':^40}')
print('*' * 40)
qtde_jogos = int(input('Digite a quantidade de jogos desejados: '))

for c in range(0, qtde_jogos):
    for c in range(0,6):
        jogos.append(randint(1,60))
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()

print('-' * 40)
for palpite in lista:
    cont+= 1
    print(f'Jogo {cont}: {palpite}')
