# 4 - Crie um programa em Python que leia dois números e mostre o resultado da soma entre eles.
# Ex: A soma entre os números 3 e 5 eh igual a 8.

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

soma = numero_1 + numero_2

print('A soma entre {} e {} é {}'.format(numero_1, numero_2, soma))