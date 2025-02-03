import random

#lista de palavras sorteadas.
palavras = ['python', 'programacao', 'computador', 'aula']

#escolher a palavra 
palavra_sorteada = random.choice(palavras)

#criar string com traços que representam letras
palavra_escondida = '_' * len(palavra_sorteada)

#criar lista vazia para armazenar letras utilizadas 
letras_adivinhadas = []

max_tentativas = 6 

while True:
    #mostras palavra escondida 
    print(palavra_escondida)
    
    letra = input('Digite uma letra: ').lower()
    
    #verificar letra digitada
    if letra in letras_adivinhadas:
        print('Você já digitou essa letra. Tente outra!')
        continue 
    
    letras_adivinhadas.append(letra)
    
    if letra in palavra_sorteada:
        lista = list(palavra_escondida)
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista[indice] = letra
        palavra_escondida = ''.join(lista)
                
    else:
        max_tentativas -=1
        print(f'Letra não encontrada. Você tem mais {max_tentativas} tentativas')
        
    if palavra_escondida == palavra_sorteada:
        print('Parabéns, você ganhou!')
        break
    elif max_tentativas == 0:
        print(f'Você perdeu. A palavra era {palavra_sorteada}')
        break



