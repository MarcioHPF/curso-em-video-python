from random import choice

a1 = input('Digite o nome do primeiro aluno(a): ')
a2 = input('Digite o nome do segundo aluno(a): ')
a3 = input('Digite o nome do terceiro aluno(a): ')
a4 = input('Digite o nome do quarto aluno(a): ')

alunos = [a1,a2,a3,a4]

print(f'O aluno escolhido é {choice(alunos)}')
