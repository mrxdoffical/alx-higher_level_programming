#!/usr/bin/python3
'''module for Square class'''


from models.rectangle import Rectangle

class square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        '''Returns a string representation of square'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

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
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
