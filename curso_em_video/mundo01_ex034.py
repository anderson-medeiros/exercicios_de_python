"""
# Aumentos múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor 
de seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de
10%. Para os inferiores ou iguais, o aumento e de 15%.
"""


salario = float(input('Informe o salário do funcionário: R$'))
salario_extra = salario * (15 if salario <= 1250 else 10 ) / 100

print(f'''\
Houve um aumento de R${salario_extra:.2f}
Agora o funcionário receberá R${salario + salario_extra:.2f}''')

