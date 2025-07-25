num = int(input('Digite um número para descobrir o fatorial dele: '))
cont = num
fat = 1
print(f'{num}! = ', end= '')
while cont > 1:
    print(f'{cont} x', end=' ')
    fat = fat * cont
    cont -= 1
    if cont == 1:
        print('1', end=' = ' )
print(fat)
