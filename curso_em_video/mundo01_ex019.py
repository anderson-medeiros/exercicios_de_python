"""
# Sorteando um item na lista

Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno escolhido foi {choice(alunos)}')

