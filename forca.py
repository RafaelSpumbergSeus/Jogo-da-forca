import random

#lista de palavras sorteadas.
palavras = ['python', 'programacao', 'computador', 'aula']

#escolher a palavra 
palavra_sorteada = random.choice(palavras)

#criar string com traços que representam letras
palavra_escondida = '-' * len(palavra_sorteada)

#criar lista vazia para armazenar letras utilizadas 
letras_adivinhadas = []

max_tentativas = 6 

while True:
    #mostras palavra escondida 
    print(palavra_escondida)
    
    letra = input('Digite uma letra: ')
    
    #verificar letra digitada
    if letra in letras_adivinhadas:
        print('Você já digitou essa letra. Tente outra!')
        continue 
    
    letras_adivinhadas.append(letra)



