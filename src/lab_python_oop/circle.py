from lab_python_oop.geometrical_figure import GeometricalFigure
from lab_python_oop.f_color import FigurColor
from math import pi

class Circle(GeometricalFigure):

    FIGURE_TYPE = "Круг"

    @classmethod
    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigurColor()
        self.color.colorproperty = color

    def get_type(self):
        return self.FIGURE_TYPE
    
    def get_square(self):
        return pi*self.radius*self.radius
    
    def __repr__(self):
        return '{}, цвет - {},  радиус = {}, площадь = {}.'.format(
        self.get_type(),
        self.color.colorproperty,
        self.radius,
        self.get_square()
    )