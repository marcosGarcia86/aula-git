'''
desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
a sua média
'''

n1 = float(input('digite sua 1º nota: '))
n2 = float(input('digite sua 2º nota: '))

media = (n1 + n2) / 2

print('sua média é {:.2f}'.format(media))
if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')