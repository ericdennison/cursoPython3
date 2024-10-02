# Dictionary Comprehension e Set Comprehension
# isinstance(valor, tipo) -> checa se valor determinado tipo

produto = {
    'nome':'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escrtório',
}

# print(produto.items())

# for chave, valor in produto.items():
#     print(chave, valor)


dc = {

    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'

}

lista = {
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
}

dc2 = {

    chave: valor
    for chave, valor in lista
    
}

print(dc)
print(dc2)
# ou
print(dict(lista))

# usando set

s1 = {2 ** i for i in range(10)}
print(s1)
# ou 
print(set(range(10)))