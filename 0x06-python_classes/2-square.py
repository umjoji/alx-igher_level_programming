#!/usr/bin/python3
class Square:
    """
    A class that defines a square by
    the private attribute size
    """
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
                raise TypeError("size must be an integer")
        elif size < 0:
                raise ValueError("size must be >= 0")
        self.__size = size
