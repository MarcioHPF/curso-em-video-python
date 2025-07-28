maior = menor = cont = soma = 0
opc = ' '

while opc  not in 'N':
    num = int(input('Digite um número: '))
    if cont == 0:
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    soma += num
    opc = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]

print(f'-'*45)
print(f'Você digitou {cont} números')
print(f'O maior número foi o {maior} e o menor foi o {menor}')
print(f'A média dos números é igual a {soma/cont:.2f}')
