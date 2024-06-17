""" 
Calculadora com while

lower -> letras minúsculas 
startswith -> valor inicia com determinada letra
not in -> se tal elementão não está entre ...
"""

while True:
    # sair = input('Quer sair? [s]im: ')
    # sair = sair.lower()
    # sair = sair.startswith('s')

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')


    numeros_validos = None
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue


    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break