# Manipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = 'nome'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'
print(pessoa)

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# checar chave existe
# print(pessoa.get('sobrenome'))

# outra forma checar
if pessoa.get('sobrenome') is None:
    print('NÁO EXISTE')
else:
    print(pessoa['sobrenome'])

