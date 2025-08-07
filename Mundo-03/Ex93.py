lista = {}
cont = total = 0
gols = []

lista['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
jogos = int(input(f'Quantos jogos o {lista["Nome"]} jogou? '))

while cont < jogos:
    gols.append(int(input(f'Quantos gols no {cont + 1}º jogo ? ')))
    cont+= 1

lista['Gols'] = gols

lista['Total'] = sum(gols)
print('-' * 45)
print(lista)

print('-' * 45)
for chave, valor in lista.items():
    print(f'O campo {chave} tem o valor {valor}')

print('-' * 45)

print(f'O jogador {lista["Nome"]} jogou {jogos} jogos.')
for c in range(0,len(gols)):
    print(f'Na partida {c+1}, fez {gols[c]} gols.')

print(f'Totalizando {lista["Total"]} gols.')
