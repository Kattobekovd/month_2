class Figure:
    unit = 'cm' #Атрибут уровня класса

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, __side_length):
        super().__init__()
        self.__side_length = __side_length

    def calculate_area(self):
        return (self.__side_length * self.__side_length)

    def info(self):
        return (f'Square side length:{self.__side_length}{Figure.unit},'
                f'area:{self.__side_length*self.__side_length}')

class Rectangle(Figure):
    def __init__(self, __length , __widht):
        super().__init__()
        self.__length = __length
        self.__width = __widht

    def calculate_area(self):
        return self.__width * self.__length

    def info(self):
        return (f'Rectangle lenght:{self.__length}{Figure.unit},'
                f'width:{self.__width}{Figure.unit}, '
                f'area:{self.calculate_area()}{Figure.unit}^2')

shapes = [Square(4),
          Square(8),
          Rectangle(5,9),
          Rectangle(3,8),
          Rectangle(4,7)]

for shape in shapes:
    print(shape.info())











