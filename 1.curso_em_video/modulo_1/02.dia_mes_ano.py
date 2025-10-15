# 2 - Criar um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa, e mostra
# uma mensagem com a data formatada.
# Ex: Você nasceu no dia 4 de Dezembro de 1988. Correcto?

dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')

print('Você nasceu no dia {} de {} de {}. Correcto?'.format(dia, mes, ano))