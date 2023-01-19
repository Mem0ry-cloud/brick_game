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


class Label:
    def __init__(self, position, size, color, text):
        self.position = position
        self.size = size
        self.color = color
        self.text = text
        pass


class Button:
    def __init__(self, position, size, color, on_click, label=None):
        self.position = position
        self.size = size
        self.color = color
        self.label = label
        self.on_click = on_click


class GameObject:
    pass


class Brick(GameObject):
    pass


class Ball(GameObject):
    pass


class Platform(GameObject):
    pass
