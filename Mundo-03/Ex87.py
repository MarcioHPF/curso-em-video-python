matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira = maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))

print('-' * 40)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]:^4}', end= ' ')
    print()
print('-' * 40)

for linha in range(0, 3):
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 == 0:
            par+= matriz[linha][coluna]
        if coluna == 2:
            terceira += matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]


print(f'Soma dos valores pares: {par}')
print(f'Soma dos valores da terceira coluna: {terceira}')
print(f'O maior número da segunda coluna é o {maior}')
