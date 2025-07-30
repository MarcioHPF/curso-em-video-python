print('-' * 30)
print(f'{'BANCO CENTRAL':^30}')
print('-' * 30)
saque = int(input('Valor a ser sacado: R$'))
total = saque
cedula = 50
totced = 0
while True:
    
    if total >= cedula:
        total = total - cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de cédulas de R${cedula},00: {totced}')

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
