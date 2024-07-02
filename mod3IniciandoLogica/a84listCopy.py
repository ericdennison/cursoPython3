"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

Garbage Collector - elimina da memoria
ex:
nome = 'Luiz'
noutra_variavel = nome
nome = 'João'
print(nome)
print(noutra_variavel)

copy -> retorna copia lista
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)