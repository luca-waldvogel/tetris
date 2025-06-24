import pygame
from config import height, width
from field import get_score

font = pygame.font.SysFont("Arial", 24)
fontSmall = pygame.font.SysFont("Arial", 20)

def draw_score(surface):
    text = font.render(f"Punkte: {get_score()}", True, (255, 255, 255))
    surface.blit(text, (10, height + 20))

def draw_pause(surface):
    text = fontSmall.render("M = Mute / P = Pause", True, (255, 255, 255))
    text_rect = text.get_rect()
    x_pos = width - text_rect.width - 10  # 10 Pixel Abstand vom rechten Rand
    surface.blit(text, (x_pos, height + 25))
