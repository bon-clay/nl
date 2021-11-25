import pygame as pg


class GUI:

    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))

    def draw_ui(self):
        self.screen.fill(pg.Color("black"))

