# 1 - Criar um script Python que leia o nome de uma pessoa, e mostra uma mensagem de boasvindas de acordo com o valor digitado.
# Ex: Olá Carlos! Prazer em te conhecer.

nome = str(input('Digite o seu nome: '))

print('Olá {}! Prazer em te conhecer.'.format(nome))