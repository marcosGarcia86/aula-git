'''
faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento.
'''

sal = float(input('Salário R$: '))
novo = (sal * 75)/100

print('Novo salário R$: {:.2f}'.format(sal+novo))