import pygame
import random

pygame.init()

x = 1280
y = 720

clock = pygame.time.Clock()

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('AlienG')

bg = pygame.image.load('assets/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

alien = pygame.image.load('assets/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alien, (50,50))

playerImg = pygame.image.load('assets/space.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50,50))
playerImg = pygame.transform.rotate(playerImg, -90)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))

    #CRIAR IMAGENS
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    pygame.display.update()
    
    clock.tick(60)