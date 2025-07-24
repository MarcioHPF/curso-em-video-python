maior = menor = 0

for c in range(0, 5):
    peso = float(input(f'Insira o peso da {c + 1}ª pessoa:'))
    if peso > maior:
        maior = peso

    if c == 0:
        menor = peso
    else:
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi: {maior}kg \nO menor peso lido foi {menor}kg')