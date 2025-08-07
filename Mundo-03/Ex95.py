lista_geral = []
cont_jogador = 0

while True:
    jogador = {} 
    gols = []

    cont_jogador += 1
    jogador['Num'] = cont_jogador
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogos = int(input(f'Quantos jogos o {jogador["Nome"]} jogou? '))

    for i in range(0, jogos):
        gols.append(int(input(f'Quantos gols no {i + 1}º jogo? ')))

    jogador['Gols'] = gols
    jogador['Total'] = sum(gols)
    lista_geral.append(jogador)

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if opc == 'N':
        break

print('-' * 50)
print(f'{"Nº":<4}{"Jogador":<15}{"Gols":<25}{"Total":<16}')
print('-' * 50)

for jogador in lista_geral:
    print(f'{jogador["Num"]:<4}{jogador["Nome"]:<15}{str(jogador["Gols"]):<25}{jogador["Total"]:<16}')

while True:
    checa = int(input('Deseja ver o resultado de qual jogador?[999 para sair] '))
    if checa == 999:
        print('Programa encerrado!')
        break
    else:
        if checa > len(lista_geral):
            print('Não existe jogador com esse código!')
        else:
            print(f'Dados do jogador {lista_geral[checa - 1]['Nome']}:')
            for indice, gols in enumerate(lista_geral[checa - 1]['Gols']):
                print(f'    Na partida {indice + 1}, fez {gols} gols;')
