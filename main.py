import pygame as pg
from sys import exit
from pygame.math import Vector2 as vec2
from settings import *
from snake import *


class Game:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_grid(self):
        #vertical lines
        for i in range(1, int(SCREEN_WIDTH/BLOCK_SIZE)):
            pg.draw.line(self.display, GREY, (i * BLOCK_SIZE, 0), (i*BLOCK_SIZE, SCREEN_HEIGHT))
        #Horizontal lines
        for i in range(1, int(SCREEN_HEIGHT/BLOCK_SIZE)):
            pg.draw.line(self.display, GREY, (0, i * BLOCK_SIZE), (SCREEN_WIDTH, i * BLOCK_SIZE))
      
    def run(self):  
        while True:
            self.display.fill(BLACK)
            self.update()
            pg.display.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
    
    def update(self):
        self.check_events()
        self.draw_grid()


if __name__ == '__main__':

    game = Game()
    game.run()



