# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '_iter_']
# iterator = iterable.__iter__() #tem _iter_ e _next_
iterator = iter(iterable)#tem _iter_ e _next_
print(next(iterator))
print(next(iterator))
print(next(iterator))
