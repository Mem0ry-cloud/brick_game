import pygame
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QInputDialog
import sys
import classes
import os
FPS = 144
SIZE = WIDTH, HEIGHT = 753, 900

def load_image(name, colorkey=None):
    fullname = name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
class MapMaker:
    def __init__(self, width=50, height=50):
        self.width = width
        self.height = height
        self.field = []
        for i in range(height):
            self.field.append([[0, 0] for i in range(width) ])
        #print((self.field[0]))
        self.left = 1
        self.top = 1
        self.cell_size = 15

    def end_pixels(self):
        width_p = self.left + self.width * self.cell_size
        height_p = self.top + self.height * self.cell_size
        return width_p, height_p

    def pixels_to_row_and_column(self, pixel_x, pixel_y):
        row = (pixel_y - self.top) // self.cell_size
        column = (pixel_x - self.left) // self.cell_size
        return row, column

    def render(self, screen):
        width_p, height_p = self.end_pixels()
        for x in range(self.left, width_p, self.cell_size):
            for y in range(self.top, height_p, self.cell_size):
                row, column = self.pixels_to_row_and_column(x, y)
                if self.field[row][column][0] == 0:
                    width = 1
                elif self.field[row][column][0] == 1:
                    width = 2
                elif self.field[row][column][0] == 2:
                    width = 3
                elif self.field[row][column][0] == 3:
                    width = 4
                elif self.field[row][column][0] == 4:
                    width = 5
                elif self.field[row][column][0] == 5:
                    width = 6
                elif self.field[row][column][0] == 6:
                    width = 7
                elif self.field[row][column][0] == 7:
                    width = 8
                elif self.field[row][column][0] == 8:
                    width = 9
                elif self.field[row][column][0] == 9:
                    width = 10
                elif self.field[row][column][0] == 10:
                    width = -1
                elif self.field[row][column][0] == -1:
                    width = 0
                if width == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 2:
                    pygame.draw.rect(screen, (255, 165, 0), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 3:
                    pygame.draw.rect(screen, (255, 255, 0), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 4:
                    pygame.draw.rect(screen, (255, 255, 153), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 5:
                    pygame.draw.rect(screen, (0, 128, 0), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 6:
                    pygame.draw.rect(screen, (8, 189, 255), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 7:
                    pygame.draw.rect(screen, (8, 82, 255), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 8:
                    pygame.draw.rect(screen, (8, 99, 255), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 9:
                    pygame.draw.rect(screen, (0, 0, 255), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == 10:
                    pygame.draw.rect(screen, (102, 11, 186), (x, y, self.cell_size, self.cell_size), width=width)
                elif width == -1:
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size), width=width)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        mx, my = mouse_pos
        width_p, height_p = self.end_pixels()
        if mx <= self.left or mx >= width_p:
            return

        if my <= self.top or my >= height_p:
            return
        #print('кор', self.pixels_to_row_and_column(mx, my))
        return self.pixels_to_row_and_column(mx, my)

    def on_click(self, cell):
        row, column = cell
        value = self.field[row][column][0]
        #print(self.field[row][column])
        if value == 0:
            self.field[row][column][0] = 1
        elif value == 1:
            self.field[row][column][0] = 2
        elif value == 2:
            self.field[row][column][0] = 3
        elif value == 3:
            self.field[row][column][0] = 4
        elif value == 4:
            self.field[row][column][0] = 5
        elif value == 5:
            self.field[row][column][0] = 6
        elif value == 6:
            self.field[row][column][0] = 7
        elif value == 7:
            self.field[row][column][0] = 8
        elif value == 8:
            self.field[row][column][0] = 9
        elif value == 9:
            self.field[row][column][0] = 10
        elif value == 10:
            self.field[row][column][0] = -1
        elif value == -1:
            self.field[row][column][0] = 0
        else:
            raise Exception("В поле хранится не 0 или 1")
        #print(self.field[row][column])
    def save_map(self):
        app = QApplication(sys.argv)
        save = Save_window()
        map_name = save.run()
        map = []
        for i in self.field:
            for j in i:
                map.append(j[0])
        classes.Cursor.add_map(map_name, map)


class Save_window(QWidget):
    def __init__(self):
        super().__init__()

    def run(self):
        name, ok_pressed = QInputDialog.getText(self, "Сохранение карты",
                                                "Введате название карты")
        if ok_pressed and name != '':
            return name
def go_back():
    print("на кнопку нажали!")
def Start():
    pygame.display.set_caption('Клетчатое поле')

    screen = pygame.display.set_mode(SIZE)

    clock = pygame.time.Clock()
    running = True

    field = MapMaker()
    buttons = pygame.sprite.Group()
    (classes.Button([buttons], (550, 720), (200, 70), on_click=go_back,
                    image=load_image("background.png"), used_image=load_image("background_used.png"),
                    label="назад", label_pos=(565, 735), font_color=(180, 180, 0), font_size=80))
    # field.set_view(1, 1, 8)
    while running:
        screen.fill((14, 227, 216))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    field.get_click(event.pos)
                buttons.update(event.pos)
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_LCTRL] and pygame.key.get_pressed()[pygame.K_s]:
                    field.save_map()
        buttons.update(pygame.mouse.get_pos(), True)
        buttons.draw(screen)
        [screen.blit(*i.get_blit()) for i in buttons]
        field.render(screen)
        pygame.display.flip()
        clock.tick(FPS)