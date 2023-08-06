"""
# Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""
from math import sqrt


catetoA = float(input('Insira a medida do cateto oposto: '))
catetoB = float(input('Insira a medida do cateto adjacente: '))

hipotenusa = sqrt(catetoA ** 2 + catetoB ** 2)
print(f'A hipotenusa vale {hipotenusa:.2f}')

