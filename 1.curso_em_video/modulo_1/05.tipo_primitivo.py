# 5 - Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as
# informações possíveis sobre ela.

tipo_primitivo = input('Digite algo pelo teclado e veja de que tipo é: ')

print('O tipo primitivo desse valor é: ', type(tipo_primitivo))
print('Só tem espaços? ', tipo_primitivo.isspace())
print('É um número? ', tipo_primitivo.isnumeric())
print('É alfabético? ', tipo_primitivo.isalpha())
print('É alfanumérico? ', tipo_primitivo.isalnum())
print('Está em maiúsculas? ', tipo_primitivo.isupper())
print('Está em minúsculos? ', tipo_primitivo.islower())
print('Está capitalizada? ', tipo_primitivo.istitle())