"""! Module for the main program."""

################################################################################
# Imports
################################################################################

from ip_play import Play

import logging


################################################################################
# Constants & Globals
################################################################################

MENU_CHOICE_EXIT: str = "Exit"

LOGGER_PATH: str = "infinite_pie.log"


################################################################################
# Function definitions
################################################################################

def main():
    """! Main function for the program."""
    # Create and configure logger
    logging.basicConfig(filename=LOGGER_PATH,
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Get logging object
    logger: logging.Logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    # Initialize game play
    __game: Play = Play()
    __game.menu.choices.extend([MENU_CHOICE_EXIT])
    __game.show()

    while __game.menu.response != MENU_CHOICE_EXIT:
        __game.run()
        __game.show()


################################################################################
# Entry point
################################################################################

if __name__ == "__main__":
    main()
