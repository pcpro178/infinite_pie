## @brief Python main program file

import ip_empire

__empire: ip_empire.Empire = None

# Defining main function
def main():
    print("hey there")
    __empire = ip_empire.Empire()


# Using the special variable
# __name__
if __name__=="__main__":
    main()
