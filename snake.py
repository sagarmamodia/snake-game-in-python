import pygame as pg
from pygame.math import Vector2 as vec2
from settings import *
from random import randrange

class Snake():
    def __init__(self, game):
        self.game = game
        self.rect = pg.Rect(randrange(0, SCREEN_WIDTH, TILE_SIZE), randrange(0, SCREEN_HEIGHT, TILE_SIZE), TILE_SIZE, TILE_SIZE)
        self.direction = vec2(TILE_SIZE, 0)
        self.time = 0
        self.delay_step = 80 #milliseconds

    def control(self):
        pass

    def delta_time(self):
        current_time = pg.time.get_ticks()
        delta_time = current_time - self.time
        if delta_time > self.delay_step:
            self.time = current_time
            return True
        return False

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
    
    def draw(self):
        pg.draw.rect(self.game.display, GREEN, self.rect)

    def update(self):
        self.move()
        self.draw()

