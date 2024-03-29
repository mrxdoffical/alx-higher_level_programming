#!/usr/bin/python3
"""module for Rectangle class"""
from models.base import Base

class Rectangle(Base):
    '''a Rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''x position of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''x position of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def validate_intger(self, name, value, eq=True):
        '''method for validation'''
        if type(value) is not int:
            raise ValueError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''computes area of this rectangle'''
        return self.width * self.height

    def display(self):
        '''print string representation'''
        s = '\n' * self.y + \
            (' ' * self.x + self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''returns a string representation of rectangle'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, x=None, y=None, width=None, height=None):
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update instance with no-keyword & keyword arguments'''
        #print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''return a dictionary representation of this class'''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
