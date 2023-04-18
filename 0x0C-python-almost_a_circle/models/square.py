#!/usr/bin/python3
# square.py
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Describes a Square class instance"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a square object

        Args:
            size (int): length of side of square
            x (int): x co-ordinate of square
            y (int): y co-ordinate of square
            id (int): id of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the str() method"""
        id = self.id
        s = self.width
        x = self.x
        y = self.y
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, s))

    @property
    def size(self):
        """gets the size of Square"""
        return self.width

    @size.setter
    def size(self, val):
        """sets the size of the Square"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Updates the attributes of a Square

        *args (ints): new attributes for square object
            - arg1 is the id attribute
            - arg2 is the size attribute
            - arg3 is the x attribute
            - arg4 is the y attribute
        **kwargs (dict): key value pairs of new attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns a dictionary representation of Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
