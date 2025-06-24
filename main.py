import pygame, sys, random
pygame.init()
from config import width, height
from field import draw_field, clear_lines, reset_field
from piece import Piece
from ui import draw_score, draw_pause



win = pygame.display.set_mode((width, height + 60))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont("Arial", 48)
    small_font = pygame.font.SysFont("Arial", 24)
    text = font.render("GAME OVER", True, (255, 0, 0))
    info = small_font.render("ESC = Beenden | R = Neustart", True, (255, 255, 255))
    pygame.mixer.music.set_volume(0.0)
    game_over_sound = pygame.mixer.Sound("sound/game_over.mp3")
    game_over_sound.set_volume(0.17)
    game_over_sound.play()
    

    while True:
        win.fill((0, 0, 0))
        win.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 30))
        win.blit(info, (width // 2 - info.get_width() // 2, height // 2 + 30))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    reset_field()
                    main()  # Spiel neu starten
                    return

def main():
    running = True
    paused = False
    music_on = True
    fall_time = 0
    fall_speed = 30
    speed_increase_interval = 5000  # alle 5 Sekunden schneller
    last_speed_update = pygame.time.get_ticks()
    current = Piece(random.randint(0, 6))

    pygame.mixer.music.load("sound/Tetris.mp3")
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)

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
                    pygame.mixer.music.set_volume(0.15)
                    if event.key == pygame.K_m:
                        if music_on:
                            pygame.mixer.music.set_volume(0.0)
                            music_on = False
                        else:
                            pygame.mixer.music.set_volume(0.15)
                            music_on = True
                    if event.key == pygame.K_LEFT:
                        current.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        current.move(1, 0)
                    elif event.key == pygame.K_DOWN:
                        current.move(0, 1)
                    elif event.key == pygame.K_UP:
                        current.rotate()
                    elif event.key == pygame.K_SPACE:
                        # Animiertes Fallen
                        while current.move(0, 1):
                            win.fill((0, 0, 0))
                            draw_field(win)
                            current.draw(win)
                            draw_score(win)
                            draw_pause(win)
                            pygame.display.update()
                            pygame.time.delay(5)  # kleine Verspätung 
                        current.lock()
                        clear_lines()
                        current = Piece(random.randint(0, 6))
                
        if paused:
            win.fill((0, 0, 0))
            draw_field(win)
            current.draw(win)
            draw_score(win)
            draw_pause(win)
            pygame.mixer.music.set_volume(0.0)
            
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
