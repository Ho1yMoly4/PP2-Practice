import pygame
import math

# Initialize Pygame library
pygame.init()

# SETTINGS
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Fonts for the user interface
font = pygame.font.SysFont("Verdana", 18)
small_font = pygame.font.SysFont("Verdana", 14)

# COLORS 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (160, 160, 160)
RED   = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE  = (0, 0, 255)

# Dictionary to map keys to colors and their names
colors = {
    pygame.K_0: (BLACK, "BLACK"),
    pygame.K_1: (RED, "RED"),
    pygame.K_2: (GREEN, "GREEN"),
    pygame.K_3: (BLUE, "BLUE"),
    pygame.K_4: ((255, 255, 0), "YELLOW"),
    pygame.K_5: ((255, 165, 0), "ORANGE"),
    pygame.K_6: ((128, 0, 128), "PURPLE"),
    pygame.K_7: ((255, 105, 180), "PINK"),
    pygame.K_8: ((139, 69, 19), "BROWN"),
    pygame.K_9: (GRAY, "GRAY"),
}

# INITIAL STATE 
tool = "pen"
color, color_name = BLACK, "BLACK"
thickness = 4

drawing = False
start_pos = None
last_pos = None
current_pos = None

# Create a separate surface for permanent drawing
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BG_COLOR)

# HELPER DRAWING FUNCTIONS 

# Get color based on current tool (white for eraser)
def get_current_color():
    return BG_COLOR if tool == "eraser" else color

# Draw a rectangle between two points
def draw_rect(surface, start, end):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surface, get_current_color(), rect, thickness)

# Draw a circle where the radius is the distance between points
def draw_circle(surface, start, end):
    radius = int(math.hypot(end[0] - start[0], end[1] - start[1]))
    if radius > 0:
        pygame.draw.circle(surface, get_current_color(), start, radius, thickness)

# Draw a square with equal sides
def draw_square(surface, start, end):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    new_x = x1 + side if x2 > x1 else x1 - side
    new_y = y1 + side if y2 > y1 else y1 - side
    rect = pygame.Rect(min(x1, new_x), min(y1, new_y), side, side)
    pygame.draw.rect(surface, get_current_color(), rect, thickness)

# Draw a right-angled triangle
def draw_right_triangle(surface, start, end):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, get_current_color(), points, thickness)

# Draw a triangle where all sides are equal
def draw_equilateral_triangle(surface, start, end):
    x1, y1 = start
    x2, y2 = end
    side = math.hypot(x2 - x1, y2 - y1)
    height = side * math.sqrt(3) / 2
    points = [
        (x1, y1 - height/2), 
        (x1 - side/2, y1 + height/2), 
        (x1 + side/2, y1 + height/2)
    ]
    pygame.draw.polygon(surface, get_current_color(), points, thickness)

# Draw a diamond/rhombus shape
def draw_rhombus(surface, start, end):
    x1, y1 = start
    x2, y2 = end
    points = [
        ((x1 + x2) / 2, y1), # Top point
        (x2, (y1 + y2) / 2), # Right point
        ((x1 + x2) / 2, y2), # Bottom point
        (x1, (y1 + y2) / 2)  # Left point
    ]
    pygame.draw.polygon(surface, get_current_color(), points, thickness)

# Function to draw the menu and help text
def draw_ui():
    # Draw panel background
    pygame.draw.rect(screen, (240, 240, 240), (WIDTH - 240, 10, 230, 230))
    pygame.draw.rect(screen, BLACK, (WIDTH - 240, 10, 230, 230), 2)

    # Display current settings
    screen.blit(font.render(f"Tool: {tool.upper()}", True, BLACK), (WIDTH - 230, 20))
    screen.blit(font.render(f"Size: {thickness}", True, BLACK), (WIDTH - 230, 50))
    screen.blit(font.render(f"Color: {color_name}", True, BLACK), (WIDTH - 230, 80))
    pygame.draw.rect(screen, color, (WIDTH - 60, 80, 30, 30))
    pygame.draw.rect(screen, BLACK, (WIDTH - 60, 80, 30, 30), 1)

    # Display shortcut instructions
    y_offset = 120
    controls = [
        "W: Pen | E: Eraser",
        "R: Rect | S: Square",
        "C: Circle | D: Rhombus",
        "T: R-Tri | A: E-Tri",
        "+/-: Size | SPACE: Clear"
    ]
    for text in controls:
        screen.blit(small_font.render(text, True, (50, 50, 50)), (WIDTH - 230, y_offset))
        y_offset += 22

# MAIN APPLICATION LOOP 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # HANDLE KEYBOARD
        elif event.type == pygame.KEYDOWN:
            # Change active tool
            if event.key == pygame.K_w: tool = "pen"
            elif event.key == pygame.K_e: tool = "eraser"
            elif event.key == pygame.K_r: tool = "rect"
            elif event.key == pygame.K_c: tool = "circle"
            elif event.key == pygame.K_s: tool = "square"
            elif event.key == pygame.K_t: tool = "right_triangle"
            elif event.key == pygame.K_a: tool = "equilateral_triangle"
            elif event.key == pygame.K_d: tool = "rhombus"

            # Change brush size
            elif event.key in (pygame.K_PLUS, pygame.K_EQUALS):
                thickness += 1
            elif event.key == pygame.K_MINUS and thickness > 1:
                thickness -= 1

            # Clear the entire canvas
            elif event.key == pygame.K_SPACE:
                canvas.fill(BG_COLOR)

            # Change color using numbers 0-9
            elif event.key in colors:
                color, color_name = colors[event.key]

        # HANDLE MOUSE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                drawing = True
                start_pos = last_pos = current_pos = event.pos

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                if tool in ("pen", "eraser"):
                    # Draw line from last point to current point
                    pygame.draw.line(canvas, get_current_color(), last_pos, current_pos, thickness)
                    last_pos = current_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                current_pos = event.pos

                # Draw the final shape onto the permanent canvas
                if tool == "rect": draw_rect(canvas, start_pos, current_pos)
                elif tool == "circle": draw_circle(canvas, start_pos, current_pos)
                elif tool == "square": draw_square(canvas, start_pos, current_pos)
                elif tool == "right_triangle": draw_right_triangle(canvas, start_pos, current_pos)
                elif tool == "equilateral_triangle": draw_equilateral_triangle(canvas, start_pos, current_pos)
                elif tool == "rhombus": draw_rhombus(canvas, start_pos, current_pos)

                drawing = False

    # DRAWING TO SCREEN
    screen.blit(canvas, (0, 0))

    # Show preview of shape while dragging mouse
    if drawing and tool not in ("pen", "eraser") and start_pos and current_pos:
        if tool == "rect": draw_rect(screen, start_pos, current_pos)
        elif tool == "circle": draw_circle(screen, start_pos, current_pos)
        elif tool == "square": draw_square(screen, start_pos, current_pos)
        elif tool == "right_triangle": draw_right_triangle(screen, start_pos, current_pos)
        elif tool == "equilateral_triangle": draw_equilateral_triangle(screen, start_pos, current_pos)
        elif tool == "rhombus": draw_rhombus(screen, start_pos, current_pos)

    # Draw the control menu on top
    draw_ui()

    # Update display and control frame rate
    pygame.display.flip()
    clock.tick(FPS)

# Close Pygame window
pygame.quit()