import pygame as pg
from gui import GUI


class App:

    def __init__(self):
        self.gui = GUI()
        self.clock = pg.time.Clock()
        self.FPS = 60

    def events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()

    def run(self):
        while True:
            self.events()
            self.gui.draw_ui()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    app = App()
    app.run()
