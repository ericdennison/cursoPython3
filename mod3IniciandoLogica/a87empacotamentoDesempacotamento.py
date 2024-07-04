"""
Introdução ao empacotamento e desempacotamento
"""


# nomes = ['Maria', 'Helena', 'Luiz']
# nome1,nome2,nome3 = nomes
# print(nome2)
# ou

# nome1,nome2,nome3 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

# pegando apenas 1 valor e colocando restante em 1 variável
# nome1,*_ = ['Maria', 'Helena', 'Luiz']
# print(nome1)
# print(_)

# pegando o valor do meio
_,nome2,*_ = ['Maria', 'Helena', 'Luiz']
print(nome2)
print(_)

# pegando o valor 3
_,_,nome3,*resto = ['Maria', 'Helena', 'Luiz']
print(nome3)
print(resto)
