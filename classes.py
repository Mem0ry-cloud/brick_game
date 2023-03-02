import pygame as pg
import sqlite3
import random

class Brick(pg.sprite.Sprite):
    def __init__(self, position, size, image="image", health=1, color=(255, 255, 255), on_collide=print):
        super().__init__()
        self.position = position
        self.size = size
        self.image = pg.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = position
        self.health = health
        self.color = color
        self.on_collide = on_collide
        colorImage = pg.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(self.color)
        self.image.blit(colorImage, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    def update(self):
        self.health -= 1
        if self.health == 0:
            if self.on_collide != print:
                self.on_collide(self.rect.x, self.rect.y)
            self.kill()


class Box(pg.sprite.Sprite):
    def __init__(self, groups, position, size, image="image", speed=1, on_collide=print):
        super().__init__(*groups)
        self.position = position
        self.size = size
        self.image = pg.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = position
        self.speed = speed
        self.on_collide = on_collide

    def update(self, args=False):
        if args == True:
            if self.on_collide != print:
                self.on_collide()
            self.kill()
            return
        self.rect.y += self.speed


class Ball(pg.sprite.Sprite):
    def __init__(self, groups, position, vector=(1, 1), size=(5, 5), image="image"):
        super().__init__(*groups)
        self.size = size
        self.vector = vector
        self.image = pg.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = position

    def update(self, args):
        if len(args) == 0:
            x, y = self.vector
            self.rect.x += x
            self.rect.y += y
        else:
            x, y = self.vector
            x1, y1 = args
            x *= x1
            if x == 0:
                x = -1
            y *= y1
            if y == 0:
                y = -1
            self.vector = x, y


class Map(pg.sprite.Sprite):
    def __init__(self, groups, position, size, mapping, brick_image="brick_image", on_collide=print, box_chance=100):
        super().__init__(*groups)
        self.position = position
        self.size = size
        self.mapping = mapping
        self.brick_image = brick_image
        self.bricks = pg.sprite.Group()
        self.on_collide = on_collide
        self.box_chance = box_chance

        for i in range(50):
            for j in range(50):
                curr = self.mapping[i * 50 + j]
                if curr[0] != 0:
                    x, y = position
                    xs, ys = size
                    if on_collide != print and random.randint(0, 100) <= box_chance:
                        self.bricks.add(Brick((x + j * (xs + 1), y + i * (ys + 1)), size, brick_image, *curr, on_collide=on_collide))
                    else:
                        self.bricks.add(Brick((x + j * (xs + 1), y + i * (ys + 1)), size, brick_image, *curr))

    def draw_all(self, screen):
        self.bricks.draw(screen)

    def update_all(self, args):
        self.bricks.update()


class Platform(pg.sprite.Sprite):
    def __init__(self, groups, position, size, image="image", speed=5, max_speed=10):
        super().__init__(*groups)
        self.size = size
        self.image = pg.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = position
        self.speed = speed
        self.curr_arg = 0
        self.curr_speed = speed
        self.max_speed = max_speed

    def update(self, args):
        if args != self.curr_arg:
            self.curr_arg = args
            self.curr_speed = self.speed
        else:
            self.curr_speed = min(self.curr_speed + 0.8, self.max_speed)
        self.rect.x += int(args * self.curr_speed)


class Cursor:
    def __init__(self):
        self.connection = sqlite3.connect("brick_game_maps.db")

    def add_info(self, info):
        pass

    def add_map(self, map_name, uncoded_map):
        file = open(map_name, mode='w')
        sym = ["0", "@", "*", "#", '&', '^', '%', '!', '/', '<', '>', '?']
        blocks = [0, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coded_map = ''
        for i in uncoded_map:
            symbol_index = blocks.index(i)
            coded_map += sym[symbol_index]
        file.write(coded_map)
        request = f'INSERT INTO maps(map_name, key' \
                  f'VALUES("{map_name}", "map\{map_name}.txt")'
        self.connection.cursor().execute(request)
        self.connection.commit()

    def get_info(self, type_info='all', name_file='test'):
        if type_info == 'all':
            request = f'SELECT map_name, key, creater FROM maps WHERE map_name = "{name_file}"'
            res = self.connection.cursor().execute(request).fetchall()
        elif type_info == 'key':
            request = f'SELECT key FROM maps WHERE map_name = "{name_file}"'
            res = self.connection.cursor().execute(request).fetchall()
            res = ' '.join(res[0])
        elif type_info == 'creater':
            request = f'SELECT creater FROM maps WHERE map_name = "{name_file}"'
            res = self.connection.cursor().execute(request).fetchall()
        return res

    def get_map(self, map_name, form='list'):
        sym = ["0", "@", "*", "#", '&', '^', '%', '!', '/', '<', '>', '?']
        format_sym = [[0, (255, 255, 255)], [-1, (0, 0, 0)], [1, (255, 0, 0)], [2, (255, 165, 0)], [3, (255, 255, 0)],
                      [4, (255, 255, 153)], [5, (0, 128, 0)], [6, (8, 189, 255)], [7, (8, 82, 255)], [8, (8, 99, 255)],
                      [9, (0, 0, 255)], [10, (102, 11, 186)]]
        map_key = self.get_info("key", map_name)
        map_file = open(map_key, encoding='utf8')
        map_coded = map_file.read()
        map_uncoded = []
        for i in map_coded:
            symbol_index = sym.index(i)
            map_uncoded.append(format_sym[symbol_index])
        return map_uncoded


class Button(pg.sprite.Sprite):
    def __init__(self, groups, position, size, color=(255, 255, 255), on_click=print, image="image", used_image=None, label="nothing",
                 font=None, font_size=36, font_color=(180, 0, 0), label_pos=(310, 50)):
        super().__init__(*groups)
        self.position = position #позиция image
        self.size = size #size image

        self.image = pg.transform.scale(image, size)
        self.default_image = self.image #начальная image
        self.used_image = self.default_image #image когда на кнопку навели
        if used_image is not None:
            self.used_image = pg.transform.scale(used_image, size)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = position
        self.color = color #цвет image
        colorImage = pg.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        self.on_click = on_click
        # font, текст
        self.label = label
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.label_pos = label_pos

    def get_blit(self): #нужен для рендера текста в окне
        return [(pg.font.Font(self.font, self.font_size).render(self.label, True, self.font_color)), (self.label_pos)]

    def update(self, args, is_not_click=False):
        if is_not_click: #used
            if self.rect.collidepoint(*list(args)):
                self.image = self.used_image
            else:
                self.image = self.default_image
            self.rect = self.image.get_rect()
            self.mask = pg.mask.from_surface(self.image)
            self.rect.x, self.rect.y = self.position
        else:
            if self.rect.collidepoint(*list(args)) and self.on_click is not print:
                self.on_click()