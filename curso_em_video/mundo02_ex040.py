"""
# Aquele clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:

* Média abaixo de 5.0: Reprovado
* Média entre 5.0 e 6.9: Recuperação
* Média 7.0 ou superior: Aprovado
"""


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print(f'Tirando {n1} e {n2}, a média do aluno é {media}')
print('O aluno está ', end='')
if media < 5:
    print('REPROVADO')
elif media < 7:
    print('em RECUPERAÇÃO')
else:
    print('APROVADO')
