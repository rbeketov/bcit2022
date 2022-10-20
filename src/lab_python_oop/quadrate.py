from lab_python_oop.rectangle import Rectangle
from lab_python_oop.f_color import FigurColor

class Quadrate(Rectangle):
     
    FIGURE_TYPE = "Квадрат"
     
    @classmethod
    def __init__(self,  side, color):
        self.side = side
        super().__init__(self.side, self.side, color)
    
    def get_type(self):
        return self.FIGURE_TYPE

    def __repr__(self):
        return '{}, цвет - {}, сторона = {}, площадь = {}.'.format(
            self.get_type(),
            self.color.colorproperty,
            self.side,
            self.get_square()
        )