#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) is not 2 or
                type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            [print() for newline in range(self.position[1])]
            for x in range(self.size):
                [print("", end=" ") for spaces in range(self.position[0])]
                for y in range(self.size):
                    print('#', end='')
                print()
