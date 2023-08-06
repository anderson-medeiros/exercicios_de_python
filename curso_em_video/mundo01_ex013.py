"""
# Reajuste Salarial

Faça um algoritimo que leia o salário de um funcionário e mostre seu novo
salário com 15% de aumento.
"""
salario = float(input('Qual é o salário do funcionário? R$'))
aumento = (15 / 100) * salario
novo_salario = salario + aumento

print(
    f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento,'
    f' passa a receber R${novo_salario:.2f}')

