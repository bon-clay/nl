from PIL import Image
import os
from time import sleep


class TestNetwork:

    def __init__(self):
        images_paths = os.listdir("imgs")
        self.index = -1
        self.images = [Image.open(f"imgs/{img_pth}") for img_pth in images_paths]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = -1
            raise StopIteration
        return self.images[self.index]



