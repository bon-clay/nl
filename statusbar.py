import pygame as pg


class IOutput:

    def message(self, message):
        raise NotImplementedError("Output must have")


class StatusBar(pg.Surface, IOutput):

    def __init__(self, resolution):
        super().__init__(resolution)

    def message(self, message):
        ...
