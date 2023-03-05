import datetime
import random

import classes
import os
import sys
import pygame as pg
import MapMaker

from timeit import default_timer

def load_image(name, colorkey=None):
    fullname = name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Window:
    def __init__(self, size=(800, 850)):
        self.size = size
        self.ui = pg.sprite.Group()
        self.next_window = -1

    def start(self):
        return -1


class MainMenuWindow(Window):
    def __init__(self):
        super().__init__()

    def on_click_1(self):
        self.next_window = 5
        self.running = False

    def on_click_2(self):
        self.next_window = 3
        self.running = False

    def on_click_3(self):
        self.next_window = 2
        self.running = False

    def on_click_4(self):
        self.next_window = 4
        self.running = False

    def start(self):
        pg.init()
        FPS = 50
        SIZE = self.size
        screen = pg.display.set_mode(SIZE)
        ui = pg.sprite.Group()
        buttons = pg.sprite.Group()
        fonts = []
        (classes.Button([buttons], (300, 100), (300, 100), on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="Играть", label_pos=(310, 120), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (300, 250), (300, 100), on_click=self.on_click_2,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="Кампания", label_pos=(310, 270), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (300, 400), (350, 100), on_click=self.on_click_3,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="Мастерская", label_pos=(310, 420), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (300, 550), (350, 100), on_click=self.on_click_4,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="Скины", label_pos=(310, 570), font_color=(180, 180, 0), font_size=80))
        # ещё переделаю это
        fonts.append((pg.font.Font(None, 50).render('Стонес Гаме', True, (180, 0, 0)), (310, 0)))
        fonts.append((pg.font.Font(None, 50).render('Сделано с божьей помощью', True, (90, 0, 0)), (200, 700)))

        def main():
            self.running = True
            clock = pg.time.Clock()
            player = None
            while self.running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                        break
                    if event.type == pg.MOUSEBUTTONDOWN:
                        buttons.update(event.pos)
                buttons.update(pg.mouse.get_pos(), True)
                screen.fill('white')
                buttons.draw(screen)
                [screen.blit(*i.get_blit()) for i in buttons]
                [screen.blit(*i) for i in fonts]
                ui.draw(screen)
                pg.display.flip()
                clock.tick(FPS)

        main()
        return self.next_window


