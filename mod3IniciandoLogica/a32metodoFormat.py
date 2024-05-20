a = 'A'
b = 'B'
c = 1.1
#associando chaves ao valor do parametro
# string = 'a={} b={} c={:.2f}'

# valor por indice
# string = 'a={0} b={1} c={2:.2f}'

# parametro nomeado
string = ' b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
        nome1=a, 
        nome2=b,
        nome3=c
    
    )

print(formato)

# Pergunta 4 Teste 4 
nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

# Pergunta 6 Teste 4
nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'
print(formato)



