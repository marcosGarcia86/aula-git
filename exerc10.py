'''
crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar
considerar US$ = 3.27
***melhorar com crawler e capturar cotação do dia***
'''

car = float(input('valor em carteira: R$ '))
dolar = car / 3.27

print('valor em dólares US$ {:.2f}'.format(dolar))