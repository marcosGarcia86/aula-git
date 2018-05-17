'''
escreva um programa que leia um valor em metros e o exiba convertido em
centimetros e milímetros
'''

mt = float(input('Informe valor em metros: '))
cm = mt * 100
mm = mt * 1000
km = mt / 1000


print('{:.0f} cm \n{:.1f} mm \n{:.2f} km'.format(cm,mm, km))