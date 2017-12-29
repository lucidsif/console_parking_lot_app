import os
from create_parking_lot import create_parking_lot

# This is a console app that allows management of parking

### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')      
    print("\t**********************************************")
    print("\t***  Welcome to Sif's parking lot program. How can we help you?  ***")
    print("\t**********************************************")
    
def display_options_and_parse_user_input(isLotCreated):
    # Let users know what they can do.
    if isLotCreated is True:
        print('[park] <string registration> <string color>')
        print('[q] <string quit>')
    else:
        print('[create_parking_lot] <int slots>')
        print('[q] <string quit>')
    # Split string into a list delimited by white spaces
    return input("What would you like to do? ").split()

def initialize_console_app():
    # Set up a loop where users can choose what they'd like to do.
    choice = ['']
    isLotCreated = False
    display_title_bar()
    while choice[0] != 'q':    
        choice = display_options_and_parse_user_input(isLotCreated)
        # Respond to the user's input.
        display_title_bar()
        if isLotCreated == True:
            if choice[0] == 'park':
                print("\nCar parked!\n")
            elif choice[0] == 'q':
                print("\nThanks for using the parking lot program!")
            else:
                print(choice)
                print("\nI didn't understand that input.\n")
        else:
            if choice[0] == 'create_parking_lot':
                isLotCreated = True
                print("\nParking lot created!\n")
            else:
                print(choice)
                print("\nI didn't understand that input.\n")


initialize_console_app()


    
