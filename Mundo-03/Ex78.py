numeros = []

for c in range(1,6):
    numeros.append(int(input(f'Digite um número para a posição {c}: ')))

print(f'Você digitou os números {numeros}')
print(f'O maior número da lista é o {max(numeros)}, nas posições', end=' ')
for pos, val in enumerate(numeros):
    if val == max(numeros):
        print(f'{pos + 1}', end= ' ')
print(f'\nO menor número da lista é o {min(numeros)}, nas posições', end=' ')
for pos, val in enumerate(numeros):
    if val == min(numeros):
        print(f'{pos + 1}', end= ' ')
