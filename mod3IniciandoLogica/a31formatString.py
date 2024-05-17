nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

# Formatação de Strings 
#.2f casas decimais
linha_1 = f'{nome} tem {altura:.2f} de altura'

print(nome,'tem ',altura,'de altura,',)
print('pesa',peso,'quilos e seu IMC é,',)
print(imc)


# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é 
# 29.320984654320987
# IMC = peso / (altura x altura)

