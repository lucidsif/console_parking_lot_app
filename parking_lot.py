import os
from create_parking_lot import create_parking_lot

### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')      
    print("\t**********************************************")
    print("\t***  Welcome to Sif's parking lot program. How can we help you?  ***")
    print("\t**********************************************")
    
def parse_user_input():
    # Let users know what they can do.
    print('[create_parking_lot] <int slots>')
    print('[park] <string registration> <string color>')
    print('[q] <string quit>')
    # Split string into a list delimited by white spaces
    return input("What would you like to do? ").split()
    
### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
choice = ['']
display_title_bar()
while choice[0] != 'q':    
    
    choice = parse_user_input()
    
    # Respond to the user's input.
    display_title_bar()
    if choice[0] == 'create_parking_lot':
        print("\nParking lot created\n")
    elif choice[0] == 'park':
        print("\nCar parked!\n")
    elif choice[0] == 'q':
        print("\nThanks for using the parking lot program!")
    else:
        print(choice)
        print("\nI didn't understand that input.\n")


    
