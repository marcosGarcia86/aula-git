'''
faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
que cada litro de tinta pinta uma área de 2m².
'''

largura = float(input('largura da parede em metros: '))
altura = float(input('altura da parede em metros: '))

area = largura * altura
tinta = area / 2

print('Dimensões {}x{} com área de {:.1f}m².'.format(largura,altura,area))
print('Precisará de {:.1f}L de tinta.'.format(tinta))