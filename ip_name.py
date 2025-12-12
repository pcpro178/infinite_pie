"""Module for handling names."""

from typing import List

import ip_lexicon as lexicon

class Name:
    """Class for handling names."""

    __label: str = "DefaultLabel"
    __name: str = "DefaultName"

    def __init__(self, label: str, allow_custom: bool = False, custom: str = "") -> None:
        """! Initialize a new name object.
        :param label: The label for the name (e.g., "Empire", "System").
        :param allow_custom: Whether to allow custom name input.
        :param custom: The custom name to assign, if any.
        """
        if label is not None and label != "":
            self.__label = label

        if allow_custom:
            if custom is not None and custom != "":
                if lexicon.is_used(custom):
                    print(f"Custom name '{custom}' is already used.")
                    self.__name = self.__prompt()
                else:
                    self.__name = custom
            else:
                self.__name = self.random()
        else:
            self.__name = self.random()

        if self.__name is None:
            print("No more unused names available in lexicon!")

        while self.__name is None or lexicon.assign(self.__name, self) is False:
            self.__name = input("Enter new name: ")
            self.__name = None if not self.__name else self.__name

    def __str__(self):
        return self.__name

    def __prompt(self) -> str:
        """! Prompt for a name.
        :return: The name entered by the user or a random name.
        """
        name: str = input(f"Enter {self.__label} name [or use random name generator]: ")
        return name if name != "" else self.random()

    def name(self, name: str = None) -> str:
        """! Accessor function for name attribute.
        :param name: Name of interest
        :return: The name attribute
        """
        if name is not None:
            self.__name = name
        return self.__name

    def random(self) -> str:
        """! Generate a random name using all available categories.
        :return: Random name from lexicon"""
        return lexicon.random_unused()
