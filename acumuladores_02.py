soma = 0
cont = 1

while (cont <= 5):
    x = float(input(' Digite a {}ª nota: '.format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5

if (media >= 7):
    res = 'Aprovado'
else:
    res = 'Reprovado'
print(' Sua média foi: {} \n Você foi {}'.format(media, res))
