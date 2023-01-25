import pygame as pg
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
    def __init__(self, groups, position, size, color, on_click, label="nothing", font=None, font_size=36, font_color=(180, 0, 0), label_pos=(310, 50)):
        super().__init__(*groups)
        self.position = position
        self.size = size
        self.color = color
        self.on_click = on_click
        #font
        self.label = label
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.label_pos = label_pos
    def get_blit(self):
        return [(pg.font.Font(self.font, self.font_size).render(self.label, True, self.font_color)), (self.label_pos)]
        #return (pg.font.Font(None, 36).render('Stones Game', True, (180, 0, 0)), (310, 50))
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
