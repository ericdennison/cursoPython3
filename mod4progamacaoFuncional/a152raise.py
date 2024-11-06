# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# print(123)
# raise ValueError("Deu Erro")
# print(456)

def nao_aceito_zerto(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por Zero")
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
            raise TypeError(
                f'"{n}" deve ser int ou float.'
                f'"{tipo_n.__name__}" enviado'
            )
    return True

def divide(n, d):

   deve_ser_int_ou_float(n)
   deve_ser_int_ou_float(d)
   nao_aceito_zerto(d)
   return n / d
    

print(divide(8, '0'))