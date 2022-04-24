soma = 0
cont = 1
while ( cont <= 5):
    x = int(input(' Digite o {}º número: '.format(cont)))
    soma = soma + x
    cont = cont + 1
print(' \n Somatório: {}'.format(soma))