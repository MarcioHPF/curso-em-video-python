from random import shuffle
alunos = []

for aluno in range (1,5):
    alunos.append(input(f'Digite o nome do {aluno}° aluno: '))
shuffle(alunos)

print(f'A ordem de apresentação dos alunos é {alunos}')
