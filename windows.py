import classes
import os
import sys
import pygame as pg


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
    def __init__(self, size=(800, 800)):
        self.size = size
        self.ui = pg.sprite.Group()

    def start(self):
        return -1


class MainMenuWindow(Window):
    def __init__(self):
        super().__init__()
        self.next_window = 1

    def on_click_1(self):
        self.next_window = -1
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
        (classes.Button([buttons], (300, 100), (300, 100), 0, on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="Играть", label_pos=(310, 120), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (300, 250), (300, 100), 0, on_click=self.on_click_2,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="Кампания", label_pos=(310, 270), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (300, 400), (350, 100), 0, on_click=self.on_click_3,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="Мастерская", label_pos=(310, 420), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (300, 550), (350, 100), 0, on_click=self.on_click_4,
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
        self.next_window = 1

    def on_click_1(self):
        self.next_window = -1
        self.running = False

    def on_click_2(self):
        self.next_window = 3
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
        (classes.Button([buttons], (100, 100), (70, 70), 0, on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="1", label_pos=(115, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (200, 100), (70, 70), 0, on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="2", label_pos=(215, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (300, 100), (70, 70), 0, on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="3", label_pos=(315, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (400, 100), (70, 70), 0, on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="4", label_pos=(415, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (500, 100), (70, 70), 0, on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="5", label_pos=(515, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (600, 100), (70, 70), 0, on_click=self.on_click_1,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="6", label_pos=(615, 115), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (550, 720), (200, 70), 0, on_click=self.go_back,
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
        return self.next_window


class LevelsMenuWindow(Window):
    def __init__(self):
        super().__init__()
        self.next_window = 1

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
        (classes.Button([buttons], (550, 720), (200, 70), 0, on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="назад", label_pos=(565, 735), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (470, 620), (250, 70), 0, on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="рандом", label_pos=(485, 635), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (70, 620), (250, 70), 0, on_click=self.go_back,
                        image=load_image("background.png"), used_image=load_image("background_used.png"),
                        label="играть", label_pos=(85, 635), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (70, 720), (250, 70), 0, on_click=self.on_click_1(),
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
    pass


class CreateMapWindow(Window):
    pass


class SkinsMenu(Window):
    def __init__(self):
        super().__init__()
        self.next_window = 1

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
        (classes.Button([buttons], (550, 720), (200, 70), 0, on_click=self.go_back,
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
            self.level = self.start_CampaignMenuWindow()
        elif self.level == 4:
            self.level = self.start_SkinsMenu()
        self.start_Window(self.level)

    def start_MainMenuWindow(self):
        return MainMenuWindow().start()

    def start_CreateMapWindow(self, map=None):
        return CreateMapWindow().start()

    def start_MainGameWindow(self, map=None):
        return MainGameWindow().start()

    def start_LevelsMenuWindow(self):
        return LevelsMenuWindow().start()  # лвлы, созданные людьми, не нами(там будут появляться созданные карты)

    def start_CampaignMenuWindow(self, max_level=1):
        return CampaignMenuWindow().start()

    def start_SkinsMenu(self):
        return SkinsMenu().start()
