# Escreva um algoritmo que calcule a média dos números pares de 1 até 100 (1 e 100 inclusos). Implemente o laço usando for.

def realce(s1):
    tam = len(s1)
    if tam:
        print('♦', '-'*tam, '♦')
        print('|', s1, '|')
        print('♦', '-'*tam, '♦')


realce('Exercicios 4.3.1')
print()
qtd = 0
soma = 0
for i in range(1,101):
    if (i % 2 == 0):
       soma += i
       qtd +=1

media = (soma / qtd)
print(' Quantidade de números pares de 0 a 100   →   {} \n Média dos números pares de 0 a 100       →   {:.0f}'.format(qtd, media))