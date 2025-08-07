pessoas = {}
lista = []
tot = 0
while True:
    pessoas['Nome'] = str(input('Nome: ')).strip().capitalize()
    
    while True:
        pessoas['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        else:
            print('Erro! Digite apenas M/F! ')
    
    pessoas['Idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    
    if opc == 'N':
        break

print('-'*50)

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
for pessoa in lista:
    tot += pessoa['Idade']

media = tot/len(lista)

print(f'B) A média da idade das pessoas é {media:.2f}')

print('C) As mulheres cadastradas foram: ', end='')
for pessoa in lista:
    if pessoa['Sexo'] == 'F':
        print(pessoa['Nome'], end=' ')
print(f'\nD) Lista das pessoas que estão acima da média: ')

for pessoa in lista:
    if pessoa['Idade'] > media:
        for chave, valor in pessoa.items():
            print(' ' * 4,f'{chave}: {valor};', end= ' ') 
        print()
print('Fim do programa.')
