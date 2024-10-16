import sys
# Generator expression, Iterables e Iterators em Python


iterable = ['Eu', 'Tenho', '_iter_']
iterator = iter(iterable) # tem _iter_ e _next_
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

# tamanho
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(len(generator))