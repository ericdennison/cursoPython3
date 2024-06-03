"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[4:8])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print(len(variavel[3]))
print(len(variavel)) #quantidade de elementos
print(variavel[0:len(variavel):1])
print(variavel[0:9:1])#pegando do inicio 0 e finalizando no 9 de 1 em um passo
print(variavel[0:9:2])
print(variavel[::-1])
print(variavel[-1:-10:-1])