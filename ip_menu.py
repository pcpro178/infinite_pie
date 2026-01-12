"""! Module for handling menus."""

################################################################################
# Imports
################################################################################

from typing import List

import inquirer


################################################################################
# Class definitions
################################################################################

class Menu:
    """! Class for handling menus."""

    def __init__(self, choices: List[str] = None, title: str = "Select an option:"):
        """! Initialize a new Menu object.
        :param choices: The menu choices
        :param title: The title to display above the menu
        """
        self.__choices: List[str] = []

        if choices is not None and len(choices) > 0:
            self.__choices.extend(choices)

        self.__response: str = "DefaultResponse"
        self.__title: str = title

    def show(self) -> str | None:
        """! Display the menu and get user selection.
        :return: The choice made by the user
        """
        questions: inquirer.List = [
            inquirer.List(
                'choice', message=self.__title, choices=self.__choices,
            ),
        ]

        self.__response = inquirer.prompt(questions)['choice']

    @property
    def choices(self) -> List[str]:
        """! Accessor for the menu choices.
        :return: The menu choices
        """
        return self.__choices

    @property
    def response(self) -> str | None:
        """! Accessor for the last menu response.
        :return: The last menu response
        """
        return self.__response

    @property
    def title(self) -> str:
        """! Accessor for the menu title.
        :return: The menu title
        """
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        """! Setter for the menu title.
        :param value: The new menu title
        """
        self.__title = value
