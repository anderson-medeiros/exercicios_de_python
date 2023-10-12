"""
# Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_da_casa = float(input('Insira o valor da casa R$'))
salario = float(input('Insira seu salário R$'))
anos = int(input('Em quanto anos você deseja quitar a dívida?'))

pagamento_mensal = valor_da_casa / (12 * anos)
if pagamento_mensal > salario * (30 / 100):
    print('Empréstimo negado')
else:
    print('Empréstimo realizado com sucesso')
