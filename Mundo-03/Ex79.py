numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
    else:
        print('O valor já está na lista.')
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()
    if opc == 'N':
        break
    
numeros.sort()
print(numeros)
