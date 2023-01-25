import classes
import pygame as pg


class Window:
    def __init__(self, size=(800, 800)):
        self.size = size
        self.ui = pg.sprite.Group()

    def start(self):
        return -1


class MainMenuWindow(Window):
    def __init__(self):
        super().__init__()

    def start(self):
        pg.init()
        FPS = 50
        SIZE = self.size
        screen = pg.display.set_mode(SIZE)
        ui = pg.sprite.Group()
        buttons = pg.sprite.Group()
        fonts = []
        (classes.Button([buttons], (200, 70), 0, 0, 0, label="Играть", label_pos=(310, 100), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (200, 70), 0, 0, 0, label="Кампания", label_pos=(310, 250), font_color=(180, 180, 0), font_size=80))
        (classes.Button([buttons], (200, 70), 0, 0, 0, label="Мастерская", label_pos=(310, 400), font_color=(180, 180, 0), font_size=80))
        fonts.append((pg.font.Font(None, 50).render('Стонес Гаме', True, (180, 0, 0)), (310, 0)))
        fonts.append((pg.font.Font(None, 50).render('Сделано с божьей помощью', True, (90, 0, 0)), (200, 700)))
        def main():
            running = True
            clock = pg.time.Clock()

            player = None
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                        break
                screen.fill('white')
                [screen.blit(*i.get_blit()) for i in buttons]
                [screen.blit(*i) for i in fonts]
                ui.draw(screen)
                pg.display.flip()
                clock.tick(FPS)
        main()
        return 1


class CampaignMenuWindow(Window):
    def __init__(self):
        super().__init__()

    def start(self):
        pg.init()
        FPS = 50
        SIZE = self.size.width, self.size.height
        screen = pg.display.set_mode(SIZE)
        ui = pg.sprite.Group()
        buttons = pg.sprite.Group()
        # classes.Button(classes.Position(0, 0), classes.Size(20, 20), )
        fonts = []
        fonts.append((pg.font.Font(None, 36).render('Stones Game', True, (180, 0, 0)), (310, 50)))
        fonts.append((pg.font.Font(None, 36).render('Made by me', True, (90, 0, 0)), (355, 700)))

        def main():
            running = True
            clock = pg.time.Clock()

            player = None
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                        break
                screen.fill('white')
                [screen.blit(*i) for i in fonts]
                ui.draw(screen)
                pg.display.flip()
                clock.tick(FPS)
            return -1

        main()


class LevelsMenuWindow(Window):
    pass


class MainGameWindow(Window):
    pass


class CreateMapWindow(Window):
    pass


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
            self.level =self.start_LevelsMenuWindow()
        elif self.level == 3:
            self.level = self.start_CampaignMenuWindow()
        self.start_Window(self.level)

    def start_MainMenuWindow(self):
        return MainMenuWindow().start()

    def start_CreateMapWindow(self, map=None):
        return CreateMapWindow().start()

    def start_MainGameWindow(self, map=None):
        return MainGameWindow().start()

    def start_LevelsMenuWindow(self):
        return LevelsMenuWindow().start()

    def start_CampaignMenuWindow(self, max_level=1):
        return CampaignMenuWindow().start()