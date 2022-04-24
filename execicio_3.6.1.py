soma = 0
qtd = 0
x = 0
while True:
    x = int(input(' Digite um valor inteiro '))
    if (x < 0):
        continue
    if not x:
        break
    soma = soma + x
    qtd = qtd + 1
    media = soma / qtd
print(' A média dos valores digitados é {}'.format(media))