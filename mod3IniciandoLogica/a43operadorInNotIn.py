# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 -> indices positivos
#  O t á v i o
# -6-5-4-3-2-1 - indices negativos

# nome = 'Otávio'
# # print(nome[2])
# # print(nome[-4])
# print('á' in nome)
# print('z' in nome)
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}: ')
else:
    print(f'{encontrar} não está em {nome}: ')