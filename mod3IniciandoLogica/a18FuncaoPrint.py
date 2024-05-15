#Exibir
#Argumento não nomeado
#CTRL + C e CTRL + V duplicar linha
print(12, 34)
print(12, 34)

#Mudar separador -> sep
#Argumento nomeado
# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="-")
print(56, 78, sep='-')
print(9, 10, sep='-')

#Mudar final linha 
print(12, 34, 1011, sep="-", end='##\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')


