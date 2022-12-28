#  Sorteiro de alunos

from random import choice, randint

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno escolhido foi {alunos[randint(0, 3)]}.')
