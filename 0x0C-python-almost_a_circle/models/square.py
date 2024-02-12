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
