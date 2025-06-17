import pygame
from config import cols, block_size
from shapes import COLORS, SHAPES
from field import get_field

class Piece:
    def __init__(self, shape_index):
        self.shape_index = shape_index
        self.rotations = SHAPES[shape_index]
        self.rotation = 0
        self.shape = self.rotations[self.rotation]
        self.color = COLORS[shape_index]
        self.row = 0
        self.col = cols // 2 - len(self.shape[0]) // 2
        self.rotate_sound = pygame.mixer.Sound("sound/rotate.ogg")
        self.rotate_sound.set_volume(0.3)

    def rotate(self):
        next_rotation = (self.rotation + 1) % len(self.rotations)
        next_shape = self.rotations[next_rotation]
        if self.valid_position(self.row, self.col, next_shape):
            self.rotation = next_rotation
            self.shape = next_shape
            self.rotate_sound.play()

    def valid_position(self, row, col, shape=None):
        shape = shape or self.shape
        field = get_field()
        for y, r in enumerate(shape):
            for x, cell in enumerate(r):
                if cell:
                    nx, ny = col + x, row + y
                    if nx < 0 or nx >= cols or ny >= len(field):
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
        from field import get_field
        field = get_field()
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
