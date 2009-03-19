# -*- coding: utf-8 -*-

"""
Record class.
Usage:

p = Record(x=10, y=11, color='blue')
print p.x
print p.color

"""


class Record(dict):
    """
    Object with record-like properties
    """
    def __init__(self, *args, **kw):
        super (Record, self).__init__ (*args, **kw)
        self.__dict__.update(*args, **kw)

    def update (self, *args, **kw):
        super (Record, self).update (*args, **kw)
        self.__dict__.update(*args, **kw)
