cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_2 = (resultado_digito_1 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)