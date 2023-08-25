"""
Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
"""

r1 = int(input('Primeiro seguimento: '))
r2 = int(input('Segundo seguimento: '))
r3 = int(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('É possivel criar um triângulo')
else:
    print('Não é possível criar um triângulo')

