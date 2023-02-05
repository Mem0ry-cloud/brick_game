import pygame as pg
import sqlite3


class Cursor:
    def __init__(self):
        self.connection = sqlite3.connect("brick_game_maps.db")
    def add_info(self, info):
        pass

    def get_info(self, type_info, name):
        if type_info == 'all':
            request = f'SELECT map_name, key, creater FROM maps WHERE map_name = "{name}"'
        elif type_info == 'key':
            request = f'SELECT key FROM maps WHERE map_name = "{name}"'
        elif type_info == 'creater':
            request = f'SELECT creater FROM maps WHERE map_name = "{name}"'
        res = self.connection.cursor().execute(request).fetchall()
        return res

class Label(pg.sprite.Sprite):
    def __init__(self, position, size, color, text):
        self.position = position
        self.size = size
        self.color = color
        self.text = text
        pass


class Button(pg.sprite.Sprite):
    def __init__(self, groups, position, size, color, on_click, image="image", used_image="used_image", label="nothing", font=None, font_size=36, font_color=(180, 0, 0), label_pos=(310, 50)):
        super().__init__(*groups)
        self.position = position
        self.size = size

        self.image = pg.transform.scale(image, size)
        self.default_image = self.image
        self.used_image = pg.transform.scale(used_image, size)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = position

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

    def update(self, args, used=False):
        if used:
            if self.rect.collidepoint(*list(args)):
                self.image = self.used_image
            else:
                self.image = self.default_image
            self.rect = self.image.get_rect()
            self.mask = pg.mask.from_surface(self.image)
            self.rect.x, self.rect.y = self.position
        else:
            if self.rect.collidepoint(*list(args)):
                self.on_click()

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
