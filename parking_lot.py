import os
from create_parking_lot import create_parking_lot

# This is a console app that allows management of parking.

### FUNCTIONS ###

def display_title_bar():    
    print("\t**********************************************")
    print("\t***  Welcome to Sif's parking lot program. How can we help you?  ***")
    print("\t**********************************************")
    
# TODO: Refactor function into 2 functions and DRY
def display_options_and_parse_user_input(lot):
    # Let users know what they can do based on whether they have created a lot or not.  
    if isinstance(lot, create_parking_lot) :
        print('\n')
        print('[park] <string registration> <string color>')
        print('[leave] <integer ticket>')
        print('[registration_numbers_for_cars_with_color] <string color')
        print('[slot_numbers_for_cars_with_color] <string color')
        print('[slot_number_for_registration_number] <string registration>')
        print('[status]')
        print('[q] <string quit>')
    else:
        print('[create_parking_lot] <int slots>')
        print('[q] <string quit>')
    # Split string into a list delimited by white spaces
    return input("What would you like to do? ").split()

def initialize_console_app():
    # Clears the terminal screen, and displays a title bar. 
    os.system('clear') 
    display_title_bar() 
    # Initialize choice to be an array with a single empty string for command line arguments parsing.
    choice = ['']
    # Initialize lot state
    lot = None
    # Set up a loop where users can choose what they'd like to do.    
    while choice[0] != 'q':   
        choice = display_options_and_parse_user_input(lot)
        # Respond to the user's input based on whether they created a lot or not.
        if isinstance(lot, create_parking_lot):
            if choice[0] == 'park':
                registration = choice[1]
                color = choice[2]
                ticket = lot.park(registration, color)
                if type(ticket) is int:
                    print('Allocated slot number:%s' %(ticket))
                else:
                    print(ticket)
            elif choice[0] == 'leave':
                ticket = int(choice[1])
                print(lot.leave(ticket))
            elif choice[0] == 'registration_numbers_for_cars_with_color':
                color = choice[1]
                print(lot.registration_numbers_for_cars_with_color(color))
            elif choice[0] == 'slot_numbers_for_cars_with_color':
                color = choice[1]
                print(lot.slot_numbers_for_cars_with_color(color))
            elif choice[0] == 'slot_number_for_registration_number':
                registration = choice[1]
                print(lot.slot_number_for_registration_number(registration))
            elif(choice[0] == 'status'):
                statusList = lot.status()
                for vehicle in statusList:
                    print('%s %s %s' %(vehicle['slot'], vehicle['registration'], vehicle['color']))
            elif choice[0] == 'q':
                print("\nThanks for using the parking lot program!")
            else:
                print(choice)
                print("\nI didn't understand that input.\n")
        else:
            if choice[0] == 'create_parking_lot':
                numOfSlots = int(choice[1])
                lot = create_parking_lot(numOfSlots)
            elif choice[0] == 'q':
                print("\nThanks for using the parking lot program!")
            else:
                print(choice)
                print("\nI didn't understand that input.\n")
        display_title_bar()

initialize_console_app()


    
