import forca
import advinhacao

def escolhe_jogo():
    print("*******************************")
    print("Escolha o seu jogo!")
    print("*******************************")

    print("(1)Forca (2)Advinhação")

    jogo= int(input("Digite o numero do jogo: "))
    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando advinhação")
        advinhacao.jogar()
        
    print("Fim de jogo!")
    
if(__name__ == "__main__"):
    escolhe_jogo()