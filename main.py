import pygame, sys, random
pygame.init()

from config import width, height
from field import draw_field, clear_lines, reset_field
from piece import Piece
from ui import draw_score, draw_pause

# ---------------------------------------------------------------------------
# Fenster & allgemeine Spielobjekte
# ---------------------------------------------------------------------------
win = pygame.display.set_mode((width, height + 60))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# ---------------------------------------------------------------------------
# Start‑Screen
# ---------------------------------------------------------------------------

def start_screen():
    """Startseite mit Buttons und Tastatur‑Steuerung"""
    font_title = pygame.font.SysFont("Arial", 48)
    font_button = pygame.font.SysFont("Arial", 28)

    button_width, button_height = 180, 50
    start_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 - 10, button_width, button_height)
    quit_button_rect  = pygame.Rect(width // 2 - button_width // 2, height // 2 + 60, button_width, button_height)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        win.fill((0, 0, 0))

        # Titel
        title_text = font_title.render("TETRIS", True, (255, 255, 255))
        win.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 3))

        # Start‑Button
        start_hover = start_button_rect.collidepoint(mouse_pos)
        start_color = (0, 180, 0) if start_hover else (0, 120, 0)
        pygame.draw.rect(win, start_color, start_button_rect)
        pygame.draw.rect(win, (255, 255, 255), start_button_rect, 2)
        start_text = font_button.render("START", True, (255, 255, 255))
        win.blit(start_text, start_text.get_rect(center=start_button_rect.center))

        # Quit‑Button
        quit_hover = quit_button_rect.collidepoint(mouse_pos)
        quit_color = (180, 0, 0) if quit_hover else (120, 0, 0)
        pygame.draw.rect(win, quit_color, quit_button_rect)
        pygame.draw.rect(win, (255, 255, 255), quit_button_rect, 2)
        quit_text = font_button.render("BEENDEN", True, (255, 255, 255))
        win.blit(quit_text, quit_text.get_rect(center=quit_button_rect.center))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button_rect.collidepoint(mouse_pos):
                    return  # Spiel starten
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
        clock.tick(60)

# ---------------------------------------------------------------------------
# Game‑Over‑Screen
# ---------------------------------------------------------------------------

def game_over():
    font_big   = pygame.font.SysFont("Arial", 48)
    font_small = pygame.font.SysFont("Arial", 24)

    text = font_big.render("GAME OVER", True, (255, 0, 0))
    info = font_small.render("ESC = Beenden | R = Neustart", True, (255, 255, 255))

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
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                elif event.key == pygame.K_r:
                    reset_field(); main(); return

# ---------------------------------------------------------------------------
# Hauptspiel‑Loop
# ---------------------------------------------------------------------------

def main():
    running, paused, music_on = True, False, True

    fall_time, fall_speed = 0, 30
    speed_interval = 5000  # alle 5 s schneller
    last_speed_update = pygame.time.get_ticks()

    current = Piece(random.randint(0, 6))

    # Musik vorbereiten
    pygame.mixer.music.load("sound/Tetris.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.15)

    def apply_volume():
        """Lautstärke abhängig von Pause‑ und Mute‑Status setzen"""
        if paused or not music_on:
            pygame.mixer.music.set_volume(0.0)
        else:
            pygame.mixer.music.set_volume(0.15)

    while running:
        clock.tick(30)

        # Geschwindigkeit erhöhen
        now = pygame.time.get_ticks()
        if now - last_speed_update > speed_interval:
            fall_speed = max(5, fall_speed - 1)
            last_speed_update = now

        if fall_time >= fall_speed:
            if not current.move(0, 1):
                try:
                    current.lock()
                except Exception:
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
                # Pause
                if event.key == pygame.K_p:
                    paused = not paused
                    apply_volume()

                # Mute (nur wenn nicht pausiert)
                elif event.key == pygame.K_m and not paused:
                    music_on = not music_on
                    apply_volume()

                # Steuerung nur wenn nicht pausiert
                if not paused:
                    if event.key == pygame.K_LEFT:  current.move(-1, 0)
                    elif event.key == pygame.K_RIGHT: current.move(1, 0)
                    elif event.key == pygame.K_DOWN: current.move(0, 1)
                    elif event.key == pygame.K_UP:   current.rotate()
                    elif event.key == pygame.K_SPACE:
                        while current.move(0, 1):
                            win.fill((0, 0, 0))
                            draw_field(win); current.draw(win)
                            draw_score(win); draw_pause(win)
                            pygame.display.update(); pygame.time.delay(5)
                        current.lock(); clear_lines(); current = Piece(random.randint(0, 6))

        # Pause‑Bildschirm
        if paused:
            win.fill((0, 0, 0))
            draw_field(win); current.draw(win)
            draw_score(win); draw_pause(win)
            font = pygame.font.SysFont("Arial", 36)
            pause_text = font.render("PAUSE", True, (255, 255, 255))
            win.blit(pause_text, (width // 2 - pause_text.get_width() // 2, height // 2))
            pygame.display.update(); continue

        fall_time += 1

        # Spiel zeichnen
        win.fill((0, 0, 0))
        draw_field(win); current.draw(win)
        draw_score(win); draw_pause(win)
        pygame.display.update()


if __name__ == "__main__":
    start_screen()
    main()
