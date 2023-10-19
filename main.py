import pygame, random, math

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

#enemy 
enemy_icons = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6
enemy_List = [pygame.image.load("images/enemy.png"), pygame.image.load("images/ufo.png"), pygame.image.load('images/spaceship.png')]

for i in range(number_of_enemies):
    enemy_icon = random.choice(enemy_List)
    enemy_icons.append(enemy_icon)
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(.3)
    enemyY_change.append(40)

bulletX, bulletY, bulletX_change, bulletY_change, bullet_state = 0, 480, 0.3, 1.7, "ready"

# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 16)
textX, textY = 10, 20

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
    
def player(x, y):
    screen.blit(player_icon, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_icon, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletY, bulletX):
    distance = math.sqrt((math.pow((enemyX - bulletX), 2)) + (math.pow((enemyY - bulletY), 2)))
    if distance < 27:
        return True
    else:
        return False

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
    
    for i in range(number_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -0.3

        # collision
        collision  = isCollision(enemyX[i], enemyY[i], bulletY, bulletX)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i], enemyY[i] = random.randint(0, 736), random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()