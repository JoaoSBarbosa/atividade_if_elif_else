print()
print(' -'*15,'Exercício 02 Saiba Mais','-'*18)
print()
print(' Reescreva o programa dos números pares, mas agora em vez de obter números pares,'
      'escreva na tela os 10 primeiros valores múltiplos de 3 \n')


x = 1

while x <= 30:
    if x % 3 == 0:
        print('► ', x)
    x = x + 1