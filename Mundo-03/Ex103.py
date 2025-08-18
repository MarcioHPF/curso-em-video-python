def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s).')


jogador = str(input('Digite o nome do jogador: ')).capitalize().strip()
gol = input('Digite o número de gols do jogador: ')
if gol.isnumeric():
    int(gol)
else:
    gol = 0

if jogador == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
