"""Module for handling names."""

from typing import List

import ip_lexicon as lexicon

class Name:
    """Class for handling names."""

    __label: str = "DefaultLabel"
    __name: str = "DefaultName"

    def __init__(self, label: str, allow_custom: bool = False, custom: str = "") -> None:
        """
        :param label: The label for the name (e.g., "Empire", "System").
        :param allow_custom: Whether to allow custom name input.
        :param custom: The custom name to set, if any.
        """
        if label is not None and label != "":
            self.__label = label

        if allow_custom:
            if custom is not None and custom != "":
                if custom in lexicon.is_used():
                    print(f"Custom name '{custom}' is already used. Generating random name instead.")
                    self.__name = self.random()
            else:
                print(f"Custom name not specified for {label}.")
                name: str = input(f"Enter {label} name [or use random name generator]: ")
                self.__name = name if name != "" else self.random()
        else:
            self.__name = self.random()

        lexicon.assign(self.__name, self)

    def __str__(self):
        return self.__name

    def get(self) -> str:
        """Get the current name."""
        return self.__name

    def set(self, name: str) -> None:
        """Set a new name."""
        self.__name = name

    def random(self, adjs: List[str] = list(), nouns: List[str] = list()) -> str:
        """Generate a random name using all available categories."""
        return lexicon.random_unused()
