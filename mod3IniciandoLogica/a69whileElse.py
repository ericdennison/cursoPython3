"""
While/else

- recurso exclusivo do python
- no fim do laço else executado
- break executado else não é executado

"""

string = input()

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não econtrei espaço na string')

print('Fora do while.')

