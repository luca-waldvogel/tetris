import pygame
from config import cols, rows
from shapes import COLORS, BLACK, GRAY

field = [[0 for _ in range(cols)] for _ in range(rows)]
score = 0
all_scores = []  # alle Scores sammeln


def draw_field(surface):
    for y in range(rows):
        for x in range(cols):
            val = field[y][x]
            color = COLORS[val - 1] if val else BLACK
            pygame.draw.rect(surface, color, (x * 30, y * 30, 30, 30))
            pygame.draw.rect(surface, GRAY, (x * 30, y * 30, 30, 30), 1)

def clear_lines():
    global field, score
    new_field = [row for row in field if any(cell == 0 for cell in row)]
    lines_cleared = rows - len(new_field)
    clear_sound = pygame.mixer.Sound("sound/Clear.mp3")
    clear_sound.set_volume(0.2)
    
    for _ in range(lines_cleared):
        new_field.insert(0, [0 for _ in range(cols)])
        clear_sound.play()
    field = new_field
    score += lines_cleared * 100

def get_field():
    return field

def get_score():
    return score

def reset_field():
    global field, score
    field = [[0 for _ in range(cols)] for _ in range(rows)]
    score = 0

def get_all_scores():
    return all_scores


