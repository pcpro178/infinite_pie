"""! Module for managing object locations in space."""

################################################################################
# Imports
################################################################################

from typing import Tuple

import logging


################################################################################
# Class definitions
################################################################################

class Coordinates:
    """! Class for handling coordinates in space."""

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        """! Initialize a new Coordinates object.
        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        """
        self.__x: int = x
        self.__y: int = y
        self.__z: int = z

    @property
    def x(self) -> int:
        """! Accessor for the X coordinate.
        :return: The X coordinate
        """
        return self.__x

    @property
    def y(self) -> int:
        """! Accessor for the Y coordinate.
        :return: The Y coordinate
        """
        return self.__y

    @property
    def z(self) -> int:
        """! Accessor for the Z coordinate.
        :return: The Z coordinate
        """
        return self.__z


class ILocatable:
    """! Interface class for handling object locations in space."""

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        """! Initialize a new Location object.
        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        """
        logger: logging.Logger = logging.getLogger()  # get logging object
        logger.debug(f"Object: {self.__class__.__name__}.{ILocatable.__name__} initializing . . .")

        self.__coordinates: Coordinates = Coordinates(x, y, z)

    @property
    def coordinates(self) -> Tuple[int, int, int]:
        """! Accessor for the coordinates as a tuple.
        :return: The coordinates as a tuple (x, y, z)
        """
        return (self.__coordinates.x, self.__coordinates.y, self.__coordinates.z)

    @coordinates.setter
    def coordinates(self, coords: Tuple[int, int, int]) -> None:
        """! Setter for the coordinates.
        :param coords: The coordinates as a tuple (x, y, z)
        """
        self.__coordinates = Coordinates(coords[0], coords[1], coords[2])

    def distance(self, other: Coordinates) -> float:
        """! Calculate the Euclidean distance to another Coordinates object.
        :param other: The other Coordinates object
        :return: The Euclidean distance
        """
        return ((self.__coordinates.x - other.x) ** 2 +
                (self.__coordinates.y - other.y) ** 2 +
                (self.__coordinates.z - other.z) ** 2) ** 0.5
