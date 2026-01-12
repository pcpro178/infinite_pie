"""! Module for actionable Infinite PIE objects."""

################################################################################
# Imports
################################################################################

from abc import ABC, abstractmethod

import logging

from ip_menu import Menu


################################################################################
# Class definitions
################################################################################

class IActionable(ABC):
    """! Interface class for actionable Infinite PIE objects."""

    def __init__(self, **kwargs) -> None:
        """! Initialize a new Actionable object.
        :param kwargs: Additional parameters to support multiple inheritance
        """
        logger: logging.Logger = logging.getLogger()  # get logging object
        logger.debug(f"Object: {self.__class__.__name__}.{IActionable.__name__} initializing . . .")

        super().__init__()

        self.__menu: Menu = Menu()

    @property
    def menu(self) -> Menu:
        """! Get the menu object.
        :return: The menu object
        """
        return self.__menu

    @abstractmethod
    def run(self) -> None:
        """! Display the menu and handle user selection.
        :return: The choice made by the user
        """
        raise NotImplementedError("Subclasses must implement the 'run' method.")

    def show(self) -> None:
        """! Show the menu to the user."""
        print(f"Object: {self.__class__.__name__}")
        self.menu.show()
