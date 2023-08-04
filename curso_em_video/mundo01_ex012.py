"""
# Calculando Descontos

Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com
5% de desconto.
"""

preco = float(input('Qual é o preço do produto? R$'))
desconto = 5
novo_preco = preco - (desconto / 100) * preco

print(f'''\
O produto que custava R${preco:.2f}, na promoção com desconto de {desconto}% \
vai custar R${novo_preco:.2f}''')

