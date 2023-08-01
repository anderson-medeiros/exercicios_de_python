"""
# Tabuada

Faça um programa que leia um número inteiro qualquer e mostre na tela a sua
tabuada.
"""

n = int(input('Digite um número inteiro para ver sua tabuada: '))
msg = f'''\
{n} x {1:2} = {n * 1}
{n} x {1:2} = {n * 2}
{n} x {1:2} = {n * 3}
{n} x {1:2} = {n * 4}
{n} x {1:2} = {n * 5}
{n} x {1:2} = {n * 6}
{n} x {1:2} = {n * 7}
{n} x {1:2} = {n * 8}
{n} x {1:2} = {n * 9}
{n} x {1:2} = {n * 10}
'''

print(msg)
