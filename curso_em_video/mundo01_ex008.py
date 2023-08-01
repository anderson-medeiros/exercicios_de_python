"""
# Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros.
"""

distancia = float(input('Insira uma distância em metros: '))

# km hm dam m dm cm mm
msg = f'''\
A medida de {distancia}m corresponde a
{distancia / 1000}km
{distancia / 100}hm
{distancia / 10}dam
{distancia * 10}dm
{distancia * 100}cm
{distancia * 1000}mm
'''
print(msg)

