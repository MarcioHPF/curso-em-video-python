from random import randint
from time import sleep

numpc = randint(0, 5)
num = int(input('Eu escolhi um número. Tente adivinhar qual número eu escolhi: '))
print('Vamos ver se você acertou...')
sleep(1.5)
print(f'Você acertou! Eu escolhi o número {numpc}!') if num == numpc else print(f'Você errou! Eu escolhi o número {numpc} e não o {num}.')
