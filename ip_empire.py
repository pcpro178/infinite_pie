"""Module for managing empires."""

from typing import List

import inquirer
import ip_name
import ip_system


class Empire:
    """Class for managing empires."""

    __name: ip_name.Name = None
    __num_systems: int = None
    __systems: List[ip_system.System] = []

    def __init__(self):
        print("Setting up new Empire . . .")
        name: str = input("Enter the name of your empire [or use random name generator]: ")
        self.__name = ip_name.Name("Empire", allow_custom=True, custom=name)

        if self.__name == "":
            self.__name = ip_name.Name(self.__class__.__name__)

        num_systems: str = None
        while num_systems is None or num_systems == 0 or not num_systems.isdigit():
            num_systems = input("Enter the number of systems in your empire: ")
        self.__num_systems = int(num_systems)

        for i in range(self.__num_systems):
            self.__systems.append(ip_system.System())

        print(f"Empire {self.__name} created.")

        self.menu()

    def menu(self):
        """Display the empire menu."""
        questions = [
            inquirer.List(
                'choice',
                message=f"Empire Menu - {self.__name}",
                choices=[
                    'View Empire Details',
                    'Manage Systems',
                    'Exit Menu'
                ],
            ),
        ]
        answers = inquirer.prompt(questions)
        return answers['choice']
