import pygame as pg
from pygame.math import Vector2 as vec2

class Block:
    def __init__(self, number):
        self.no = number

    def draw(self, display, color, pos, size):
        pg.draw.rect(display, color, pg.Rect(pos[0], pos[1], size, size))

    