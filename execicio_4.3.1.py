soma = 0
qtd = 0
for i in range(1,101):
    if ( i % 2 == 0):
        soma = soma + i
        qtd = qtd + 1
media = soma / qtd
print('\n A quantidade de números pares foi de: {} \n A soma: {} \n A média desses números foi de: {}  '.format(qtd, soma, media))