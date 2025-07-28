from random import randint
cont = 0
print('-_-' * 10)
print(f'{'Jogo do Par ou Ímpar':^30}')
print('-_-' * 10)
print('Vamos jogar!')
while True:
    pc = randint(0,10)
    jogador = int(input('Digite um valor: '))
    par = str(input('Par ou ímpar?[P/I] ')).upper().strip()[0]
    if (pc + jogador) % 2 == 0:
        if par == 'P':
            cont += 1
            print(f'Você escolheu {jogador} e o computador, {pc}. O total é {pc + jogador} que é par. Você venceu!')
            print('QUERO REVANCHE!')
            print('-' * 40)
        else:
            print(f'Você escolheu {jogador} e o computador, {pc}. O total é {pc + jogador} que é par. Você perdeu!')
            break
    else:
        if par == 'I':
            cont += 1
            print(f'Você escolheu {jogador} e o computador, {pc}. O total é {pc + jogador} que é ímpar. Você venceu!')
            print('QUERO REVANCHE!')
            print('-' * 75)
        else:
            print(f'Você escolheu {jogador} e o computador, {pc}. O total é {pc + jogador} que é ímpar. Você perdeu!')
            break

print(f'Cansei de jogar! Você ganhou {cont} vezes') if cont > 1 else print(f'Você não conseguiu nem uma vez! Não quero jogar mais.')
