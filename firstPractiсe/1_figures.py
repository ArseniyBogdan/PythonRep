import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(Shape):
    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new):
        self.__width = new

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new):
        self.__height = new


class Square(Rectangle):
    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new):
        self.__width = new
        self.__height = new

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new):
        self.__height = new
        self.__width = new


def client_code(rect):
    rect.height = 10
    rect.width = 40
    print("width =", rect.width, "; height =", rect.height)
    rect.width = 30
    rect.height = 15
    print("width =", rect.width, "; height =", rect.height)


print("Square")
rect1 = Square(10)
client_code(rect1)


print("Rectangle")
rect2 = Rectangle(10, 10)
client_code(rect2)
