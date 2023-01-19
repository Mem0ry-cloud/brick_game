import pygame as pg

pg.init()
FPS = 50
SIZE = WIDTH, HEIGHT = 800, 800

pg.init()
screen = pg.display.set_mode(SIZE)
all_sprites = pg.sprite.Group()
players = pg.sprite.Group()
platforms = pg.sprite.Group()


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, players)
        self.image = pg.Surface((20, 20))
        self.image.fill("lightblue")
        self.rect = pg.Rect(x, y, 20, 20)

    def update(self, *keys):
        if not pg.sprite.spritecollideany(self, platforms):
            self.rect = self.rect.move(0, 1)
            return

        if keys:
            keys = keys[0]
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.rect = self.rect.move(-1, 0)
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.rect = self.rect.move(1, 0)

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, platforms)
        self.image = pg.Surface((50, 10))
        self.image.fill("gray")
        self.rect = pg.Rect(x, y, 50, 10)

f1 = pg.font.Font(None, 36)
text1 = f1.render('Hello Привет', True, (180, 0, 0))
pg.display.update()
def main():
    running = True
    clock = pg.time.Clock()

    player = None
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    if not player:
                        player = Player(*event.pos)
                    else:
                        player.rect.x, player.rect.y = event.pos
                if event.button == 1:
                    Platform(*event.pos)
        screen.fill('white')
        all_sprites.draw(screen)
        screen.blit(text1, (10, 50))
        keys = pg.key.get_pressed()
        all_sprites.update(keys)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
    pg.quit()