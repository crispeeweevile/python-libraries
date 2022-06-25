class Color3(tuple):
    """A very small Color3 library intended for use with Pygame. Uses 0-255 scale and supports making Color3(s) from tuples or just using some of the pre-made colors"""
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

    def __init__(self, r: int, g: int, b: int) -> None:
        """Base constructor for making a new Color3"""
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def from_tuple(cls, color_tuple: tuple | list) -> object:
        """Converts a tuple or list into a Color3 where index 0 is r, 1 is g, and 2 is blue"""
        return cls(color_tuple[0], color_tuple[1], color_tuple[2])

    @classmethod
    def from_color_name(cls, color_name: str) -> object:
        """Converts a string color name into a Color3 (LIMITED SELECTION)"""
        color_tuple = Color3.colors_by_name[color_name.upper()]
        return cls.from_tuple(color_tuple)

    def __new__ (cls, r, g, b):
        """I still don't really know..."""
        return super(Color3, cls).__new__(cls, (r, g, b))
    
