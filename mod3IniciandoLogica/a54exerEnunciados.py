"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
inteiro = input('Digite um número inteiro: ')


try:
    inteiro = int(inteiro)
    if inteiro % 2 == 0:
        print('É um número Par')
    else:
        print('É um número Impar')
except ValueError:
    print("Não é inteiro")



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Digite o horario atual: ")
concatena = horario[0:2]
uniao = concatena[0] + concatena[1]
resposta = int(uniao)


if resposta >= 0 and resposta <= 11:
    print('Bom dia')
elif resposta >= 12 and resposta <= 17:
    print('Boa tarde')
else:
    print('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
quantidade = len(nome)
if quantidade <= 4:
    print('Seu nome é curto')
elif quantidade >= 5 and quantidade <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')