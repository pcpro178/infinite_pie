"""! Module for handling gameplay."""

################################################################################
# Imports
################################################################################

from enum import StrEnum

import inquirer

from ip_empire import Empire

import ip_empire as empire


################################################################################
# Class definitions
################################################################################

class MenuChoices(StrEnum):
    """! Enumeration for main menu choices."""
    NEW_EMPIRE: str = 'New Empire'
    MANAGE_EMPIRE: str = 'Manage Empire'
    END_TURN: str = 'End Turn'
    EXIT: str = 'Exit'


class Play:
    """! Class for handling gameplay."""

    __empire: Empire = None

    def __init__(self):
        """! Initialize a new Play object."""
        pass

    def menu(self) -> str | None:
        """! Display the main gameplay menu.
        :return: The choice made by the user
        """
        questions: inquirer.List = [
            inquirer.List(
                'choice', message="Infinite PIE Menu", choices=[str(x) for x in MenuChoices],
            ),
        ]

        answers: dict = inquirer.prompt(questions)

        if answers['choice'] == MenuChoices.NEW_EMPIRE:
            if self.__empire is not None:
                confirm: str = input("An empire already exists. Creating a new empire will overwrite the existing one. Continue? (y/n): ")
                if confirm[0].lower() == 'y':
                    self.__empire = Empire()
            else:
                self.__empire = Empire()
        elif answers['choice'] == MenuChoices.MANAGE_EMPIRE:
            if self.__empire is None:
                print("No empire created. Create a new empire to begin.")
            else:
                while self.__empire.menu() != empire.MenuChoices.EXIT:
                    pass
        elif answers['choice'] == MenuChoices.END_TURN:
            if self.__empire is None:
                print("No empire created. Create a new empire to begin.")
            else:
                self.__empire.cycle()
        elif answers['choice'] == MenuChoices.EXIT:
            print("Exiting . . .")
        else:
            print("Invalid choice.")

        return answers['choice']
