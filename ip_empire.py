"""! Module for managing empires."""

import os

from cmd import Cmd
from io import StringIO
from typing import List, Type, TypeVar

import inquirer

from ip_name import Name
from ip_ship import Ship
from ip_system import System

T = TypeVar('T')


COL_PADDING: int = 2
MAX_AUTO_LIST: int = 5
MENU_CHOICE_VIEW_DETAILS: str = 'View Details'
MENU_CHOICE_MANAGE_SYSTEMS: str = 'Manage Systems'
MENU_CHOICE_EXIT: str = 'Exit'


class Empire:
    """! Class for managing empires."""

    __name: Name = None
    __ships: List[Ship] = []
    __systems: List[System] = []

    def __init__(self) -> None:
        """! Initializes Empire object instance
        """
        super().__init__()
        print("Setting up new Empire . . .")
        name: str = input("Enter the name of your empire [or use random name generator]: ")
        self.__name = Name("Empire", allow_custom=True, custom=name)

        if self.__name == "":
            self.__name = Name(self.__class__.__name__)

        # Create initial systems
        self.__create_members(System, self.__systems)

        # Create initial ships
        self.__create_members(Ship, self.__ships)

        print(f"Empire {self.__name} created.")

    def __str__(self) -> str:
        """! Override function to generate object as human readable string
        :return: String representation of object
        """
        s: str = f"Empire: {self.__name}\r\n"
        s += self.__members_list_to_string(System, self.__systems)
        s += self.__members_list_to_string(Ship, self.__ships)
        return s

    def __create_members(self, typeof: Type[T], listof: list) -> None:
        """! Instaniates lists of object members
        :param typeof: Member list type
        :param listof: Member list
        """
        num_create_str: str = None
        type_name: str = typeof.__name__.lower()
        while num_create_str is None or num_create_str == 0 or not num_create_str.isdigit():
            num_create_str = input(f"Enter the starting number of {type_name}s: ")
        num_create_int: int = int(num_create_str)
        print(f"{type_name[0].upper() + type_name[1:]}{'s' if 1 < num_create_int else ''} created:", end='')
        for i in range(num_create_int):
            obj: object = typeof()
            listof.append(obj)
            print(f"{',' if 0 < i else ''} {obj.name()}", end='')
        listof.sort()
        print()

    def __members_list_to_string(self, typeof: Type[T], listof: list) -> str:
        """! Converts specified member list to string
        :param typeof: Member list type
        :param listof: Member list
        :return: String representation of member list
        """
        display_columns: int = os.get_terminal_size().columns
        type_name: str = typeof.__name__.lower()
        s: str = f"Number of {type_name[0].upper() + type_name[1:]}s: {len(listof)}\r\n"
        names_buffer: StringIO = StringIO()
        Cmd(stdout=names_buffer).columnize([x.name() for x in listof], displaywidth=display_columns)
        for line in names_buffer.getvalue().splitlines():
            s += "  " + line + "\r\n"
        return s

    # todo jfell cleanup
    # def cycle(self) -> None:
    #     """Complete a temporal cycle (i.e. a player turn, as it were)."""
    #     self.menu()

    def menu(self) -> str | None:
        """! Display the empire menu.
        :return: The choice made by the user
        """
        questions: inquirer.List = [
            inquirer.List(
                'choice',
                message="Empire Menu",
                choices=[
                    MENU_CHOICE_VIEW_DETAILS,
                    MENU_CHOICE_MANAGE_SYSTEMS,
                    MENU_CHOICE_EXIT
                ],
            ),
        ]

        answers: dict = inquirer.prompt(questions)

        if answers['choice'] == MENU_CHOICE_VIEW_DETAILS:
            print(str(self))
        elif answers['choice'] == MENU_CHOICE_MANAGE_SYSTEMS:
            print("System management not yet implemented.")
        elif answers['choice'] == MENU_CHOICE_EXIT:
            print("Exiting . . .")
        else:
            print("Invalid choice.")

        return answers['choice']
