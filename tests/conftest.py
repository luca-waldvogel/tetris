# tests/conftest.py
import sys, os

# Projekt-Root ins sys.path packen
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, project_root)

# Dummy-Shim für pygame.mixer.Sound
import pygame
from types import SimpleNamespace

if not hasattr(pygame, 'mixer'):
    pygame.mixer = SimpleNamespace()

class DummySound:
    def __init__(self, *args, **kwargs):
        pass
    def play(self, *args, **kwargs):
        pass
    def set_volume(self, *args, **kwargs):
        pass  # stub, macht nichts

pygame.mixer.init   = lambda *args, **kwargs: None
pygame.mixer.Sound  = DummySound