'''
faça um programa que leia um número inteiro e mostre na tela o seu sucessor
e seu antecessor.
'''

n1 = int(input('Digite um número inteiro: '))
sucessor = n1 +1
antecessor = n1 - 1
print('o sucessor de {} é {} \ne o seu antecessor é {}'.format(n1,
sucessor, antecessor))