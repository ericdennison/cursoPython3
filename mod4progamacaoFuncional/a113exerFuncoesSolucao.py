# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# retorne se o número é par ou ímpar

#Minha Resposta
def produto(*args):
    resposta = 1
    for i in args:
        resposta *= i
        
    return resposta

comparar = produto(1,2,3,4)
print(f'Sua resposta: {comparar}')
print(f'Resposta correta: {1*2*3*4}')


def parImpar(num):
    if num % 2 == 0:
        return 'Número Par'
    else:
        return 'Número Impar' 

par_impar = parImpar(comparar)
print(par_impar)


#Resposta do Professor

def multiplicar(*args):
    total = 0 
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)
print(1*2*3*4*5)

def p_i(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    # else:
    #     return 'impar'
    return f'{numero} é impar'

print(p_i(2))
print(p_i(3))
print(p_i(15))
print(p_i(16))

