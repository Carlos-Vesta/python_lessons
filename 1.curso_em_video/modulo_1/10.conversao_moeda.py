# 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e mostre quantos
# Dólares ela pode comprar.
# Considere:
# USD 1.00 = 63.00MT

moeda_metical = float(input('Digite quanto tens em metical, para saber quantos dólarespodes comprar: '))

moeda_dolar = moeda_metical / 63

print('{:,.2f} MT pode comprar {:,.2f} USD'.format(moeda_metical, moeda_dolar))