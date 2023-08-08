"""
# Analisandor de textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

* O nome com todas as letras maíusculas e mínusculas.
* Quantas letras ao todo (sem considerar espaços).
* Quantas letras tem o primeiro nome.
"""

nome = input('Digite seu nome completo: ').strip()
primeiro_nome = nome.split()[0]

print(f'''\
Analisando seu nome...
Seu nome em maíusculas é {nome.upper()}
Seu nome em mínusculas é {nome.lower()}
Seu nome tem ao todo {len(nome) - nome.count(' ')} letras
Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras''')

