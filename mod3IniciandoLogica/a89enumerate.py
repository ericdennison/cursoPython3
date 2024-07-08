"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# usando numerate e list
# lista_enumerada = list(enumerate(lista, start=19))
# print(lista_enumerada)

# usando next
# print(next(lista_enumerada))

# usando for
# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

# é o mesmo que:

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])