from random import randint
from time import sleep
pc = randint(1,10)
cont = 1
print('O computador está escolhendo um número entre 0 e 10...')
sleep(0.5)
jogador = int(input('Pronto! Agora tente acertar o número que ele escolheu: '))

while jogador != pc:
    cont += 1
    if jogador > pc:
        jogador = int(input('\033[31mTenta um menor! Faça outro palpite: '))
    else:
        jogador = int(input('\033[31mTenta um maior! Faça outro palpite: '))

if cont == 1:
    print(f'\033[32mParabéns! Você acertou de primeira! O computador escolheu o número {pc}!')
else:
    print(f'\033[32mParabéns! O computador escolheu o número {pc}! Você conseguiu com {cont} palpites!')
