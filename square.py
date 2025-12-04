from Lab_2.rectangle import Rectangle

class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    @property
    def name(self):
        return self.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            self.name,
            self.color.color,
            self.width,
            self.area()
        )
