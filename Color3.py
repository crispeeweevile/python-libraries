import pygame



class Color3(tuple):
    colors_by_name = {
        "BLACK": (0, 0, 0),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "WHITE": (255, 255, 255),
        "PINK": (255, 0, 255),
        "YELLOW": (255, 255, 0),
        "TEAL": (0, 255, 255),
        "PURPLE": (255, 0, 255),
    }

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def from_tuple(cls, color_tuple: tuple | list):
        return cls(color_tuple[0], color_tuple[1], color_tuple[2])

    @classmethod
    def from_color_name(cls, color_name: str):
        color_tuple = Color3.colors_by_name[color_name.upper()]
        return cls.from_tuple(color_tuple)

    def __new__ (cls, r, g, b):
        return super(Color3, cls).__new__(cls, (r, g, b))
    