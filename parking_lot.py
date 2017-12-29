import os
from create_parking_lot import create_parking_lot

# This is a console app that allows management of parking.

### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')      
    print("\t**********************************************")
    print("\t***  Welcome to Sif's parking lot program. How can we help you?  ***")
    print("\t**********************************************")
    
def display_options_and_parse_user_input(lot):
    # Let users know what they can do based on whether they have created a lot or not.
    if isinstance(lot, create_parking_lot) :
        print('[park] <string registration> <string color>')
        print('[q] <string quit>')
    else:
        print('[create_parking_lot] <int slots>')
        print('[q] <string quit>')
    # Split string into a list delimited by white spaces
    return input("What would you like to do? ").split()

def initialize_console_app():
    # Initialize choice to be an array with a single empty string for command line arguments parsing.
    choice = ['']
    # Initialize isLotCreated state for better UX and program robustness.
    lot = None
    display_title_bar()
    # Set up a loop where users can choose what they'd like to do.    
    while choice[0] != 'q':    
        choice = display_options_and_parse_user_input(lot)
        # Respond to the user's input based on whether they created a lot or not.
        display_title_bar()
        if isinstance(lot, create_parking_lot):
            if choice[0] == 'park':
                print("\nCar parked!\n")
            elif choice[0] == 'q':
                print("\nThanks for using the parking lot program!")
            else:
                print(choice)
                print("\nI didn't understand that input.\n")
        else:
            if choice[0] == 'create_parking_lot':
                numOfSlots = int(choice[1])
                lot = create_parking_lot(numOfSlots)
                print("\nParking lot created!\n")
            else:
                print(choice)
                print("\nI didn't understand that input.\n")


initialize_console_app()


    
