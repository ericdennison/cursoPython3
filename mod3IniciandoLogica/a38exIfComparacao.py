primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'primeiro="{primeiro_valor}" é maior que o segundo"{segundo_valor}"')
elif primeiro_valor < segundo_valor:
    print('Segundo valor é maior')
else:
    print('Tente novamente')






# Beecrowd
# Python 3.11
raio = float(input())
pi = 3.14159
area = pi*(raio**2)
print('{:.2f}'.format(area))
print(f'A={area:.4f}')
