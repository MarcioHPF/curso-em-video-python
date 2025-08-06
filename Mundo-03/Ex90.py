notas = {}

notas['Nome'] = str(input('Digite o nome do aluno: ')).strip().capitalize()
notas['Média'] = float(input('Digite a média do aluno: '))

if notas['média'] < 6:
    notas['situação'] = 'Reprovado'
else:
    notas['situação'] = 'Aprovado'

print('-' * 30)
for k,v in notas.items():
    print(f'{k}: {v}')