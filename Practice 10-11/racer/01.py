import pygame
import random
import time
import os

# Initialize Pygame modules
pygame.init()

# SETTINGS 
WIDTH, HEIGHT = 400, 600
FPS = 60
N = 5  # The enemy speed increases every 5 coins collected

# Initial Speeds (Constants/Variables)
BG_SPEED = 5
ENEMY_SPEED = 7
PLAYER_SPEED = 5

# Set up the display and game clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racer: Weighted Evolution")
clock = pygame.time.Clock()

# PATH SETUP 
BASE = os.path.dirname(__file__)
RES = os.path.join(BASE, "resources")

def get_path(name):
    """Helper function to get the full path of a resource."""
    return os.path.join(RES, name)

# LOAD ASSETS 
try:
    image_bg = pygame.image.load(get_path("AnimatedStreet.png"))
    image_player = pygame.image.load(get_path("Player.png"))
    image_enemy = pygame.image.load(get_path("Enemy.png"))
    image_money = pygame.transform.scale(
        pygame.image.load(get_path("Tenge.png")), (40, 40)
    )

    # Audio assets
    pygame.mixer.music.load(get_path("background.wav"))
    sound_crash = pygame.mixer.Sound(get_path("crash.wav"))
    sound_money = pygame.mixer.Sound(get_path("money.wav"))
    sound_bip = pygame.mixer.Sound(get_path("bip.wav"))
except pygame.error as e:
    print(f"File loading error: {e}")
    pygame.quit()
    exit()

# Start background music
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Font styles
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 18)

# INITIALIZE GAME OBJECTS 
bg_y1, bg_y2 = 0, -HEIGHT # Two backgrounds for infinite scrolling

# Player start position
player = image_player.get_rect(center=(WIDTH // 2, HEIGHT - 70))

# Enemy start position
enemy = image_enemy.get_rect()
enemy.left = random.randint(0, WIDTH - enemy.w)
enemy.bottom = 0

# Coin start position
money = image_money.get_rect()
money.left = random.randint(0, WIDTH - money.w)
money.bottom = 0

# GAME VARIABLES 
score = 0
coins_collected_count = 0  # Number of coins gathered (to trigger speed up)
current_coin_value = random.choice([10, 20, 50])  # Weight of the coin on screen
running = True

# MAIN GAME LOOP 
while running:
    # 1. EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Play horn/beep sound on Spacebar
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound_bip.play()

    # 2. MOVEMENT LOGIC
    keys = pygame.key.get_pressed()
    
    # Calculate Player movement based on keys
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_SPEED
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * PLAYER_SPEED
    player.move_ip(dx, dy)
    
    # Keep player within screen boundaries
    player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    # Move the Enemy downward
    enemy.y += ENEMY_SPEED
    if enemy.top > HEIGHT: # Respawn enemy if it leaves screen
        enemy.left = random.randint(0, WIDTH - enemy.w)
        enemy.bottom = 0

    # Move the Coin downward
    money.y += BG_SPEED
    if money.top > HEIGHT: # Respawn coin and change its weight
        money.left = random.randint(0, WIDTH - money.w)
        money.bottom = 0
        current_coin_value = random.choice([10, 20, 50])

    # Scroll the background images
    bg_y1 += BG_SPEED
    bg_y2 += BG_SPEED
    if bg_y1 >= HEIGHT: bg_y1 = -HEIGHT
    if bg_y2 >= HEIGHT: bg_y2 = -HEIGHT

    # 3. COLLISION DETECTION
    # If Player collects a coin
    if player.colliderect(money):
        sound_money.play()
        
        # Add the coin's current weight to total score
        score += current_coin_value
        coins_collected_count += 1
        
        # INCREASE ENEMY SPEED every N coins collected
        if coins_collected_count % N == 0:
            ENEMY_SPEED += 1
        
        # Respawn coin and choose a new weight for the next one
        money.left = random.randint(0, WIDTH - money.w)
        money.bottom = 0
        current_coin_value = random.choice([10, 20, 50])

    # If Player hits the Enemy
    if player.colliderect(enemy):
        pygame.mixer.music.stop()
        sound_crash.play()
        
        # Fill screen red and show Game Over text
        screen.fill("red")
        game_over_text = font_big.render("GAME OVER", True, "black")
        screen.blit(game_over_text, game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        
        time.sleep(2)
        running = False

    # 4. RENDERING / DRAWING
    # Draw Backgrounds
    screen.blit(image_bg, (0, bg_y1))
    screen.blit(image_bg, (0, bg_y2))
    
    # Draw Game Entities
    screen.blit(image_money, money)
    screen.blit(image_player, player)
    screen.blit(image_enemy, enemy)

    # Draw UI (Score and current coin weight)
    score_display = font_small.render(f"Score: {score}", True, "black")
    weight_display = font_small.render(f"Coin Value: {current_coin_value}", True, "blue")
    count_display = font_small.render(f"Coins: {coins_collected_count}", True, "darkgreen")
    
    screen.blit(score_display, (WIDTH - 150, 10))
    screen.blit(weight_display, (WIDTH - 150, 35))
    screen.blit(count_display, (WIDTH - 150, 60))

    # Update the full display Surface to the screen
    pygame.display.flip()
    
    # Ensure the game runs at 60 Frames Per Second
    clock.tick(FPS)

pygame.quit()