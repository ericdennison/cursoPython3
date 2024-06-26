"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'perfume'
letra = input('Digite apenas uma letra: ')

# contador = 0
if letra == letra[0:1]:
    if letra in palavra_secreta:
        acertos = palavra_secreta.replace(letra, '*')
        print(acertos)
    



else:
    print('Digite apenas uma letra')

