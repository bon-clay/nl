import pygame as pg


class App:

    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()
        self.FPS = 60

    def events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()

    def run(self):
        while True:
            self.events()
            self.screen.fill(pg.Color("black"))
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    app = App()
    app.run()
