from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.quadrate import Quadrate

import numpy as np

def main():
    rec = Rectangle(3, 3, "синий")
    cir = Circle(3, "зелёный")
    squ = Quadrate(3, "красный")
    print(rec)
    print(cir)
    print(squ)

    print(np.ones((4,4)))


if __name__ == "__main__":
    main()