# 7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

nota_1 = float(input('Digite a primira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2

print('As notas e a média do aluno são: \nNOTA 1 = {} \nNOTA 2 = {} \nMÉDIA = {}'.format(nota_1, nota_2, media))