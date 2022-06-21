import pygame
import random
import time
import os

os.system ("color 1")
os.system ("cls")

nome = input("Nome: ")
email = input("Email: ")
data = {"Nome":nome,"Email":email}
logs = open("logs.txt", "a")
try:
    logs.write(f"{data}\n") 
except:
    print("Erro de login!!!")
logs.write(str(data) + "\n") 

pygame.init()

x = 1280
y = 720

clock = pygame.time.Clock()

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('AlienG')

bg = pygame.image.load('assets/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

alien = pygame.image.load('assets/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alien, (50,25))

playerImg = pygame.image.load('assets/space.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50,50))
playerImg = pygame.transform.rotate(playerImg, -90)

missil = pygame.image.load('assets/missile.png').convert_alpha()
missil = pygame.transform.scale(missil, (25,25))
missil = pygame.transform.rotate(missil, -45)


pos_alien_x = 1250
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300

triggered = False

rodando = True

pontos = 4
font = pygame.font.SysFont('fonts\PixelGameFont.ttf', 50)
shootSound = pygame.mixer.Sound('assets/shoot.wav')
shootSound.set_volume(0.5)
musicaFundo = pygame.mixer.Sound('assets/music.wav')
musicaFundo.set_volume(0.1)

player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()

#FUNÇÕES
def perdeu():
    font = pygame.font.SysFont('fonts\PixelGameFont.ttf', 100)
    text = font.render("Game Over", True, (165,42,42))
    screen.blit(text, (450,300))
    pygame.display.update()
    time.sleep(3)
    exit()
    
def ganhou():
    font = pygame.font.SysFont('fonts\PixelGameFont.ttf', 100)
    text = font.render("You Win!!!", True, (165,42,42))
    screen.blit(text, (450,300))
    pygame.display.update()
    time.sleep(3)
    exit()

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
def colisions():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos += 1
        return True
    elif pontos == 0:
        perdeu()
    elif pontos == 50:
        ganhou()

    else:
        return False

time.sleep(2)

while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))
    musicaFundo.play()
    musicaFundo.set_volume(0.1)


    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    #TECLAS
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 5
        if not triggered:
            pos_missil_y -= 5
    
    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 5
        if not triggered:
            pos_missil_y += 5

    if tecla[pygame.K_SPACE]:
        shootSound.play()
        shootSound.set_volume(0.5)
        triggered = True
        vel_missil_x = 10
    
    if pontos == -1:
        rodando = False

    #RESPAWN
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()
    
    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    #POSICAO RECT
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.x = pos_missil_x
    missil_rect.y = pos_missil_y

    alien_rect.x = pos_alien_x
    alien_rect.y = pos_alien_y

    #MOVIMENTO
    x -= 3
    pos_alien_x -= 5

    pos_missil_x += vel_missil_x

    score = font.render(f'Vidas: {int(pontos)} ', True, (0,0,0))
    screen.blit(score, (50,50))

    #CRIAR IMAGENS
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))
    
    print(pontos)

    pygame.display.update()
    
    clock.tick(60)