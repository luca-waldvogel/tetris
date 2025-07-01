import pytest
from config import cols, rows
from field import reset_field
from piece import Piece

@pytest.fixture(autouse=True)
def clear_field():
    # Arrange (gemeinsame Einrichtung für alle Tests)
    reset_field()
    yield
    reset_field()

def test_shape_cannot_move_out_of_left_boundary():
    # Arrange
    piece = Piece(shape_index=0)            # I-Form
    piece.col = 0                           # ganz links
    # Act
    moved = piece.move(dx=-1, dy=0)         # nach links verschieben
    # Assert
    assert moved is False, "Shape sollte sich nicht links über den Rand bewegen können"

def test_shape_cannot_move_out_of_right_boundary():
    # Arrange
    piece = Piece(shape_index=0)
    # platziere rechts: cols = Gesamtspalten, Breite der Form = 4
    piece.col = cols - len(piece.shape[0])  
    # Act
    moved = piece.move(dx=1, dy=0)          # nach rechts verschieben
    # Assert
    assert moved is False, "Shape sollte sich nicht rechts über den Rand bewegen können"

def test_shape_cannot_move_out_of_bottom_boundary():
    # Arrange
    piece = Piece(shape_index=0)
    piece.row = rows - len(piece.shape)     # ganz unten
    # Act
    is_valid = piece.valid_position(row=piece.row + 1,
                                    col=piece.col,
                                    shape=piece.shape)
    # Assert
    assert is_valid is False, "Shape sollte sich nicht unterhalb des Spielfeldes bewegen können"