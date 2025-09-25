import ramdom
emoji =["✂️","📄","🪨"]
from random import choice
computador = choice(emoji)
jogador = str(input("Escolha entre Pedra, Papel ou Tesoura: ")).lower()
if jogador == "pedra":
    jogador = "🪨"
elif jogador == "papel":
    jogador = "📄"
elif jogador == "tesoura":
    jogador = "✂️"
else:
    print("Jogada inválida! Escolha entre Pedra, Papel ou Tesoura.")
    exit()
print(f"Jogador escolheu: {jogador}")
print(f"Computador escolheu: {computador}")
if jogador == computador:
    print("Empate!")    
elif (jogador == "🪨" and computador == "✂️") or (jogador == "📄" and computador == "🪨") or (jogador == "✂️" and computador == "📄"):
    print("Jogador vence!")
else:
    print("Computador vence!")
    