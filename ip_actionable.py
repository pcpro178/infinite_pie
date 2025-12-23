"""! Module for actionable Infinite PIE objects."""

################################################################################
# Imports
################################################################################

from abc import ABC, abstractmethod
from typing import List

from ip_menu import Menu


################################################################################
# Class definitions
################################################################################

class Actionable(ABC):
    """! Class for actionable Infinite PIE objects."""

    __menu: Menu = None  # Menu for the actionable object

    def __init__(self, choices: List[str], title: str = "Select an option:") -> None:
        """! Initialize a new Actionable object.
        :param choices: Menu choices
        :param title: Title to display above the menu
        """
        super().__init__()
        self.__menu = Menu(choices, title)

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

    @abstractmethod
    def show(self) -> None:
        """! Show the menu to the user."""
        raise NotImplementedError("Subclasses must implement the 'show' method.")
