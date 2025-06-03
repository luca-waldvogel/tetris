import pygame
import random

pygame.init()

# Konfiguration
cols, rows = 10, 20
block_size = 30
width = cols * block_size
height = rows * block_size

# Farben
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# Tetris-Formen mit Rotationen
SHAPES = [
    # I
    [[[1, 1, 1, 1]],
     [[1], [1], [1], [1]]],
    # J
    [[[1, 0, 0], [1, 1, 1]],
     [[1, 1], [1, 0], [1, 0]],
     [[1, 1, 1], [0, 0, 1]],
     [[0, 1], [0, 1], [1, 1]]],
    # L
    [[[0, 0, 1], [1, 1, 1]],
     [[1, 0], [1, 0], [1, 1]],
     [[1, 1, 1], [1, 0, 0]],
     [[1, 1], [0, 1], [0, 1]]],
    # O
    [[[1, 1], [1, 1]]],
    # S
    [[[0, 1, 1], [1, 1, 0]],
     [[1, 0], [1, 1], [0, 1]]],
    # T
    [[[0, 1, 0], [1, 1, 1]],
     [[1, 0], [1, 1], [1, 0]],
     [[1, 1, 1], [0, 1, 0]],
     [[0, 1], [1, 1], [0, 1]]],
    # Z
    [[[1, 1, 0], [0, 1, 1]],
     [[0, 1], [1, 1], [1, 0]]]
]

win = pygame.display.set_mode((width, height + 60))
pygame.display.set_caption("Tetris")

font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
field = [[0 for _ in range(cols)] for _ in range(rows)]
score = 0

class Piece:
    def __init__(self, shape_index):
        self.shape_index = shape_index
        self.rotations = SHAPES[shape_index]
        self.rotation = 0
        self.shape = self.rotations[self.rotation]
        self.color = COLORS[shape_index]
        self.row = 0
        self.col = cols // 2 - len(self.shape[0]) // 2

    def rotate(self):
        next_rotation = (self.rotation + 1) % len(self.rotations)
        next_shape = self.rotations[next_rotation]
        if self.valid_position(self.row, self.col, next_shape):
            self.rotation = next_rotation
            self.shape = next_shape

    def valid_position(self, row, col, shape=None):
        shape = shape or self.shape
        for y, r in enumerate(shape):
            for x, cell in enumerate(r):
                if cell:
                    nx, ny = col + x, row + y
                    if nx < 0 or nx >= cols or ny >= rows:
                        return False
                    if ny >= 0 and field[ny][nx]:
                        return False
        return True

    def move(self, dx, dy):
        if self.valid_position(self.row + dy, self.col + dx):
            self.row += dy
            self.col += dx
            return True
        return False

    def lock(self):
        for y, row_data in enumerate(self.shape):
            for x, cell in enumerate(row_data):
                if cell:
                    fy, fx = self.row + y, self.col + x
                    if fy < 0:
                        raise Exception("Game Over")
                    field[fy][fx] = self.shape_index + 1

    def draw(self, surface):
        for y, row_data in enumerate(self.shape):
            for x, cell in enumerate(row_data):
                if cell:
                    pygame.draw.rect(surface, self.color, ((self.col + x) * block_size,
                                                           (self.row + y) * block_size,
                                                           block_size, block_size))

def draw_field(surface):
    for y in range(rows):
        for x in range(cols):
            val = field[y][x]
            color = COLORS[val - 1] if val else BLACK
            pygame.draw.rect(surface, color, (x * block_size, y * block_size, block_size, block_size))
            pygame.draw.rect(surface, GRAY, (x * block_size, y * block_size, block_size, block_size), 1)

def clear_lines():
    global field, score
    new_field = [row for row in field if any(cell == 0 for cell in row)]
    lines_cleared = rows - len(new_field)
    for _ in range(lines_cleared):
        new_field.insert(0, [0 for _ in range(cols)])
    field = new_field
    score += lines_cleared * 100

def draw_score(surface):
    text = font.render(f"Punkte: {score}", True, (255, 255, 255))
    surface.blit(text, (10, height + 20))

def main():
    global score
    running = True
    fall_time = 0
    fall_speed = 30
    current = Piece(random.randint(0, len(SHAPES) - 1))

    while running:
        clock.tick(30)
        fall_time += 1

        if fall_time >= fall_speed:
            if not current.move(0, 1):
                try:
                    current.lock()
                except:
                    running = False
                    continue
                clear_lines()
                current = Piece(random.randint(0, len(SHAPES) - 1))
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

        win.fill(BLACK)
        draw_field(win)
        current.draw(win)
        draw_score(win)
        pygame.display.update()

    pygame.quit()

main()
