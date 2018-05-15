n1 = float(input('1º valor: '))
n2 = float(input('2º valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, \no produto é {} \ne a divisão é {}'.format(s,m,d), end=' -> ')
print('dívisão inteira {} e potência {}'.format(di,e))