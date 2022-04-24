print()
print(' -'*15,' Exercício 03','-'*18)
print('\n Crie um programa que calcule a tabuada de um número escolhido pelo uisuario. Imprima na tela a tabuada desse numero de 1 a 10')
res = 1
while (res == 1):
    x = int(input(' Digite o valor que deseja executara  tabuada: \n '))
    y = 0
    while y < 11:
        print('', x, 'x', y, ': {}'.format(x*y))
        y = y + 1
    res = int(input(' \n Deseja continuar com outros números ? Digite: \n  1) Para SIM: ► \n  2) Para NÃO: ►  '))
    print()
print(' Encerrando...')