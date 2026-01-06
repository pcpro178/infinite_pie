"""! Module for managing empire territory. """

################################################################################
# Imports
################################################################################

from typing import List

from ip_system import System


################################################################################
# Constants & Globals
################################################################################


################################################################################
# Class definitions
################################################################################

class Territory:
    """! Class for managing empire territory. """

    def __init__(self):
        """! Initializes Territory object instance. """
        self.__systems: List[System] = None

    @property
    def systems(self) -> List[System]:
        """! Getter for systems
        :return: List of systems
        """
        return self.__systems

    @systems.setter
    def systems(self, value: List[System]) -> None:
        """! Setter for systems
        :param value: List of systems
        """
        self.__systems = value
