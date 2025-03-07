# Variáveis livres + nonlocal (locals, globals)
# variável livre - variável não definida dentro escopo função
# locals -> quais variáveis locais
# __code__.co_freevars -> acesso variáveis livres
# globals - mostra variáveis globais
# nonlocal -> marca variável não local

# print(globals())

# def fora(x):
#     a = x
#     def dentro():
#         # print(locals())
#         # print(dentro.__code__.co_freevars)
#         # variável livre
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    # necessário passar valor padrão parametro
    # evitar erro
    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

final = c()
print(final)

