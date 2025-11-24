"""Module for the main program."""

import ip_empire

__empire: ip_empire.Empire = None

# Defining main function
def main():
    __empire = ip_empire.Empire()


# Using the special variable
# __name__
if __name__=="__main__":
    main()
