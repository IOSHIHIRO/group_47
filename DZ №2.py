class Figure:
    unit = 'cm'
    def calculate_area(self):
        pass
    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length
    def calculate_area(self):
        return self.__side_length ** 2
    def info(self):
        print(f"Square side length: {self.__side_length}{Figure.unit},"
              f"area: {self.calculate_area()}{Figure.unit}")

class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Rectangle length: {self.__length}{Figure.unit},'
              f'width:{self.__width}{Figure.unit},'
              f'area:{self.calculate_area()}{Figure.unit}')

figures = [
    Square(5),
    Square(3),
    Rectangle(5, 8),
    Rectangle(2, 4),
    Rectangle(10, 6)
]
for figure in figures:
    figure.info()