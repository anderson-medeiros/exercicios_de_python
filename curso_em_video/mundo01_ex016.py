"""
# Quebrando um número

Crie um programa que leia um número real qualquer pelo teclado e mostre na
tela a sua porção inteira.
"""
from math import trunc


numero = float(input('Insira um número real: '))
print(trunc(numero))

