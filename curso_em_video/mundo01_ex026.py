"""
# Primeira e última ocorrência de uma string

Faça um programa que leia uma frase pelo teclado e mostre:
* Quantas vezes aparece a letra "A".
* Em que posição ela aparece a primeira vez.
* Em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ').strip().lower()
print(f'''\
A letra A aparece {frase.count('a')} vezes na frase.
A primeira letra A apareceu na posição {frase.find('a')}.
A última letra A apareceu na posição {frase.rfind('a')}.''')

