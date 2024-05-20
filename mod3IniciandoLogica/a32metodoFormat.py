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
    nome1=a, nome2=b, nome3=c
    
    )

print(formato)