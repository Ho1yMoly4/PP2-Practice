import pygame
import sys
import os
from player import MusicPlayer

WIDTH, HEIGHT = 600, 400
FPS = 30
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (0, 255, 127)
GRAY = (150, 150, 150)

def draw_text(surface, text, font, color, pos):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, pos)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Keyboard Music Player")
    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("Arial", 24)
    small_font = pygame.font.SysFont("Arial", 18)

    base_path = os.path.dirname(os.path.abspath(__file__))
    music_folder = os.path.join(base_path, "music")
    
    player = MusicPlayer(music_folder)

    running = True
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.prev_track()
                elif event.key == pygame.K_q:
                    running = False

        track_name = player.get_current_track_name()
        status = "Playing" if player.is_playing else "Stopped"
        time_pos = player.get_pos()

        pygame.draw.rect(screen, (40, 40, 40), (30, 50, 540, 200), border_radius=10)
        
        draw_text(screen, f"Track: {track_name}", font, WHITE, (50, 80))
        draw_text(screen, f"Status: {status}", font, GREEN, (50, 130))
        draw_text(screen, f"Time: {time_pos} sec", font, WHITE, (50, 180))
        
        controls = "P: Play | S: Stop | N: Next | B: Prev | Q: Quit"
        draw_text(screen, controls, small_font, GRAY, (50, 320))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()