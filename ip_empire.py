"""Module for managing empires."""

from typing import List

import inquirer

from ip_name import Name
from ip_options import Options
from ip_ship import Ship
from ip_system import System


MAX_AUTO_LIST: int = 5


class Empire(Options):
    """Class for managing empires."""

    __name: Name = None
    __ships: List[Ship] = []
    __systems: List[System] = []

    __questions = [
        inquirer.List(
            'choice',
            message=f"Empire Menu",
            choices=[
                'View Empire Details',
                'Manage Systems',
                'Exit Menu'
            ],
        ),
    ]

    def __init__(self):
        super().__init__()
        print("Setting up new Empire . . .")
        name: str = input("Enter the name of your empire [or use random name generator]: ")
        self.__name = Name("Empire", allow_custom=True, custom=name)

        if self.__name == "":
            self.__name = Name(self.__class__.__name__)

        # Create initial systems
        num_systems: str = None
        while num_systems is None or num_systems == 0 or not num_systems.isdigit():
            num_systems = input("Enter the starting number of systems: ")
        for i in range(int(num_systems)):
            self.__systems.append(System())

        # Create initial ships
        num_ships: str = None
        while num_ships is None or num_ships == 0 or not num_ships.isdigit():
            num_ships = input("Enter the starting number of ships: ")
        for i in range(int(num_ships)):
            self.__ships.append(Ship())

        print(f"Empire {self.__name} created.")

    def __str__(self) -> str:
        s: str = f"Empire: {self.__name}\r\n"
        s += f"Number of Systems: {len(self.__systems)}\r\n"
        if (MAX_AUTO_LIST >= len(self.__systems)) or ('y' == input(f"Show all? [Yes/No] ")[0].lower()):
            for system in self.__systems:
                s += f" - {system}\r\n";
        s += f"Number of Ships: {len(self.__ships)}\r\n"
        if (MAX_AUTO_LIST >= len(self.__ships)) or ('y' == input("Show all? [Yes/No] ")[0].lower()):
            for ship in self.__ships:
                s += f" - {ship}\r\n"
        return s

    def cycle(self):
        """Complete a temporal cycle (i.e. a player turn, as it were)."""
        self.menu()

    def menu(self):
        """Display the empire menu."""
        answers = inquirer.prompt(self.__questions)

        if answers['choice'] == 'View Empire Details':
            print(str(self))
        elif answers['choice'] == 'Manage Systems':
            print("System management not yet implemented.")

        return answers['choice']
