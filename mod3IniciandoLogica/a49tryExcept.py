# Exceptions
"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(1234)
# print(456)
# int('a')

# numero = input('Vou dobrar o número que vc digitar: ')

# numero_float = float(numero)
# print(f'O dobro de {numero} é {numero_float * 2:.2f}')


numero_str = input(
    'Vou dobrar o número que vc digitar: '

)

try:
     print('STR: ', numero_str)
     numero_float = float(numero_str)
     print('FLOAT: ', numero_float)
     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')