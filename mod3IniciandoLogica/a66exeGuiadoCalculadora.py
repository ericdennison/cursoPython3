""" 
Calculadora com while

lower -> letras minúsculas 
startswith -> valor inicia com determinada letra
"""

while True:
    # sair = input('Quer sair? [s]im: ')
    # sair = sair.lower()
    # sair = sair.startswith('s')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break