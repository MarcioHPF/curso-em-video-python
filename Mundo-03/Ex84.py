menor = maior = 0
lista = []
pessoas = []
while True:
    pessoas.append(str(input('Digite o nome: ')).strip().capitalize())
    pessoas.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        menor = maior = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    opc = ' '
    while opc not in 'NS':
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'Foram adicionadas {len(lista)} pessoas na lista')
print('As pessoas com maior peso são: ', end=' ')
for c in lista:
    if c[1] == maior:
        print(f'{c[0]}', end= ' ')
print('\nAs pessoas com menor peso são: ', end=' ')

for c in lista:
    if c[1] == menor:
        print(f'{c[0]}', end= ' ')
