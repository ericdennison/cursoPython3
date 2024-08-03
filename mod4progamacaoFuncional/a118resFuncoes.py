# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(valor):
#     return valor * 2

# def triplicar(valor):
#     return valor * 3

# def quadruplicar(valor):
#     return valor * 4


# print(duplicar(3))
# print(triplicar(4))
# print(quadruplicar(5))


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(3))
print(triplicar(4))
print(quadruplicar(5))