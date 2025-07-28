while True:
    print ('-_' * 20)
    num = int(input('Digite um número para ver sua tabuada: '))
    cont = 1
    if num > 0:
        while cont <= 10:
            print (f'{cont} x {num} = {cont * num}')
            cont += 1
    else:
        break
print('Programa encerrado!')
