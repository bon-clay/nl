import pygame as pg
from gui import GUI
from event_system import event_system_instance as ES


class Start:

    def __init__(self, event_type):
        ES.subscribe(event_type, self)

    def update_event(sefl):
        print("[STARTED]")

class App:

    def __init__(self):
        self.gui = GUI() # first init
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.img = pg.Surface((10, 10))
        self.start = Start("start_button_event")

    def run(self):
        while True:
            ES.update()
            self.gui.draw_ui()
            self.clock.tick(self.FPS)
            pg.display.set_caption(str(self.clock.get_fps()))

if __name__ == "__main__":
    app = App()
    app.run()
