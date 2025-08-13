"""

Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
String são textos que estão dentro de aspas

"""
print(1234)

# Aspas simples
print('Luiz Otávio')
print('Luiz "Otávio"')


# Aspas duplas
print("Luiz Otávio")
print("Luiz 'Otávio'")

#Escape
print("Luiz \"Otávio\"")

# r
print(r"Luiz \"Otávio\"")

'''
o r antes da string significa raw string (“string crua”).

Isso faz com que o Python não interprete as barras invertidas (\) como caracteres de escape.
Ou seja, dentro de uma raw string, \n não vira quebra de linha, \t não vira tabulação, e \" é mantido exatamente como \".


Tipagem Dinâmica — o tipo é decidido em tempo de execução
* Em Python, você não declara o tipo da variável (int, str, float, etc.) no código.

* O tipo é inferido automaticamente no momento em que você atribui um valor.

* O mesmo nome de variável pode apontar para objetos de tipos diferentes ao longo do programa.

Exemplo: 
x = 10        # x é int agora
x = "texto"   # agora x é str

Tipagem Forte — o Python não faz conversões automáticas inseguras
* Uma linguagem de tipagem fraca permitiria misturar tipos de forma implícita (ex: somar número com texto sem erro).

* Em Python, se você tentar operar tipos incompatíveis sem conversão explícita, vai dar erro.

Exemplo:
x = "10"
y = 5
print(x + y)  # ❌ TypeError
É preciso converter manualmente:
print(int(x) + y)  # ✅ 15


*metáfora
'''



