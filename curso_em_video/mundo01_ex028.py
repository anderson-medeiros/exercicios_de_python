"""
# Jogo da adivinhação v.1.0

Escreva um programa que faça o computador "pensar" em um número inteiro entre
0 e 5 e peça para o usuário tentar descubrir qual foi o número escolhido pelo
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep


print(f'''\
{'=' * 60}
Vou pensar em um número entre 0 e 5. Tente adivinhar...
{'=' * 60}''')

numero_aleatorio = randint(0, 5)
numero_jogador = int(input('Em que número eu pensei? '))

print('Processando...')
sleep(3)
if numero_jogador == numero_aleatorio:
    print('Você venceu')
else:
    print('Você perdeu')

