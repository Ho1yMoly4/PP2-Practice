import pygame
import random
import time
import os

pygame.init()

# WINDOW SETTINGS 
WIDTH, HEIGHT = 400, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# PATH SETUP 
BASE = os.path.dirname(__file__)  # current file locatiяon
RES = os.path.join(BASE, "resources")  # path to resources folder

def load(name):
    return os.path.join(RES, name)  # helper to load files

# LOAD IMAGES 
image_bg = pygame.image.load(load("AnimatedStreet.png"))
image_player = pygame.image.load(load("Player.png"))
image_enemy = pygame.image.load(load("Enemy.png"))
image_money = pygame.transform.scale(
    pygame.image.load(load("Tenge.png")), (40, 40)
)

# BACKGROUND MUSIC 
pygame.mixer.music.load(load("background.wav"))
pygame.mixer.music.set_volume(0.5)  # volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # loop forever

# SOUND EFFECTS 
sound_crash = pygame.mixer.Sound(load("crash.wav"))
sound_money = pygame.mixer.Sound(load("money.wav"))
sound_bip = pygame.mixer.Sound(load("bip.wav"))

# FONTS 
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 18)

# BACKGROUND SCROLL VARIABLES 
bg_y1, bg_y2 = 0, -HEIGHT
bg_speed = 5

# PLAYER SETUP 
player = image_player.get_rect(center=(WIDTH // 2, HEIGHT - 50))
player_speed = 5

# ENEMY SETUP 
enemy = image_enemy.get_rect()
enemy.left = random.randint(0, WIDTH - enemy.w)
enemy.bottom = 0
enemy_speed = 7

# MONEY (COIN) SETUP 
money = image_money.get_rect()
money.left = random.randint(0, WIDTH - money.w)
money.bottom = 0

# GAME VARIABLES 
score = 0
timer = 0
running = True

# GAME LOOP 
while running:

    # HANDLE EVENTS 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # play sound when SPACE is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound_bip.play()

    keys = pygame.key.get_pressed()

    # PLAYER MOVEMENT 
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed + player_speed // 2  # auto move down

    player.move_ip(dx, dy)

    # keep player inside screen
    player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    # ENEMY MOVEMENT 
    enemy.y += enemy_speed
    if enemy.top > HEIGHT:
        enemy.left = random.randint(0, WIDTH - enemy.w)
        enemy.bottom = 0

    # MONEY MOVEMENT (same as background) 
    money.y += bg_speed
    if money.top > HEIGHT:
        money.left = random.randint(0, WIDTH - money.w)
        money.bottom = 0

    # BACKGROUND SCROLL 
    bg_y1 += bg_speed
    bg_y2 += bg_speed

    if bg_y1 >= HEIGHT:
        bg_y1 = -HEIGHT
    if bg_y2 >= HEIGHT:
        bg_y2 = -HEIGHT

    # SPEED INCREASE OVER TIME 
    timer += 1
    if timer % 300 == 0:
        bg_speed += 1
        enemy_speed += 1
        player_speed = int(player_speed + 0.5)

    # COLLISIONS 
    # player collects money
    if player.colliderect(money):
        sound_money.play()
        money.left = random.randint(0, WIDTH - money.w)
        money.bottom = 0
        score += 20

    # player hits enemy
    if player.colliderect(enemy):
        sound_crash.play()

        screen.fill("red")
        text = font_big.render("Game Over", True, "black")
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        pygame.display.flip()
        time.sleep(2)
        running = False

    # DRAW EVERYTHING
    screen.blit(image_bg, (0, bg_y1))
    screen.blit(image_bg, (0, bg_y2))

    screen.blit(image_money, money)
    screen.blit(image_player, player)
    screen.blit(image_enemy, enemy)

    # draw score
    score_text = font_small.render(f"Score: {score} tg", True, "black")
    screen.blit(score_text, (WIDTH - 140, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()