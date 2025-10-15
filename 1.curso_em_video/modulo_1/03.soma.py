# 3 - Crie um script em Python que leia dois números e mostre o resultado da soma entre eles.
# Ex: O resultado da soma de 3 e 7 é 10.

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

soma = numero_1 + numero_2

print('O resultado da soma entre {} e {} é {}'.format(numero_1, numero_2, soma))