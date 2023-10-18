import pygame
import random

# initialise pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# title 
pygame.display.set_caption("Space invaders")

# background
background = pygame.image.load("images/background.jpg")

# bullet
bullet = pygame.image.load("images/bullet.png")
#icon
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# player
player_icon = pygame.image.load("images/battleship.png")
playerX, playerY, playerX_change = 370, 480, 0

enemy_icon = pygame.image.load("images/enemy.png")
enemyX, enemyY, enemyX_change, enemyY_change = random.randint(0, 736), random.randint(50, 150), 0.3, 20

bulletX, bulletY, bulletX_change, bulletY_change, bullet_state = 0, 480, 0.3, 1.7, "ready"

def player(x, y):
    screen.blit(player_icon, (x, y))

def enemy(x, y):
    screen.blit(enemy_icon, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))

# infinite game loop
running = True
while running:
    screen.fill((112,63,226))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check keysroke if pressed <- or ->
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":                    
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyY += enemyY_change
        enemyX_change = -0.3

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()