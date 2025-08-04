cont = 0
lista = []
while True:
    cont += 1
    num = int(input('Digite um número: '))
    lista.append(num)
    opc = ' '
    while opc not in "NS":
        opc = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if opc == 'N':
        break    

lista.sort(reverse= True)
print('-' * 30)
print(f'Foram digitados {cont} números.')
print(lista)
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')