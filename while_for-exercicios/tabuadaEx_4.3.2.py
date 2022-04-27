# Escreva um algoritmo que calcule e exiba a tabuada de um número escolhido e digitado pelo usuário.
# A tabuada deve ser calculada até um determinado número n, também fornecido pelo usuário. Implemente o laço usando for.
import borda_modulo

print()
borda_modulo.realce('  Exercicios 4.3.2-Tabuada  ')
x = int(input(' Digite o valor que deseja calcular a tabuada: '))
y = int(input(' Digite até qual número deseja mostrar a tabuada do {} '.format(x)))
print()
for i in range(0, y+1, 1):
    print(' {} X {} = {}'.format(x, i, x*i))