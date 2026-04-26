import pygame
import random
import time

# CONFIGURATION 
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20  
pygame.init()

# Setup display and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game: Weighted Food & Timers")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 24)

# Colors
WHITE = (255, 255, 255)
GREEN = (46, 204, 113)
RED   = (231, 76, 60)
GOLD  = (241, 196, 15) # For high-weight food
BLACK = (44, 62, 80)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (BLOCK_SIZE, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE - 2, BLOCK_SIZE - 2))

class Food:
    def __init__(self, snake_body):
        self.pos = self.generate_safe_pos(snake_body)
        
        # TASK: DIFFERENT WEIGHTS 
        # 20% chance for a "Golden" food worth 3 points, otherwise 1 point
        if random.random() < 0.2:
            self.weight = 3
            self.color = GOLD
            self.lifetime = 4.0  # Golden food disappears faster
        else:
            self.weight = 1
            self.color = RED
            self.lifetime = 8.0  # Normal food lasts longer
            
        # TASK: TIMER 
        self.spawn_time = time.time()

    def generate_safe_pos(self, snake_body):
        while True:
            x = random.randrange(0, WIDTH, BLOCK_SIZE)
            y = random.randrange(0, HEIGHT, BLOCK_SIZE)
            if (x, y) not in snake_body:
                return (x, y)

    def is_expired(self):
        """Check if the food has been on screen longer than its lifetime."""
        return time.time() - self.spawn_time > self.lifetime

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], BLOCK_SIZE - 2, BLOCK_SIZE - 2))

# GAME INITIALIZATION 
snake = Snake()
food = Food(snake.body)
score = 0
level = 1
speed = 10 

running = True
while running:
    screen.fill(BLACK)
    
    # 1. EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
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

    # Wall Collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    # Self Collision
    if head in snake.body[1:]:
        running = False

    # TASK: EXPIRING FOOD 
    # If food expires before snake eats it, spawn a new one
    if food.is_expired():
        food = Food(snake.body)

    # Food Consumption
    if head == food.pos:
        snake.grow()
        # TASK: WEIGHTED SCORE 
        score += food.weight 
        
        # Level up logic (based on total score)
        if score // 5 >= level: 
            level += 1
            speed += 2
        
        food = Food(snake.body)

    # 3. DRAWING
    food.draw()
    snake.draw()
    
    # Calculate remaining time for the food to display on UI
    time_left = max(0, int(food.lifetime - (time.time() - food.spawn_time)))
    
    ui_text = font.render(f"Score: {score} | Level: {level} | Food Timer: {time_left}s", True, WHITE)
    screen.blit(ui_text, (15, 15))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()