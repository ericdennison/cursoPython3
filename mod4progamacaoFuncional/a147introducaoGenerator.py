# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    # yield 1
    # # return 'ACABOU'
    # print('Continuando...')
    # yield 2
    # print('Mais uma')
    # yield 3
    # print('Vou terminar')
    # return 'ACABOU'
    while True:
        yield n
        n += 1


        if n >= maximum:
            return 
        

gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# ou usando for
for n in gen:
    print(n)