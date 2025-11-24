"""Module for handling stellar systems."""

import ip_name

class System:
    """Class for handling stellar systems."""

    __name: ip_name.Name = None

    def __init__(self):
        self.__name = ip_name.Name(self.__class__.__name__)
        print(f"System {self.__name} created.")
