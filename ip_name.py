## @brief Name handling module

from typing import List

import randomname

class Name:
    """Class for handling names."""

    __name: str = "DefaultName"

    def __init__(self, obj: str = ""):
        name: str = input(f"Enter {obj} name [or use random name generator]: ")
        self.__name = name if name != "" else self.random()
        print(f"New {obj} name: {self.__name}")

    def get(self) -> str:
        """Get the current name."""
        return self.__name

    def set(self, name: str) -> None:
        """Set a new name."""
        self.__name = name

    def random(self, adjs: List[str] = list(), nouns: List[str] = list()) -> str:
        """Generate a random name using all available categories."""
        return randomname.get_name(adjs, nouns)

    def print_categories(self) -> None:
        """Prints available categories."""
        print(f"Adjective categories: {randomname.ADJECTIVES}")
        print(f"Noun categories: {randomname.NOUNS}")
