from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for c in range(0,5):
        lista.append(randint(1,10))
        print(lista[c], end=' ', flush=True)
        sleep(0.5)

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = []
sorteia(números)
print()
somaPar(números)
