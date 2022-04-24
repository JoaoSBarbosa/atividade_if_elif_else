# Escreva um algoritmo que leia dois valores na tela o resultado da multiplicação de ambos.
# Entretanto, para calcular a multiplicação, utilize somente operação de soma e subtração

x = int(input(' Digite um valor: '))
y = int(input(' Digite outro valor: '))

cont = 1
mult = 0

while (cont <= x):   # Enquanto contador for menor que o primeiro nº digitado, y será somado com ele mesmo
    mult = mult + y  # Y será somado com ele mesmo 'x' vezes mesma coisa que 5x3 que é 5x5x5
    cont = cont + 1  # Limitador para o contador chegar ao valor do 1º nº digitado e parar
print(' Resultado da multiplicação: {} x {} = {}'.format(x, y, mult))
