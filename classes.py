import pygame as pg
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Cursor:
    pass


class Label(pg.sprite.Sprite):
    def __init__(self, position, size, color, text):
        self.position = position
        self.size = size
        self.color = color
        self.text = text
        pass


class Button(pg.sprite.Sprite):
    def __init__(self, position, size, color, on_click, label=None):
        self.position = position
        self.size = size
        self.color = color
        self.label = label
        self.on_click = on_click


class GameObject(pg.sprite.Sprite):
    def __init__(self, position, size, *sprite_groups):
        super().__init__(*sprite_groups)
        self.position = position
        self.size = size

class Brick(GameObject):
    def __init__(self, position, size, health):
        #super().__init__()
        pass


class Ball(GameObject):
    def __init__(self, position, size, velocity):
        #super().__init__()
        pass


class Platform(GameObject):
    def __init__(self, position, size, time=None):   #время до исчезновения
        #super().__init__()
        self.time = time

    def update(self):
        pass

class PlayerPlatform(Platform):
    def __init__(self):
        #super().__init__()
        pass
    def update(self):
        pass
