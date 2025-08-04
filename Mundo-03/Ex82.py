lista = []
par = []
impar = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    opc = ' '
    while opc not in 'NS':
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if opc == 'N':
        break

print('-' * 30)
print(f'Lista com os números digitados: {lista}')
print(f'Lista dos números pares digitados: {par}')
print(f'Lista com os números ímpares digitados: {impar}')