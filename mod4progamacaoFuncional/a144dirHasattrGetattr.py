# dir, hasattr e getattr em Python

# hasattr -> checa determinado metodo existe

string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    # print(string.upper())
    # ou
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)