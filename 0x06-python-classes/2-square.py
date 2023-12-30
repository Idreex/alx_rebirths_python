#!/usr/bin/python3
class validat(Exception):
    def validate(self, size):
        if size < 0:
            raise ValueError()
        return size


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value

    
    
my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)




# size must be an integer
# size must be >= 0