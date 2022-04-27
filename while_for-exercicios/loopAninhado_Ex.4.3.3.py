# Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10 e, para cada número,
# calcule a tabuada multiplicando-o pelo intervalo de 1 até 10. Implementação com dois whil
import borda_modulo
print()
borda_modulo.realce(' Exercícios 4.3.3- Tabuada usando loop aninhado')
print()
tab = 1

while (tab <= 10):
    print('\nTabuada do {}\n '.format(tab))
    i = 0
    while (i < 11):
        print('{} X {} = {}'.format(tab, i, tab*i))
        i += 1
    tab += 1
print()
borda_modulo.realce('FIM')