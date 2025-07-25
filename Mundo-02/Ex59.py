from time import sleep

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
opc = 0

while opc != 5:
    print(f'{'':-^40}')
    sleep(0.2)
    print('''\033[33m[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Mudar números
[ 5 ] Sair do programa         
''')
    opc = int(input('Digite a operação desejada: \033[m'))
    print(f'{'':-^40}')
    if opc == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1 + n2}')
    elif opc == 2:
        print(f'A multiplicação de {n1} e {n2} é igual a {n1 * n2}')
    elif opc == 3:
        if n1 > n2:
            print (f'O número {n1} é o maior.')
        elif n2 > n1:
            print(f'O número {n2} é maior.')
        else:
            print('Os números são iguais.')
    elif opc == 4:
        n1 = int(input('Insira um novo número: '))
        n2 = int(input('Insira outro número: '))

print('Fechando programa...')
