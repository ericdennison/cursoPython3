import random
# import sys

'''
randint -> número aleatorio inteiro
sys.exit()-> stop execução
'''

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    # print(nove_digitos)

    # sys.exit()

    contador_regressivo_1 = 10


    resultado_digito_1 = 0
    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_2 = (resultado_digito_1 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0


    # segundo digito resolução

    dez_digitos = nove_digitos + str(digito_2)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_3 = (resultado_digito_2 * 10) % 11
    digito_3 = digito_3 if digito_3 <= 9 else 0

    # novo cpf

    cpf_gerado_calculo = f'{nove_digitos}{digito_2}{digito_3}'

    print(cpf_gerado_calculo)
