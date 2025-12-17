"""! Module for the main program."""


from ip_play import Play
# todo jfell cleanup
# import ip_empire


# todo jfell cleanup
# __empire: ip_empire.Empire = None
__game: Play = Play()


def main():
    """! Main function for the program."""
    # todo jfell cleanup
    # __empire = ip_empire.Empire()
    # __empire.cycle()
    while __game.cycle():
        pass


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
