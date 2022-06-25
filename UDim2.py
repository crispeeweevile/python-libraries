import pygame

    
class UDim2(tuple):
    """UDim2 is a class made for Pygame in order to help you with replacing all those pesky tuples that you use for positions and sizes.
    UDim2 uses your pygame display resolution and some simple math to allow to easily position your objects based off the screen size, or
    you can just use offset!"""

    def verify_pygame_loaded():
        """Used to prevent the user from using the class before setting up Pygame. This is important because we use a special pygame function to handle the Scale value"""
        if not pygame.get_init(): raise Exception("Pygame must be initialized before UDim2 can be used!")
        if not pygame.display.get_active(): raise Exception("There must be an initialized display before UDim2 can be used!")

    def __init__(self, scale_x: float, offset_x: int, scale_y: float, offset_y: int) -> None:
        """Creates a new UDim2 object. scale values are floats that represent a percentage of the display resolution, offset values are integers that represent an exact number of pixels to move something by"""
        UDim2.verify_pygame_loaded()
        self.Scale = [scale_x, scale_y]
        self.Offset = [offset_x, offset_y]

    @classmethod
    def from_scale(cls, scale_x: float, scale_y: float) -> object:
        """Creates a new UDim2 object using only the scale value, offset will default to 0"""
        UDim2.verify_pygame_loaded()
        res=pygame.display.get_window_size()
        return cls(scale_x, 0, scale_y, 0)

    @classmethod
    def from_offset(cls, offset_x: int, offset_y: int) -> object:
        """Creates a new UDim2 object using only the offset value, scale will default to 0"""
        UDim2.verify_pygame_loaded()
        res=pygame.display.get_window_size()
        return cls(0, offset_x, 0, offset_y)

    def calculate(self) -> list:
        """Calculates the exact pixel count for x and y"""
        UDim2.verify_pygame_loaded()
        return [(self.Scale[0]*self.res[0])+self.Offset[0], (self.Scale[1]*self.res[1])+self.Offset[1]]

    def __new__(cls, sx,ox,sy,oy):
        """Uhhh, I'm not really sure, but it gives us compatability for Pygame... (Essentially makes the class act like a tuple?)"""
        UDim2.verify_pygame_loaded()
        res=pygame.display.get_window_size()
        return super(UDim2, cls).__new__(cls, ((sx*res[0])+ox, (sy*res[1])+oy))
