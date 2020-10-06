from os import system, name


# https://www.geeksforgeeks.org/clear-screen-python/
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
