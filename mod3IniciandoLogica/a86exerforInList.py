"""
Exercicio
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz

Minha resposta:

lista = ['Maria', 'Helena', 'Luiz']

for indice, nome in enumerate(lista):
    print(indice, nome, type(nome)) 

"""


lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices :
    print(indice, lista[indice], type(lista[indice]))


