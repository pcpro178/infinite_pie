"""! Module for handling names."""

################################################################################
# Imports
################################################################################

import ip_lexicon as lexicon


################################################################################
# Class definitions
################################################################################

class Name:
    """! Class for handling names."""

    __label: str = "DefaultLabel"
    __name: str = "DefaultName"
    __prompt: str = "DefaultPrompt"

    def __init__(self, label: str, prompt: str = None) -> None:
        """! Initialize a new name object.
        :param label: The label for the name (e.g., "Empire", "System").
        :param prompt: The prompt to display when asking for a name.
        """
        self.__label = label if label is not None and label != "" else None
        self.__prompt = prompt if prompt is not None and prompt != "" else None

        if self.__label is None:
            raise ValueError("Label must be provided and cannot be empty.")

        if prompt is None or prompt == "":
            random_name: str = self.random()
            self.__name = random_name if random_name is not None else None
        else:
            self.__reprompt()

    def __str__(self):
        return self.__name

    def __reprompt(self) -> None:
        """! Prompt for a name."""

        if self.__prompt is None or self.__prompt == "":
            raise ValueError("Prompt must be provided and cannot be empty.")

        response: str = None

        while response is None or response == "":
            response: str = input(self.__prompt)
            if response is None or response == "":
                response = self.random()
                if response is None or response == "":
                    print("No more unused names available in lexicon!")
                    response = None
                else:
                    self.__name = response
            else:
                if lexicon.is_used(response):
                    print(f"Name '{response}' is already used.")
                    response = None
                else:
                    self.__name = response

    @property
    def name(self) -> str:
        """! Accessor function for name attribute.
        :return: The name attribute
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """! Mutator function for name attribute.
        :param name: The new name to set
        """
        self.__name = name

    def assign(self, obj: object) -> bool:
        """! Assign an object to name.
        :param obj: The object to assign the name to
        :return: True if assignment was successful, False otherwise
        """
        return lexicon.assign(self.__name, obj)

    def random(self) -> str:
        """! Generate a random name using all available categories.
        :return: Random name from lexicon"""
        return lexicon.random_unused()
