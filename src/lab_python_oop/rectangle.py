from lab_python_oop.geometrical_figure import GeometricalFigure
from lab_python_oop.f_color import FigurColor


class Rectangle(GeometricalFigure):

    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigurColor()
        self.color.colorproperty = color
    
    def get_type(self):
        return self.FIGURE_TYPE
    
    def get_square(self):
        return self.width*self.height
    
    def __repr__(self):
        return '{}, цвет - {},  ширина = {}, высота = {}, площадь = {}.'.format(
        self.get_type(),
        self.color.colorproperty,
        self.width,
        self.height,
        self.get_square()
    )