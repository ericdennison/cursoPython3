# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1
    # return 'ACABOU'
    print('Continuando...')
    yield 2
    print('Mais uma')
    yield 3
    print('Vou terminar')
    return 'ACABOU'
    

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))