# 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua Área
# e quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de
# dois metros ao quadrado (2m * m).

largura = float(input('Digite o valor da largura da parede em metros: '))
altura = float(input('Digite o valor da altura da parede em metros: '))

area = largura * altura
quantidade_tinta = area / 2

print('Uma parede com {:.2f} metros de largura e {:.2f} metros de altura, tem uma área de {:.2f} metros quadrados, ' \
'e necessita de {:.2f} litros de tinta para pinta-la.'.format(largura, altura, area, quantidade_tinta) )