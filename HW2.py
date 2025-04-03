class Figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_area (self,):
        return 0
    def  info(self):
        print("Figure info not available")
class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
    def calculate_area(self):
        return self.__side_length ** 2
    def info(self):
        print(f'Square side length: {self.__side_length}{self.unit}, area: {self.calculate_area()}{self.unit}.')
class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
    def calculate_area(self,):
        return self.__length * self.__width
    def info(self):
        print(f'Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit},  area: {self.calculate_area()}{self.unit}.')
if __name__ == "__main__":
    figures = [
        Square(9),
        Square(6),
        Rectangle(6, 8),
        Rectangle(9, 3),
        Rectangle(2, 9)
        ]
    for figure in figures:
        figure.info()