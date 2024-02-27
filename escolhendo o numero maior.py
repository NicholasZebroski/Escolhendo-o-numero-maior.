n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))

if n1 > n2:
    print('o número maior é o {}.'.format(n1))
elif n2 > n1:
    print('o número maior é o {}.'.format(n2))
else:
    print("Os números são iguais!")