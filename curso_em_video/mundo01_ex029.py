"""
# Radar eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R$7,00 por cada Km acima do limite.
"""

limite = 80
velocidade = int(input('Insira a velocidade em que o carro está: '))

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    print(f'A multa foi de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')

