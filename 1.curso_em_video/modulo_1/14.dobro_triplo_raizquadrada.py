# 14. Crie um algoritmo que leia um numero e mostre na tela o seu dobro, triplo e raiz quadrada.

numero = float(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)

print('O número {} tem como dobro {}, triplo {} e raiz quadrada {}'.format(numero, dobro, triplo, raizQuadrada))