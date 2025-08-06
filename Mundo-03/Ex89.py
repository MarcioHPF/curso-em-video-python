lista = []
alunos = []
cont=0
while True:
    cont += 1
    alunos.append(cont)
    alunos.append(str(input('Nome: ')).strip().capitalize())
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    media = (alunos[2] + alunos[3])/2
    alunos.append(media)
    lista.append(alunos[:])
    alunos.clear()
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if opc == 'N':
        break

print('-' * 40)
print('Nº','Aluno',' ' * 23,'Média')
print('-' * 40)

for aluno in lista:
    print(f'{aluno[0]}', end='  ')
    print(f'{aluno[1]:.<30}', end='')
    print(f' {aluno[4]:>5.2f}')

print('-' * 55)
while True:
    nota = int(input('Deseja saber a nota de qual aluno? [999 para sair]: '))
    if nota == 999:
        print('Programa encerrado!')
        break
    else:
        print(f'Notas de {lista[nota - 1][1]}: {lista[nota - 1][2]}, {lista[nota - 1][3]}')
        print('-' * 55)
