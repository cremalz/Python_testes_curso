import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Primeiro Jogo")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Posição do jogador
x = 400
y = 300
velocidade = 5

# Loop principal do jogo
rodando = True
while rodando:
    pygame.time.delay(30)  # controla a velocidade do loop
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Captura teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Atualiza a tela
    tela.fill(BRANCO)               # limpa a tela
    pygame.draw.rect(tela, VERMELHO, (x, y, 50, 50))  # desenha o jogador
    pygame.display.update()         # atualiza a tela

pygame.quit()
sys.exit()