class Rectangle:
    # Constructor
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    # Defining instance methods
    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)