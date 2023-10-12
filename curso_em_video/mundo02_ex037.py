"""
# Conversor de Bases Númericas

Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão.

1. para binário
2. para octal
3. para hexadecimal
"""


numero = int(input('Digite um número inteiro: '))

print(f'''\
Escolha uma das bases númericas para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {numero:b}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {numero:o}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {numero:x}')
else:
    print('Opção inválida, tente novamente.')
