"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra global faz uma variável do escopo ser a mesma no escopo interno
Call Stack -> Pilha chamada
"""

x = 1 # x criado escopo global


def escopo():
    global x # definindo global
    x = 10 # x criado escopo função
    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

