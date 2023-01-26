import pygame as pg
from sys import exit
from pygame.math import Vector2 as vec2
from settings import *
from snake import *
from block import *


class Game:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display.fill(WHITE)
        self.snake = Snake(self.display) #Created a snake object

    def run(self):
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            
            self.update()
            pg.display.update()
    
    def update(self):
        self.draw_grid()
        self.snake.update() #updating snake at every frame

    def draw_grid(self):
        #vertical lines
        for i in range(1, int(SCREEN_WIDTH/BLOCK_SIZE)):
            pg.draw.line(self.display, BLACK, (i * BLOCK_SIZE, 0), (i*BLOCK_SIZE, SCREEN_HEIGHT))
        for i in range(1, int(SCREEN_HEIGHT/BLOCK_SIZE)):
            pg.draw.line(self.display, BLACK, (0, i * BLOCK_SIZE), (SCREEN_WIDTH, i * BLOCK_SIZE))


if __name__ == '__main__':

    game = Game()
    game.run()



