'''
faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
'''

prod = float(input('Valor do produto R$: '))
desc = ((prod * 5)/100)

print('Valor com desconto\nR$ {:.2f}'.format(prod-desc))