import pygame as pg
from picture_box import PictureBox


class GUI:

    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        pb_size = self.screen.get_width() // 5
        self.picture_box = PictureBox((pb_size, pb_size))

    def show_image(self, image):
        self.picture_box.show_image(image)

    def render_picture_box(self):
        pb_x = self.screen.get_width() - self.picture_box.get_width() - 10
        pb_y = self.screen.get_height() - self.picture_box.get_height() - 10
        self.screen.blit(self. picture_box, (pb_x, pb_y))

    def draw_ui(self):
        self.screen.fill(pg.Color("black"))
        self.render_picture_box()
        pg.display.update()

