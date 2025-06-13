import pygame
import sys
pygame.init()
import random
from config import width, height
from field import draw_field, clear_lines
from piece import Piece
from ui import draw_score, draw_pause



win = pygame.display.set_mode((width, height + 60))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

def game_over():
    print
    "Game Over! Thanks for playing!"
    pygame.quit()
    sys.exit()

def main():
    running = True
    paused = False
    fall_time = 0
    fall_speed = 30
    speed_increase_interval = 5000  # alle 5 Sekunden schneller
    last_speed_update = pygame.time.get_ticks()
    current = Piece(random.randint(0, 6))

    while running:
        clock.tick(30)
        

        # Geschwindigkeitserhöhung mit der Zeit
        current_time = pygame.time.get_ticks()
        if current_time - last_speed_update > speed_increase_interval:
            fall_speed = max(5, fall_speed - 1)  # Minimale Geschwindigkeit 5
            last_speed_update = current_time

        if fall_time >= fall_speed:
            if not current.move(0, 1):
                try:
                    current.lock()
                except:
                    game_over()
                
                clear_lines()
                current = Piece(random.randint(0, 6))

                if not current.valid_position(current.row, current.col):
                    game_over()
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if not paused:
                    if event.key == pygame.K_LEFT:
                        current.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        current.move(1, 0)
                    elif event.key == pygame.K_DOWN:
                        current.move(0, 1)
                    elif event.key == pygame.K_UP:
                        current.rotate()
                    elif event.key == pygame.K_SPACE:
                        # Block sofort auf den Boden bewegen
                        while current.move(0, 1):
                            pass
                        current.lock()
                        clear_lines()
                        current = Piece(random.randint(0, 6))
                
        if paused:
            win.fill((0, 0, 0))
            draw_field(win)
            current.draw(win)
            draw_score(win)
            draw_pause(win)
            
            # Pausenanzeige
            font = pygame.font.SysFont("Arial", 36)
            pause_text = font.render("PAUSE", True, (255, 255, 255))
            win.blit(pause_text, (width // 2 - pause_text.get_width() // 2, height // 2))
            pygame.display.update()
            continue  # Überspringt den Rest der Schleife

        fall_time += 1
        
        # Spielfeld zeichnen
        win.fill((0, 0, 0))
        draw_field(win)
        current.draw(win)
        draw_score(win)
        draw_pause(win)
        pygame.display.update()

if __name__ == "__main__":
    main()
