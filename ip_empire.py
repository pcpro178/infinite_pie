## @brief Empire class for managing empires

import ip_name

class Empire:
    """Class for managing empires."""
    __name: ip_name.Name = None

    def __init__(self):
        print("Creating new Empire instance . . .")
        self.__name = ip_name.Name("Empire")

    def name_get(self):
        """Get the current empire name."""
        return self.__name

    def name_set(self, name):
        """Set a new empire name."""
        self.__name = name

    def test(self):
        """Test randomname functionalities."""

        # Generate a name using all available categories
        print(ip_name.randomname.get_name())

        # Generate a name with specific categories
        print(ip_name.randomname.get_name(adj=('appearance',), noun=('cats', 'food')))
        print(ip_name.randomname.get_name(adj=('character',), noun=('cats', 'food')))
        print(ip_name.randomname.get_name(adj=('complexity',), noun=('cats', 'food')))
        print(ip_name.randomname.get_name(adj=('linguistics',), noun=('cats', 'food')))
        print(ip_name.randomname.get_name(adj=('materials',), noun=('cats', 'food')))
        print(ip_name.randomname.get_name(adj=('physics'), noun=('cats', 'food')))

        self.__name.print_categories()
