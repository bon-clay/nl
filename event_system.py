import pygame as pg


class Event:

    def __init__(self):
        self.subs = []

    def subscribe(self, sub):
        self.subs.append(sub)

    def unsubscribe(self, sub):
        self.subs.remove(sub)

    def invoke(self, *args, **kwargs):
        output = kwargs["output"]
        message = kwargs["message"]
        if output is None and isinstance(output, IOutput):
            output.message(message)
        for sub in self.subs:
            sub.update_event(*args, **kwargs)


class EventSystem():

    event_types = {
            "start_button_event": Event(),
            }
    mouse_event_handlers = []

    def reg_mouse_handle(self, handler):
        self.mouse_event_handlers.append(handler)

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type in [pg.MOUSEBUTTONDOWN,
                    pg.MOUSEBUTTONUP,
                    pg.MOUSEMOTION]:
                for handler in self.mouse_event_handlers:
                    handler.mouse_handle(event, mouse_pos)

    def subscribe(self, event_type, sub):
        EventSystem.event_types[event_type].subscribe(sub)

    def unsubscribe(event_type, sub):
        EventSystem.event_types[event_type].unsubscribe(sub)

    def __getitem__(self, item):
        return self.event_types[item]

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


event_system_instance = EventSystem(status_bar)
