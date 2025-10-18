# 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de
# desconto.

preco_produto = float(input('Digite o preço do produto: '))

desconto = preco_produto * 0.05
preco_desconto = preco_produto - desconto

print('O produto tem como preço {:,.2f} meticais, e com desconto de 5% ({:,.2f}) o ' \
'preço passa a ser {:,.2f} meticais.'.format(preco_produto, desconto, preco_desconto))