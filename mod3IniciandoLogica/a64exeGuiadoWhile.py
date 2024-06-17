"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio' #Iteráveis
#      1110987654321

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

print(nome[3])
contador = 0
novo_nome = ''
while contador < len(nome):
    novo_nome += "*"+nome[contador] # novo_nome = novo_nome('') + "*" + nome[contador] 0
    print(novo_nome)
    contador += 1 