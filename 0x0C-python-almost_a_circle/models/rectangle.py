#!/usr/bin/python3
"""module for Rectangle class"""
from models.Base import Base

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