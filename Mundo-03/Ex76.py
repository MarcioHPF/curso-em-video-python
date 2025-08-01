lista = ('Abacate', 4.75, 'Acerola', 1.50, 'Banana', 3.5, 'Beringela', 2.5, 'Cacau', 12.50, 'Cenoura', 3.25)

print('-'*37)
print(f'{' SACOlÃO COMPRE MAIS ':.^37}')
print('-'*37)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>5.2f}')

