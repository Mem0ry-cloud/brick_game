import classes
import pygame as pg
class Window:
    def __init__(self, size=classes.Size(800, 800)):
        self.size = size
        self.ui = pg.sprite.Group()

class MainMenuWindow(Window):
    def __init__(self):
        super().__init__()

    def start(self):
        pg.init()
        FPS = 50
        SIZE = self.size.width, self.size.height
        screen = pg.display.set_mode(SIZE)
        ui = pg.sprite.Group()
        buttons = pg.sprite.Group()
        #classes.Button(classes.Position(0, 0), classes.Size(20, 20), )
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

        main()


class CampaignMenuWindow(Window):
    pass


class LevelsMenuWindow(Window):
    pass


class MainGameWindow(Window):
    pass


class CreateMapWindow(Window):
    pass


class WindowMaster:
    def __init__(self):
        pass

    def start_MainMenuWindow(self):
        pass

    def start_CreateMapWindow(self, map=None):
        pass

    def start_MainGameWindow(self, map=None):
        pass

    def start_LevelsMenuWindow(self):
        pass

    def start_CampaignMenuWindow(self, max_level=1):
        pass