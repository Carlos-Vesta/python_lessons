# 14 - Crie um programa que leia um numero Real qualquer pelo teclado, e mostre na tela a sua
# porção inteira.
# Ex: Digite um número: 3.365
# O número 3.365 tem a parte inteira 3.

import math

numero = float(input('Digite um número real qualquer: '))

print('O numero {}, tem como porção inteira {}'.format(numero, math.trunc(numero)))