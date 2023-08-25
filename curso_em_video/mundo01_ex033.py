"""
# Maior e menor valores

Faça um programa que leia três números e mostre qual é maior e qual é o menor.
"""

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')

