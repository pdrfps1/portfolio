
def jogar():
    import random
    print("*******************************")
    print("Bem-vindo ao jogo de advinhacao!")
    print("*******************************")
    # Variaveis
    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 3
    pontos = 1000


    # Escolha de nivel
    print("Qual o nivel de dificulade?")
    print("(1) Facil (2) Médio (3) Dificil")

    nivel = int(input("Escolha um nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        
        chute_str = input("Digite o seu numero entre 1 e 100: ")
        print("Voce digitou" , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou. E você fez", pontos,"pontos.")
            break
        else:
            if(maior):
                print("Você errou! O numero que voce digitou é maior que o numero secreto.")
            elif(menor):
                print("Você errou! O numero que voce digitou é menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    
    print ("Fim de jogo. O numero secreto era", numero_secreto, "e você fez", pontos,"pontos.")
    
    if(__name__ == "__main__"):
        jogar()