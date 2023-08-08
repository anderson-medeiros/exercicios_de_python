"""
# Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
consseno e tangente desse ânguno.
"""
from math import radians, sin, cos, tan


angulo = int(input('Digite o ângulo que você deseja: '))
radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'''\
O ângulo de {angulo} tem:
SENO de {seno:.2f}
COSSENO de {cosseno:.2f} 
TANGENTE de {tangente:.2f}''')

