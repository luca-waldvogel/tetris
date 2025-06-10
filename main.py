import pygame
import sys
pygame.init()
import random
from config import width, height
from field import draw_field, clear_lines
from piece import Piece
from ui import draw_score



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
    fall_time = 0
    fall_speed = 30
    current = Piece(random.randint(0, 6))

    while running:
        clock.tick(30)
        fall_time += 1

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
                if event.key == pygame.K_LEFT:
                    current.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    current.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    current.move(0, 1)
                elif event.key == pygame.K_UP:
                    current.rotate()

        win.fill((0, 0, 0))
        draw_field(win)
        current.draw(win)
        draw_score(win)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