class CampaignMenuWindow(Window):
    def __init__(self):
        super().__init__()
        self.map = None

    def on_click_1(self):
        self.next_window = -1
        self.map = "1_map"
        self.running = False

    def on_click_2(self):
        self.next_window = -1
        self.map = "2_map"
        self.running = False

    def on_click_3(self):
        self.next_window = -1
        self.map = "3_map"
        self.running = False

    def on_click_4(self):
        self.next_window = -1
        self.map = "4_map"
        self.running = False

    def on_click_5(self):
        self.next_window = -1
        self.map = "5_map"
        self.running = False

    def on_click_6(self):
        self.next_window = -1
        self.map = "6_map"
        self.running = False

    def go_back(self):
        self.next_window = 0
        self.running = False

    def start(self):
        pg.init()
        FPS = 50
        SIZE = self.size
        screen = pg.display.set_mode(SIZE)
        ui = pg.sprite.Group()
        buttons = pg.sprite.Group()
        fonts = []
        (classes.Button([buttons], (100, 100), (70, 70), on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="1", label_pos=(115, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (200, 100), (70, 70), on_click=self.on_click_2,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="2", label_pos=(215, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (300, 100), (70, 70), on_click=self.on_click_3,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="3", label_pos=(315, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (400, 100), (70, 70), on_click=self.on_click_4,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="4", label_pos=(415, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (500, 100), (70, 70), on_click=self.on_click_5,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="5", label_pos=(515, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (600, 100), (70, 70), on_click=self.on_click_6,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="6", label_pos=(615, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (550, 720), (200, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="назад", label_pos=(565, 735), font_color=(180, 180, 0), font_size=80))
        # ещё переделаю это
        fonts.append((pg.font.Font(None, 50).render('Выбор уровня', True, (180, 0, 0)), (310, 0)))

        def main():
            self.running = True
            clock = pg.time.Clock()
            player = None
            while self.running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                        break
                    if event.type == pg.MOUSEBUTTONDOWN:
                        buttons.update(event.pos)
                buttons.update(pg.mouse.get_pos(), True)
                screen.fill('white')
                buttons.draw(screen)
                [screen.blit(*i.get_blit()) for i in buttons]
                [screen.blit(*i) for i in fonts]
                ui.draw(screen)
                pg.display.flip()
                clock.tick(FPS)

        main()
        return self.next_window, self.map


class LevelsMenuWindow(Window):
    def __init__(self):
        super().__init__()

    def on_click_1(self):
        self.running = False

    def go_back(self):
        self.next_window = 0
        self.running = False

    def start(self):
        pg.init()
        FPS = 50
        SIZE = self.size
        screen = pg.display.set_mode(SIZE)
        ui = pg.sprite.Group()
        buttons = pg.sprite.Group()
        fonts = []
        (classes.Button([buttons], (550, 720), (200, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="назад", label_pos=(565, 735), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (470, 620), (250, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="рандом", label_pos=(485, 635), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (70, 620), (250, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="играть", label_pos=(85, 635), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (70, 720), (250, 70), on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="создать", label_pos=(85, 735), font_color=(180, 180, 0), font_size=80))
        fonts.append((pg.font.Font(None, 50).render('Мастерская', True, (180, 0, 0)), (310, 0)))

        def main():
            self.running = True
            clock = pg.time.Clock()
            player = None
            while self.running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                        break
                    if event.type == pg.MOUSEBUTTONDOWN:
                        buttons.update(event.pos)
                buttons.update(pg.mouse.get_pos(), True)
                screen.fill('white')
                buttons.draw(screen)
                [screen.blit(*i.get_blit()) for i in buttons]
                [screen.blit(*i) for i in fonts]
                ui.draw(screen)
                pg.display.flip()
                clock.tick(FPS)

        main()
        return self.next_window


class MainGameWindow(Window):
    def __init__(self, map):
        super().__init__()
        self.map = map
        self.next_window = 0
        self.restart = True

    def play_again_button(self):
        self.running = False
        self.restart = True

    def exit_button(self):
        self.running = False

    def start(self):
        ball_image = load_image("ball_2.png")
        box_image = load_image("box_image.png")

        pg.init()
        FPS = 100
        SIZE = self.size
        xs, ys = SIZE
        screen = pg.display.set_mode(SIZE)
        top_border = pg.Rect(0, 0, xs + 1, 1)
        left_border = pg.Rect(0, 0, 1, ys + 1)
        right_border = pg.Rect(xs, 0, 1, ys + 1)
        void_border = pg.Rect(0, ys, xs + 1, 100)
        buttons = pg.sprite.Group()
        fonts = []
        boxes = pg.sprite.Group()
        playerPlatform = pg.sprite.Group()
        self.balls = pg.sprite.Group()
        self.platform = classes.Platform([playerPlatform], (300, 720), (200, 10), image=load_image("background_used.png"), speed=2)
        fonts.append((pg.font.Font(None, 50).render('Чтобы начать, нажмите SPACE', True, (180, 0, 0)), (100, 550)))
        classes.Ball([self.balls], (300, 620), size=(6, 6), image=ball_image)
        def loose():
            fonts.append((pg.font.Font(None, 50).render('Ты проиграл :<', True, (180, 0, 0)), (300, 550)))
            (classes.Button([buttons], (500, 600), (100, 50), on_click=self.play_again_button,
                            image=load_image("background.png"), used_image=load_image("background_used.png"),
                            label="Ещё раз", label_pos=(505, 625), font_color=(180, 180, 0), font_size=30))
            (classes.Button([buttons], (200, 600), (100, 50), on_click=self.exit_button,
                            image=load_image("background.png"), used_image=load_image("background_used.png"),
                            label="Выйти", label_pos=(205, 625), font_color=(180, 180, 0), font_size=30))

        def win():
            fonts.append((pg.font.Font(None, 50).render('Ты выиграл :D', True, (180, 0, 0)), (300, 550)))
            (classes.Button([buttons], (500, 600), (100, 50), on_click=self.play_again_button,
                            image=load_image("background.png"), used_image=load_image("background_used.png"),
                            label="Ещё раз", label_pos=(505, 625), font_color=(180, 180, 0), font_size=30))
            (classes.Button([buttons], (200, 600), (100, 50), on_click=self.exit_button,
                            image=load_image("background.png"), used_image=load_image("background_used.png"),
                            label="Выйти", label_pos=(205, 625), font_color=(180, 180, 0), font_size=30))

        def buff_more_balls():
            chance = random.randint(1, 100)
            if chance <= 10 and len(self.balls) <= 40:
                print(len(self.balls))
                new_balls = pg.sprite.Group()
                for i in self.balls:
                    classes.Ball([new_balls], (i.rect.x - 5, i.rect.y), size=(6, 6), vector=(1, -1), image=balls_image)
                    classes.Ball([new_balls], (i.rect.x + 5, i.rect.y), size=(6, 6), vector=(-1, -1), image=balls_image)
                self.balls.add(*new_balls)
            else:
                rand_vector = random.choice([(0, -1), (1, -1), (-1, -1), (0, -2)])
                classes.Ball([self.balls], (self.platform.rect.x + 75 + random.randint(1, 100), self.platform.rect.y - 50 + random.randint(1, 30)), size=(6, 6), vector=rand_vector, image=balls_image)
        def create_box(x, y):
            classes.Box([boxes], (x, y), size=(10, 10), image=box_image, on_collide=buff_more_balls)

        mapping = classes.Map([], (20, 10), (14, 10), classes.Cursor().get_map(self.map), load_image("brick.png"),
                              on_collide=create_box, box_chance=30)

        def draw():
            screen.fill('white')
            playerPlatform.draw(screen)
            self.balls.draw(screen)
            boxes.draw(screen)
            mapping.draw_all(screen)
            buttons.draw(screen)
            [screen.blit(*i.get_blit()) for i in buttons]
            [screen.blit(*i) for i in fonts]
            pg.display.flip()
        def main(self):
            self.running = True
            wait = None
            self.clock = pg.time.Clock()
            while wait is None:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_SPACE]:
                        wait = 1
                keys = pg.key.get_pressed()
                if keys[pg.K_d]:
                    playerPlatform.update(1)
                elif keys[pg.K_a]:
                    playerPlatform.update(-1)
                else:
                    playerPlatform.update(0)
                pg.display.flip()
                self.clock.tick(FPS)
                draw()
            fonts.clear()
            while self.running:
                start = default_timer()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                        break
                    keys = pg.key.get_pressed()
                    if keys[pg.K_d]:
                        playerPlatform.update(1)
                    elif keys[pg.K_a]:
                        playerPlatform.update(-1)
                    else:
                        playerPlatform.update(0)
                    if event.type == pg.MOUSEBUTTONDOWN:
                        buttons.update(event.pos)
                for ball in self.balls:
                    if ball.rect.colliderect(void_border):
                        ball.kill()
                        continue
                    for platform in playerPlatform:
                        if ball.rect.colliderect(platform.rect):
                            ball.update((1, -1))
                    bricks = mapping.bricks
                    x = 1
                    y = 1
                    for brick in bricks:
                        if ball.rect.colliderect(brick.rect):
                            l, t, w, h = brick.rect.left, brick.rect.top, brick.rect.width, brick.rect.height
                            if ball.rect.colliderect(pg.Rect(l, t, w, 1)) or ball.rect.colliderect(
                                    pg.Rect(l, t + h, w, 1)):
                                y = -1
                            elif ball.rect.colliderect(pg.Rect(l, t, 1, h)) or ball.rect.colliderect(
                                    pg.Rect(l + w, t, 1, h)):
                                x = -1
                            brick.update()
                            mapping.bricks = bricks
                    ball.update((x, y))
                    if ball.rect.colliderect(top_border):
                        ball.update((1, -1))
                    if ball.rect.colliderect(left_border) or ball.rect.colliderect(right_border):
                        ball.update((-1, 1))
                for box in boxes:
                    if box.rect.colliderect(void_border):
                        box.kill()
                    for platform in playerPlatform:
                        box.update(box.rect.colliderect(platform.rect))
                self.balls.update([])
                if len(mapping.bricks) == 0:
                    win()
                elif len(self.balls) == 0:
                    loose()
                buttons.update(pg.mouse.get_pos(), True)
                draw()
                self.clock.tick(FPS)
        while self.restart == True:
            self.restart = False
            xs, ys = SIZE
            screen = pg.display.set_mode(SIZE)
            buttons = pg.sprite.Group()
            fonts = []
            boxes = pg.sprite.Group()
            balls_image = load_image("ball_2.png")
            playerPlatform = pg.sprite.Group()
            self.balls = pg.sprite.Group()
            self.platform = classes.Platform([playerPlatform], (300, 720), (200, 10),
                                             image=load_image("background_used.png"), speed=2)
            fonts.append((pg.font.Font(None, 50).render('Чтобы начать, нажмите SPACE', True, (180, 0, 0)), (100, 550)))
            classes.Ball([self.balls], (300, 620), size=(6, 6), image=balls_image)
            mapping = classes.Map([], (20, 10), (14, 10), classes.Cursor().get_map(self.map), load_image("brick.png"),
                                  on_collide=create_box, box_chance=30)
            main(self)
        return self.next_window


def CreateMapWindow():
    MapMaker.Start()

class SkinsMenu(Window):
    def __init__(self):
        super().__init__()
        self.next_window = -1

    def go_back(self):
        self.running = False
        self.next_window = 0

    def start(self):
        pg.init()
        FPS = 50
        SIZE = self.size
        screen = pg.display.set_mode(SIZE)
        ui = pg.sprite.Group()
        buttons = pg.sprite.Group()
        fonts = []
        (classes.Button([buttons], (550, 110), (200, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="=>", label_pos=(565, 110), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (550, 220), (200, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="=>", label_pos=(565, 220), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (50, 110), (200, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="<=", label_pos=(65, 110), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (50, 220), (200, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="<=", label_pos=(65, 220), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (250, 110), (250, 70), on_click=print,
                        image=load_image("background_used.png"),
                        label="скин", label_pos=(265, 110), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (250, 220), (250, 70), on_click=print,
                        image=load_image("background_used.png"),
                        label="скин", label_pos=(265, 220), font_color=(180, 180, 0), font_size=80))


        (classes.Button([buttons], (550, 720), (200, 70), on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="назад", label_pos=(565, 735), font_color=(180, 180, 0), font_size=80))
        fonts.append((pg.font.Font(None, 50).render('Скины', True, (180, 0, 0)), (310, 0)))
        def main():
            self.running = True
            clock = pg.time.Clock()
            player = None
            while self.running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                        break
                    if event.type == pg.MOUSEBUTTONDOWN:
                        buttons.update(event.pos)
                buttons.update(pg.mouse.get_pos(), True)
                screen.fill('white')
                buttons.draw(screen)
                [screen.blit(*i.get_blit()) for i in buttons]
                [screen.blit(*i) for i in fonts]
                ui.draw(screen)
                pg.display.flip()
                clock.tick(FPS)

        main()
        return self.next_window


class WindowMaster:
    def __init__(self):
        self.level = -1
        self.map = "new_test"

    def start_Window(self, level):
        self.level = level
        print(f"switching to window number {self.level}")
        if self.level is None or self.level == -1:
            return
        if self.level == 0:
            self.level = self.start_MainMenuWindow()
        elif self.level == 1:
            self.level = self.start_CreateMapWindow()
        elif self.level == 2:
            self.level = self.start_LevelsMenuWindow()
        elif self.level == 3:
            self.level, self.map = self.start_CampaignMenuWindow()
            if self.map:
                print(self.map)
                self.level = self.start_MainGameWindow(self.map)
        elif self.level == 4:
            self.level = self.start_SkinsMenu()
        elif self.level == 5:
            self.level = self.start_MainGameWindow(self.map)
        self.start_Window(self.level)

    def start_MainMenuWindow(self):
        return MainMenuWindow().start()

    def start_CreateMapWindow(self, map=None):
        return CreateMapWindow().start()

    def start_MainGameWindow(self, map=None):
        return MainGameWindow(map).start()

    def start_LevelsMenuWindow(self):
        return LevelsMenuWindow().start()  # лвлы, созданные людьми, не нами(там будут появляться созданные карты)

    def start_CampaignMenuWindow(self, max_level=1):
        return CampaignMenuWindow().start()

    def start_SkinsMenu(self):
        return SkinsMenu().start()
