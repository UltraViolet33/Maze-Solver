import pygame as pg
import sys
from settings import *


class Maze:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        pg.display.set_caption("Generation and solving maze using DFS")
        self.clock = pg.time.Clock()

    def update(self):
        pg.display.flip()

    def draw(self):
        pass

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.clock.tick(FPS)
