import pygame as pg


class PictureBox(pg.Surface):

    def __init__(self, resolution):
        super().__init__(resolution)
        self.fill(pg.Color("green"))

    def show_image(self, image):
        image = pg.transform.scale(image, self.get_size())
        self.blit(image, (0, 0))

