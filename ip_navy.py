"""! Module for managing empire navy. """

################################################################################
# Imports
################################################################################

from typing import List

from ip_ship import Ship


################################################################################
# Constants & Globals
################################################################################


################################################################################
# Class definitions
################################################################################

class Navy:
    """! Class for managing empire navy. """

    def __init__(self):
        """! Initializes Navy object instance. """
        self.__ships: List[Ship] = None

    @property
    def ships(self) -> List[Ship]:
        """! Getter for ships
        :return: List of ships
        """
        return self.__ships

    @ships.setter
    def ships(self, ships: List[Ship]) -> None:
        """! Setter for ships
        :param ships: List of ships to set
        """
        self.__ships = ships
