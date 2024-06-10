"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool

capitalize -> luiz Otávio -> Luiz Otávio
"""

string = 'luiz Otávio'
# outra_variavel = string
# string[3] = 'ABC' #não pode ser mudado o valor
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string[3]) 
print(outra_variavel)
print(string.capitalize())
print(string.zfill(20)) # 000000000luiz Otávio