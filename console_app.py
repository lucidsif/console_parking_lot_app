import os
import sys
from create_parking_lot import create_parking_lot

# This is a console app that allows management of parking.

### FUNCTIONS ### 

def display_title_bar():    
    print("\t**********************************************")
    print("\t***  Welcome to Sif's parking lot program.  ***")
    print("\t*******     How can we help you?      *******")
    print("\t**********************************************")

def display_options(lotContainer):
    # See initialize_console_app() for information on lotContainer
    lot = lotContainer[0]
    # Let users know what they can do based on whether they have created a lot or not.  
    if isinstance(lot, create_parking_lot) :
        print('\n')
        display_title_bar()        
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

def handle_command_missing_args():
    pass

def process_input(command, lotContainer):
    # See initialize_console_app() for information on lotContainer
    lot = lotContainer[0]
    # Respond to the input based on whether they created a lot or not and the exact method being called.
    if isinstance(lot, create_parking_lot):
        if command[0] == 'park':
            registration = command[1]
            color = command[2]
            ticket = lot.park(registration, color)
            if type(ticket) is int:
                print('Allocated slot number:%s' %(ticket))
            else:
                print(ticket)
        elif command[0] == 'leave':
            ticket = int(command[1])
            print(lot.leave(ticket))
        elif command[0] == 'registration_numbers_for_cars_with_color':
            color = command[1]
            registrationList = lot.registration_numbers_for_cars_with_color(color)
            print(str(registrationList)[1:-1])
        elif command[0] == 'slot_numbers_for_cars_with_color':
            color = command[1]
            slotList = lot.slot_numbers_for_cars_with_color(color)
            print(str(slotList)[1:-1])
        elif command[0] == 'slot_number_for_registration_number':
            registration = command[1]
            print(lot.slot_number_for_registration_number(registration))
        elif(command[0] == 'status'):
            statusList = lot.status()
            for vehicle in statusList:
                print('%s %s %s' %(vehicle['slot'], vehicle['registration'], vehicle['color']))
        elif command[0] == 'q':
            print("\nThanks for using the parking lot program!")
        else:
            print(command)
            print("\nI didn't understand that input.\n")
    else:
        if command[0] == 'create_parking_lot':
            numOfSlots = int(command[1])
            lotContainer[0] = create_parking_lot(numOfSlots)
            # return lot
        elif command[0] == 'q':
            print("\nThanks for using my parking lot program!")
        else:
            print(command)
            print("\nI didn't understand that input.\n")

def process_file_input(lotContainer):
    # If a filename as been sent as input for the program at launch, parse the file into inputs 
    # and feed each input line to process_input()     
    if len(sys.argv) == 2:
        fileInput = sys.argv[1]
        lineInputs = []
        with open(fileInput,'r') as i:
            lineInputs = i.readlines()
        for command in lineInputs:
            process_input(command.split(), lotContainer)   

def process_user_input(lotContainer):
    # Initialize choice to be an array with a single empty string for command line arguments parsing.
    user_input = ['']
    # Set up a loop where users can choose what they'd like to do.
    while user_input[0] != 'q':
        display_options(lotContainer)   
        user_input = input("What would you like to do? ").split()
        process_input(user_input, lotContainer)

def initialize_console_app():
    # Clears the terminal screen and display a title bar. 
    os.system('clear') 
    display_title_bar() 
    # Initialize lot state in a list so we can pass lot by reference to functions. 
    lotContainer = [None]
    process_file_input(lotContainer)
    process_user_input(lotContainer)


    
