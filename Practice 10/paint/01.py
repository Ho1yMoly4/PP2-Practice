import pygame
import math

pygame.init()

# SETTINGS 
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 20)

# COLORS 
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY  = (160,160,160)
RED   = (255,0,0)
GREEN = (0,180,0)
BLUE  = (0,0,255)

colors = {
    pygame.K_0: (BLACK, "BLACK"),
    pygame.K_1: (RED, "RED"),
    pygame.K_2: (GREEN, "GREEN"),
    pygame.K_3: (BLUE, "BLUE"),
    pygame.K_4: ((255,255,0), "YELLOW"),
    pygame.K_5: ((255,165,0), "ORANGE"),
    pygame.K_6: ((128,0,128), "PURPLE"),
    pygame.K_7: ((255,105,180), "PINK"),
    pygame.K_8: ((139,69,19), "BROWN"),
    pygame.K_9: (GRAY, "GRAY"),
}

# STATE 
tool = "pen"
color, color_name = BLACK, "BLACK"
thickness = 4

drawing = False
start = None
prev = None
current = None

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BG_COLOR)

# HELP FUNCTIONS 
def get_color():
    return BG_COLOR if tool == "eraser" else color

def draw_rect(surface, start, end):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
    pygame.draw.rect(surface, get_color(), rect, thickness)

def draw_circle(surface, start, end):
    r = int(math.hypot(end[0]-start[0], end[1]-start[1]))
    if r > 0:
        pygame.draw.circle(surface, get_color(), start, r, thickness)

def draw_ui():
    pygame.draw.rect(screen, (235,235,235), (WIDTH-230, 10, 220, 110))
    pygame.draw.rect(screen, BLACK, (WIDTH-230, 10, 220, 110), 2)

    screen.blit(font.render(f"Tool: {tool}", True, BLACK), (WIDTH-220, 20))
    screen.blit(font.render(f"Size: {thickness}", True, BLACK), (WIDTH-220, 50))
    screen.blit(font.render(f"Color: {color_name}", True, BLACK), (WIDTH-220, 80))

    pygame.draw.rect(screen, color, (WIDTH-60, 80, 30, 30))

# MAIN LOOP 
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # KEYBOARD 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: tool = "pen"
            elif event.key == pygame.K_r: tool = "rect"
            elif event.key == pygame.K_c: tool = "circle"
            elif event.key == pygame.K_e: tool = "eraser"

            elif event.key in (pygame.K_PLUS, pygame.K_EQUALS):
                thickness += 1
            elif event.key == pygame.K_MINUS and thickness > 1:
                thickness -= 1

            elif event.key == pygame.K_SPACE:
                canvas.fill(BG_COLOR)

            elif event.key in colors:
                color, color_name = colors[event.key]

        # MOUSE 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start = prev = current = event.pos

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current = event.pos
                if tool in ("pen", "eraser"):
                    pygame.draw.line(canvas, get_color(), prev, current, thickness)
                    prev = current

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                current = event.pos

                if tool == "rect":
                    draw_rect(canvas, start, current)
                elif tool == "circle":
                    draw_circle(canvas, start, current)

                drawing = False

    # DRAW 
    screen.blit(canvas, (0,0))

    if drawing and tool in ("rect", "circle") and start and current:
        if tool == "rect":
            draw_rect(screen, start, current)
        elif tool == "circle":
            draw_circle(screen, start, current)

    draw_ui()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()