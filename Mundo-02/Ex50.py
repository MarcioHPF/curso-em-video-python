soma = cont = 0

for c in range(0, 6):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'O somatório de todos os {cont} números pares da lista é {soma}')