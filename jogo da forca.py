 
palavra = "celular"
letras_usuário = []
chances = 5
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_usuário:
            print (letra, end=" ")
        
        else:
            print("_", end=" ")    
    print (f"você tem {chances} chances")
    tentativas = input("Escolha uma letra para advinhar: ")
    letras_usuário.append(tentativas.lower())
    if tentativas.lower() not in palavra.lower():
        chances -= 1
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuário:
            ganhou = False
    
    if chances == 0 or ganhou:
        break
if ganhou:
    print(f"muito bem, você ganhou a palavra era {palavra}")
    
else:
    print (f"infelizmente vc perdeu, a palavra era {palavra}") 