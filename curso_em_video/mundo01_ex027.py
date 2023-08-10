"""
# Primeiro e último nome de uma pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""


nome = input('Digite seu nome completo: ').strip().split()

print(f'''\
Muito prazer em te conhecer!
Seu primeiro nome é {nome[0].capitalize()}
Seu último nome é {nome[-1].capitalize() if len(nome) > 1 else '******'}''')

