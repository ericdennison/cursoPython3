"""
Flag (Bandeira ) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
#apontam para o mesmo valor
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

#apontam para valores diferentes
n1 = 'a'
n2 = 'b'
print(id(n1))
print(id(n2))

