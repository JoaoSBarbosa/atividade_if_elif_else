# Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final.
# Para este intervalo especificado pelo usuário, calcule na tela:
# A) A quantidade de números inteiros e positivo;
# B) A quantidade de números pares;
# C) A quantidade de números ímpares;
# D) A respectiva média de cada um dos itens anteriores

qtd_positivo = 0
soma_positivos = 0
qtd_pares = 0
soma_pares = 0
qtd_impares = 0
soma_impares = 0

inicial = int(input(' \n Digite o valor inicial: '))
final = int(input(' Digite o valor final : '))
print()
cont = inicial

if (inicial < final):  # Verificar se os números estarão em ordem crescente
    while (cont <= final):  # Enquanto o valor inicial for menor ou diferente do final, faça:

        if (cont > 0):  # Condicional para verificar se o número é positivo
            qtd_positivo = qtd_positivo + 1  # Será somado na variável qtd_positivo + 1 toda ves que essa condição for verdadeira
            soma_positivos = soma_positivos + cont  # Será somado também na variável soma_positivo todos os números positivos enquanto essa condição for TRUE

        # Aqui será realizado os mesmos passos do If anterior, mas dessa vez com números pares

        if (cont % 2 == 0):
            qtd_pares = qtd_pares + 1
            soma_pares = soma_pares + cont

        # Aqui será realizado o mesmo processo dos ifs anteriores, mas dessa vez apenas com os números impares

        else:
            qtd_impares = qtd_impares + 1
            soma_impares = soma_impares + cont

        # Limitador para o valor inicial chegar até o valor final e parar o loop

        cont = cont + 1

    # Processamento para obter as médias

    media_positivo = soma_positivos / qtd_positivo
    media_pares = soma_pares / qtd_pares
    media_impares = soma_impares / qtd_impares

    # Saída de dados para o usuário
    print('▬'*30)
    print(' Quantidade de números positivo {} \n Média dos números positivos:   {:.0f}'.format(qtd_positivo,
                                                                                             media_positivo))
    print('▬'*30)
    print(' Quantidade de números pares: {} \n Média de números pares:      {:.0f} '.format(qtd_pares, media_pares))
    print('▬'*30)
    print(' Quantidade de números ímpares: {} \n Média dos números ímpares:     {:.0f} '.format(qtd_impares, media_impares))
    print('▬'*30)
    print('                   ◄ FIM ►')

else:
    print(' Você digitou um valor inicial maior ou igual ao valor final \n Encerrando o programa ! ')
