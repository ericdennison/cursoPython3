# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
else: 
    print('Senha incorreta.')

# usando o not

senha2 = input('Senha: ')
if not senha2:
    print('Você não digitou nada')


print(not True) #False
print(not False) #True