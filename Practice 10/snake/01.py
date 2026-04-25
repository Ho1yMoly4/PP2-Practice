import pygame
import random

# CONFIGURATION 
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20  # Size of one grid square
pygame.init()

# Setup display and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game: Levels & Speed")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 24)

# Colors
WHITE = (255, 255, 255)
GREEN = (46, 204, 113)
RED   = (231, 76, 60)
BLACK = (44, 62, 80)
GRAY  = (149, 165, 166)

class Snake:
    def __init__(self):
        # Initial body: 3 segments
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (BLOCK_SIZE, 0) # Moving Right

    def move(self):
        # Calculate new head position
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        # Add new head and remove tail
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        # Keep the tail to increase length
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE - 2, BLOCK_SIZE - 2))

class Food:
    def __init__(self, snake_body):
        self.pos = self.generate_safe_pos(snake_body)

    def generate_safe_pos(self, snake_body):
        while True:
            # Generate random grid coordinates
            x = random.randrange(0, WIDTH, BLOCK_SIZE)
            y = random.randrange(0, HEIGHT, BLOCK_SIZE)
            # Ensure food doesn't spawn inside the snake's body
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.pos[0], self.pos[1], BLOCK_SIZE - 2, BLOCK_SIZE - 2))

# GAME INITIALIZATION 
snake = Snake()
food = Food(snake.body)
score = 0
level = 1
speed = 10  # Initial FPS

running = True
while running:
    screen.fill(BLACK)
    
    # 1. EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # Prevent 180-degree turns
            if event.key == pygame.K_UP and snake.direction != (0, BLOCK_SIZE):
                snake.direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -BLOCK_SIZE):
                snake.direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and snake.direction != (BLOCK_SIZE, 0):
                snake.direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-BLOCK_SIZE, 0):
                snake.direction = (BLOCK_SIZE, 0)

    # 2. LOGIC UPDATE
    snake.move()
    head = snake.body[0]

    # CHECK: Wall Collision (Leaving the playing area)
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("GAME OVER: Hit the wall!")
        running = False

    # CHECK: Self Collision
    if head in snake.body[1:]:
        print("GAME OVER: Hit yourself!")
        running = False

    # CHECK: Food Consumption
    if head == food.pos:
        snake.grow()
        score += 1
        food = Food(snake.body) # Generate new food in a safe spot
        
        # LEVEL UP: Every 3 foods collected
        if score % 3 == 0:
            level += 1
            speed += 2 # Increase game speed

    # 3. DRAWING
    food.draw()
    snake.draw()
    
    # UI: Score and Level counter
    ui_text = font.render(f"Score: {score} | Level: {level} | Speed: {speed}", True, WHITE)
    screen.blit(ui_text, (15, 15))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()