import pygame as pg
from event_system import event_system_instance as ES



class Button(pg.Rect):

    colors = {
            "normal": pg.Color("green"),
            "hover": pg.Color("orange"),
            "pressed": pg.Color("lightblue")
            }

    def __init__(self, x, y, width, height, text, event_type):
        super().__init__(x, y, width, height)
        self.text = text
        self.event = ES[event_type]
        ES.reg_mouse_handle(self)
        self.color = self.colors["normal"]

    def mouse_handle(self, event, mouse_pos):
        if self.collidepoint(mouse_pos):
            if event.type == pg.MOUSEBUTTONDOWN:
                self.color = self.colors["pressed"]
                self.on_click()
            if event.type == pg.MOUSEBUTTONUP or \
                    event.type == pg.MOUSEMOTION:
                self.color = self.colors["hover"]
        else:
            self.color = self.colors["normal"]

    def draw(self, display):
        pg.draw.rect(display, self.color, self)

    def on_click(self):
        self.event.invoke()
