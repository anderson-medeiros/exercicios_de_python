"""
# Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se
alistar ou se passou do tempo do alistamento. Seu programa também deverá mostrar
o tempo que falta ou que passou passou do prazo.
"""
from datetime import date


ano_nascimento = int(input('Insira seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
ano_alistamento = 18

if idade < 5 or idade > 120:
    print('Data inválida')
else:
    print(f'Ano de nascimento: {ano_nascimento}')
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < ano_alistamento:
        print(f'Ainda faltam {ano_alistamento - idade} anos para o alistamento')
        print(f'Seu alistamento será em {ano_atual + (ano_alistamento - idade)}')
    elif idade > ano_alistamento:
        print(f'Você já deveria ter se alistado há {idade - ano_alistamento} anos.')
        print(f'Seu alistamento foi em {ano_atual - (idade - ano_alistamento)}.')
