'''
Debugger

executar depurar [ctrl+shift+D]
marcar linha debugger
clicar depurador do python
utilizar o contornar [F10]
'''
frase = 'O Python é uma linguagem de programção'\
        'multiparadigma.'\
        'Python foi criado por Guido Van Rossum'
        

print(frase.count('Python')) #2

# i = 0
# contagem = 0
# while i < len(frase):
#     letra_atual = frase[i]

#     print(letra_atual)
#     i += 1
#     comod3IniciandoLogica/a70iterandoStringWhile.pyntagem += 1
# print(contagem)

# resposta Professor

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = qtd_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual
        
    i += 1
    
   
print('A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes}x')
    