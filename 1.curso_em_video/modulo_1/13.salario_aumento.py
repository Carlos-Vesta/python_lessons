# 13 - Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salario, com
# 15% de aumento.

salario = float(input('Digite o salário do funcionário: '))

aumento = salario * 0.15
salario_aumento = salario + aumento

print('O salário do funcionário é {:,.2f} meticais, e com aumento de 15% ({:,.2f}) ' \
'passa a ser {:,.2f} meticais.'.format(salario, aumento, salario_aumento))
