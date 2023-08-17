"""
# Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele e BISSEXTO.
"""
ano = int(input('Insira um ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('Ano bissexto')
elif (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
    print('Ano bissexto')
else:
    print('Ano normal')

