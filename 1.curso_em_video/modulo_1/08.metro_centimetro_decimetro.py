# 8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e
# milímetros.

metro = float(input('Digite um valor me metros: '))

centimetro = metro * 100
milimetro = metro * 1000

# Número formatado com separador de milhar (,) e duas casas decimais de ponto flutuante (.2f)
print('O valor {:,.2f} em metros, corresponde a {:,.2f} cintímetros e {:,.2f} milímetros'.format(metro, centimetro, milimetro))