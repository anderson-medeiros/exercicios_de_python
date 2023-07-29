"""
# Dissecando uma variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele.
"""

entrada = input('Digite algo: ')
print(f'''\
tipo {type(entrada)}
alfanúmerico? {entrada.isalnum()}
alfabético: {entrada.isalpha()}
ascii: {entrada.isascii()}
decimal: {entrada.isdecimal()}
digíto: {entrada.isdigit()}
indentificavel: {entrada.isidentifier()}
minúsculo: {entrada.islower()}
numérico: {entrada.isnumeric()}
imprimível: {entrada.isprintable()}
espaço: {entrada.isspace()}
título: {entrada.istitle()}''')

