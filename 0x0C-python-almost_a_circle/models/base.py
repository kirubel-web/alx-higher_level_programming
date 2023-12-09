#!/usr/bin/python3
''' Square class.'''


class Square:
    ''' class Square'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a new square.
        Args:
           size (int): The size of the new square.
        '''
        self.size = size
        self.position = position
