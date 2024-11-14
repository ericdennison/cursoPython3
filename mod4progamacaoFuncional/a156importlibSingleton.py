# Singleton: só pode existir uma instancia 
# importlib: recarrega módulo
import importlib

import a154_p2

print(a154_p2.variavel_modulo)

for i in range(10):
    importlib.reload(a154_p2)
    print(i)
    import a154_p2

print("FIM")