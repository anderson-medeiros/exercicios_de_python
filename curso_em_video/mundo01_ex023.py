"""
# Separando dígitos de um número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados.

Ex:
Digite um número: 1834
unidade: 4, dezena: 3, centena: 8, milhar: 1
"""


numero = int(input('Informe um número entre 0 e 10000: '))
if 0 <= numero < 10000:
    print(f'Analisando o número {numero}')
    print(f'Unidade: {numero // 1 % 10}')
    print(f'Dezena:  {numero // 10 % 10}')
    print(f'Centena: {numero // 100 % 10}')
    print(f'Milhar:  {numero // 1000 % 10}')
else:
    print('O número não esta dentro do limite')

