from random import randint
numpc = randint(1,3)
print(f'{' Pedra, Papel ou Tesoura? ':-^40}')
print('''Para jogar escolha:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Digite a sua escolha: '))
print(f'{'':-^40}')
if jogador == 1:
    print(f'Você escolheu Pedra!')
    if numpc == 1: 
        print('O computador também escolheu Pedra!\033[33m EMPATOU!')
    elif numpc == 2:
        print('O computador escolheu Papel!\033[31m Você PERDEU!')
    else:
        print('O computador escolheu Tesoura!\033[32m Você GANHOU!')
elif jogador == 2:
    print('Você escolheu Papel!')
    if numpc == 1: 
        print('O computador escolheu Pedra!\033[32m Você GANHOU!')
    elif numpc == 2:
        print('O computador escolheu Papel!\033[33m EMPATOU!')
    else:
        print('O computador escolheu Tesoura!\033[31m Você PERDEU!') 
elif jogador == 3:
    print('Você escolheu Tesoura!')
    if numpc == 1: 
        print('O computador escolheu Pedra!\033[31m Você PERDEU!')
    elif numpc == 2:
        print('O computador escolheu Papel!\033[32m Você GANHOU!')
    else:
        print('O computador também escolheu Tesoura!\033[33m EMPATOU!')
