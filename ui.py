import pygame
from config import height, width
from field import get_score, get_all_scores

font = pygame.font.SysFont("Arial", 24)

def draw_score(surface):
    text = font.render(f"Punkte: {get_score()}", True, (255, 255, 255))
    surface.blit(text, (10, height + 20))

def draw_pause(surface):
    text = font.render("P = Pause", True, (255, 255, 255))
    text_rect = text.get_rect()
    x_pos = width - text_rect.width - 10  # 10 Pixel Abstand vom rechten Rand
    surface.blit(text, (x_pos, height + 20))

def draw_scoreboard(surface):
    x_offset = width + 10
    y_offset = 10
    # Scoreboard-Hintergrund immer zeichnen
    pygame.draw.rect(surface, (0, 0, 0), (width, 0, 160, height))  

    title_text = font.render("Highscores", True, (255, 255, 255))
    surface.blit(title_text, (x_offset, y_offset))
    y_offset += 30

    for idx, punkte in enumerate(get_all_scores()):
        text = font.render(f"{idx+1}. {punkte}", True, (255, 255, 255))
        surface.blit(text, (x_offset, y_offset + idx * 30))


