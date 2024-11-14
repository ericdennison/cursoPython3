# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import a154_p2
from a154_p2 import variavel_modulo, soma

print('Este módulo se chama', __name__)
print(a154_p2.variavel_modulo)
print(variavel_modulo)
print(soma(3,3))
print(a154_p2.soma(2, 3))