
# Escreva uma tabuada de um número fornecido pelo usuário.
# A tabuada deve ser calculada até determinado número n, também fornecido pelo usuário

print()
x = int(input(' Qual número deseja efetuar a tabuada ? '))
n = int(input(' Até qual número deseja efetuar a tabuada: '))

for i in range(0, n+1, 1):
    print('{} x {} = {}'.format(x, i, x*i))
