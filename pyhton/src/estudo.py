print("*******************************")
print("Bem-vindo ao jogo de advinhacao!")
print("*******************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Voce digitou" , chute)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Voce acertou")
else:   
    print("Voce errou")