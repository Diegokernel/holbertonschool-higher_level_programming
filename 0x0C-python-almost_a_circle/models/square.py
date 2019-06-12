#!/usr/bin/python3
'''square class '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class inherits from Rectangle '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        ''' size '''
        return super().width

    @size.setter
    def size(self, value):
        ''' size setter '''
        super(Square, type(self)).width.fset(self, value)
        super(Square, type(self)).height.fset(self, value)

    def update(self, *args, **kwargs):
        ''' update '''
        if len(args) >= 1:
            keys = ['id', 'size', 'x', 'y']
            [setattr(self, keys[arg], args[arg]) for arg in range(len(args))]
        else:
            [setattr(self, key, value) for key, value in kwargs.items()]

    def to_dictionary(self):
        ''' dictionary '''
        return {'id': self.id, 'size': super().width,
                'x': super().x, 'y': super().y}
