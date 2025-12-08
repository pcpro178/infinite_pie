"""Module for base ship type."""

import ip_name


class Ship:
    """Class for base ship type."""

    __name: ip_name.Name = None

    def __init__(self):
        """! Initialize a new Ship."""
        self.__name = ip_name.Name(self.__class__.__name__)
        print(f"Ship {self.__name} created.")

    def __str__(self) -> str:
        """! String representation of the Ship."""
        return f"Ship: {self.__name}"
