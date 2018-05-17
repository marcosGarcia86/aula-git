'''
faça um programa que leia um número inteiro qualquer e mostre na tela a sua
tabuada
'''

tab = int(input('Digite um valor inteiro: '))
print('\ntabuada', tab)
i = 0
while i <= 10:
    print('%d x %d = %d' % (tab, i, tab * i))
    tab = tab
    i +=1