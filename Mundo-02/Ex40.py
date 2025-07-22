notaA = float(input('Digite a nota da primeira prova: '))
notaB = float(input('Digite a nota da segunda prova: '))
media = (notaA + notaB) / 2

print(f'Notas do aluno:\nProva 1: {notaA}\nProva 2: {notaB}\nMédia das provas: {media}')
if media < 5:
    print('Aluno REPROVADO')  
elif media >= 5 and media < 7:
    print('Aluno EM RECUPERAÇÃO') 
else:
    print('Aluno APROVADO')
    