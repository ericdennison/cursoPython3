"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Luiz')

# print(texto.__next__())
# print(texto.__next__())
# #ou 
# print(next(texto))

# for letra in texto
texto = 'Luiz' #iterável
iterador = iter(texto) #iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# que é o mesmo que

for letra in texto:
    print(letra)