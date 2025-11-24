"""Module for managing empires."""

from typing import List

import ip_name
import ip_system

class Empire:
    """Class for managing empires."""

    __name: ip_name.Name = None
    __num_systems: int = None
    __systems: List[ip_system.System] = []

    def __init__(self):
        print("Setting up new Empire . . .")
        self.__name = input("Enter the name of your empire [or use random name generator]: ")

        if self.__name == "":
            self.__name = ip_name.Name(self.__class__.__name__)

        num_systems: str = None
        while num_systems is None or num_systems == 0 or not num_systems.isdigit():
            num_systems = input("Enter the number of systems in your empire: ")
        self.__num_systems = int(num_systems)

        for i in range(self.__num_systems):
            self.__systems.append(ip_system.System())

        print(f"Empire {self.__name} created.")

    def name_get(self):
        """Get the current empire name."""
        return self.__name

    def name_set(self, name):
        """Set a new empire name."""
        self.__name = name
