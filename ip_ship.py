"""! Module for base ship type."""

################################################################################
# Imports
################################################################################

from __future__ import annotations

import logging

from ip_locatable import ILocatable
from ip_name import Name


################################################################################
# Constants & Globals
################################################################################

DEFAULT_SPEED: int = 100


################################################################################
# Class definitions
################################################################################

class Ship(ILocatable):
    """!Class for base ship type."""

    def __init__(self, base: str):
        """! Initialize a new Ship."""
        logger: logging.Logger = logging.getLogger()  # get logging object
        logger.debug(f"Object: {self.__class__.__name__} initializing . . .")

        super().__init__()

        self.__base: str = base
        self.__destination: str | None = None
        self.__name: Name = Name("Ship")
        self.__speed: int = DEFAULT_SPEED

    def __eq__(self, obj: Ship) -> bool:
        """! Override equality comparison (==) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name == obj.__name.name

    def __gt__(self, obj: Ship) -> bool:
        """! Override greater-than (>) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name > obj.__name.name

    def __lt__(self, obj: Ship) -> bool:
        """! Override less-than (<) operator
        :param obj: Object to be compared against
        :return: True or false depending on comparison
        """
        if type(obj) is not Ship:
            raise ValueError(f"Param 'obj' (type={type(obj)}) must be of type {type(self)}")
        return self.__name.name < obj.__name.name

    def __repr__(self) -> str:
        """! String representation of the Ship object for program usage
        :return: String representation of the Ship object
        """
        return f"{self.__name}: {self.__base} -> {self.__destination or 'In Transit or Idle'}"

    def __str__(self) -> str:
        """! String representation of the Ship object for user display
        :return: String representation of the Ship
        """
        return f"{self.__name}"

    @property
    def base(self) -> str:
        """! Accessor function for base attribute.
        :return: The base attribute
        """
        return self.__base

    @property
    def destination(self) -> str | None:
        """! Accessor function for destination attribute.
        :return: The destination attribute
        """
        return self.__destination

    @destination.setter
    def destination(self, value: str | None) -> None:
        """! Mutator function for destination attribute.
        :param value: The new value for the destination attribute
        """
        self.__destination = value

    @property
    def name(self) -> str:
        """! Accessor function for name attribute.
        :return: The name attribute
        """
        return self.__name.name

    @name.setter
    def name(self, value: str) -> None:
        """! Mutator function for name attribute.
        :param value: The new value for the name attribute
        """
        self.__name.name = value

    @property
    def speed(self) -> int:
        """! Accessor function for speed attribute.
        :return: The speed attribute
        """
        return self.__speed

    @speed.setter
    def speed(self, value: int) -> None:
        """! Mutator function for speed attribute.
        :param value: The new value for the speed attribute
        """
        self.__speed = value
