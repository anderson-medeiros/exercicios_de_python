"""
# Aluguel de Carros


Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
pagar. Sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.
"""

dias_alugado = int(input('Quantos dias alugados? '))
distancia_percorrida = float(input('Quantos Km rodados? '))
custo_dia = 60
custo_km = 0.15
divida = (distancia_percorrida * custo_km) + (dias_alugado * custo_dia)

print(f'O total a pagar é de R${divida:.2f}')

