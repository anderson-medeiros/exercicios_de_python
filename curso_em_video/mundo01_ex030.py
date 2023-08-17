"""
# Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é
PAR ou ÍMPAR.
"""
numero = int(input('Me diga um número: '))
print(f'{numero} é um número {"par" if not numero % 2 else "impar"}')

