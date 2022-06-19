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

missil = pygame.image.load('assets/missile.png').convert_alpha()
missil = pygame.transform.scale(missil, (25,25))
missil = pygame.transform.rotate(missil, -45)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300


triggered = False
rodando = True

#FUNÇÕES
def respawn():
    x = 1350
    y = random.randint(1,640)
    return[x,y]
def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_x_missil = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_x_missil]


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    #TECLAS
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 8
        if not triggered:
            pos_missil_y -= 8
    
    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 8
        if not triggered:
            pos_missil_y += 8

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 20

    #RESPAWN
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()

    #MOVIMENTO
    x -= 5
    pos_alien_x -= 10

    pos_missil_x += vel_missil_x

    #CRIAR IMAGENS
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    pygame.display.update()
    
    clock.tick(60)