import pygame as pg
from pygame.math import Vector2 as vec2
from settings import *
from block import *

class Snake():
    def __init__(self, display):
        self.display = display
        self.length = SNAKE_LENGTH
        self.blocks = [Block(i) for i in range(SNAKE_LENGTH)]
    
    def draw(self):
        for block in self.blocks:
            block.draw(self.display, RED, (200, 200), BLOCK_SIZE)
    
    def update(self):
        self.draw()
