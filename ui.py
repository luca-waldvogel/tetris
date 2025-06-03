import pygame
from config import height
from field import get_score

font = pygame.font.SysFont("Arial", 24)

def draw_score(surface):
    text = font.render(f"Punkte: {get_score()}", True, (255, 255, 255))
    surface.blit(text, (10, height + 20))
