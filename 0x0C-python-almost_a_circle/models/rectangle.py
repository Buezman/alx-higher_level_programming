#!/usr/bin/python3
# rectangle.py
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Describes a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a new Rectangle object.

        Args:
            width (int): width of new Rectangle
            height (int): height of new Rectangle
            x (int): x co-ordinate of new Rectangle
            y (int): y co-ordinate of new Rectangle
            id (int): id of new Rectangle from Base class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, val):
        """updates the width of a Rectangle"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, val):
        """updates the height of a Rectangle"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """get x co-ordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """get y co-ordinate of Rectangle"""
        return self.__y

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """calculate the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """prints Rectangle instance with the # character"""

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Overrides the __str__ method"""
        id = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h))

    def update(self, *args, **kwargs):
        """Updates the Rectangle.
        Args:
            *args (ints): New attribute values.
                - argument1 represents id attribute
                - argument2 represents width attribute
                - argument3 represent height attribute
                - argument4 represents x attribute
                - argument5 represents y attribute
            **kwargs (dict): key/value pairs of new attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns a dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
