import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from create_parking_lot import create_parking_lot
from console_app import (display_title_bar, display_options, process_input,
process_file_input, process_user_input, initialize_console_app)

def test_display_title_bar(capsys):
    display_title_bar()
    out, err = capsys.readouterr()
    line1 = "\t**********************************************\n"
    line2 = "\t**  Welcome to Sif's parking lot program!  **\n"
    line3 = "\t*******     How can we help you?      *******\n"
    line4 = "\t**********************************************\n"
    expectedPrint = line1 + line2 + line3 + line4
    assert out == expectedPrint

def test_display_options(capsys):
    quitOption = '[q] <string quit>\n'
    def uninitialized_lot():
        # An uninitialized lot should print only 'create_parking_lot' and 'quit'
        lotContainer = [None]
        createParkingLotOption = '[create_parking_lot] <int slots>\n'
        expectedPrintForUninitializedLot = createParkingLotOption + quitOption
        display_options(lotContainer)
        out, err = capsys.readouterr()
        assert out == expectedPrintForUninitializedLot
    
    def initialized_lot():
        # An initialized lot should print only print 'park', 'leave', 
        # 'registration_numbers_for_cars_with_color', 'slot_numbers_for_cars_with_color', 
        # 'slot_number_for_registration_number', 'status', and 'quit' options
        lotContainer = [None]
        with capsys.disabled():
            initializedLot = create_parking_lot(10)
            lotContainer[0] = initializedLot
        parkOption = '[park] <string registration> <string color>\n'
        leaveOption = '[leave] <integer ticket>\n'
        registrationNumberForCarsWithColorOption = '[registration_numbers_for_cars_with_color] <string color\n'
        slotNumbersForCarsWithColorOption = '[slot_numbers_for_cars_with_color] <string color\n'
        slotNumberForRegistrationNumberOption = '[slot_number_for_registration_number] <string registration>\n'
        statusOption = '[status]\n'
        expectedPrintForInitializedLot = ('\n\n' + parkOption + leaveOption + 
        registrationNumberForCarsWithColorOption + slotNumbersForCarsWithColorOption +
        slotNumberForRegistrationNumberOption + statusOption + quitOption)
        display_options(lotContainer)
        out, err = capsys.readouterr()
        assert out == expectedPrintForInitializedLot
    uninitialized_lot()
    initialized_lot()

def test_process_input(capsys):
    # Input commands
    park = 'park'
    leave = 'leave'
    registrationNumbersForCarsWithColor = 'registration_numbers_for_cars_with_color'
    slotNumbersForCarsWithColor= 'slot_numbers_for_cars_with_color'
    slotNumberForCarWithRegistrationNumber = 'slot_number_for_car_with_registration_number'
    status = 'status'
    createParkingLot = 'create_parking_lot'
    quitCmd = 'q'
    invalidInput = 'thisIsInvalidInput'
    # Response messages
    quitResponse = "\nThanks for using the parking lot program!"
    invalidResponse = "\nI didn't understand that input.\n\n"

    def uninitialized_lot():
            def test_create_parking_lot_cmd():
                lotContainer = [None]
                # A create_parking_lot command passed to process_input should call the
                # create_parking_lot() method 
                process_input([createParkingLot, 10], lotContainer)
                out, err = capsys.readouterr()    
                assert out == 'Created a parking lot with 10 slots\n'
                # It should mutate the lotContainer by replacing the None with a create_parking_lot instance
                assert isinstance(lotContainer[0], create_parking_lot)
            def test_quit_cmd():
                lotContainer = [None]                
                # It should print a thank you message when the quit command is given
                process_input([quitCmd], lotContainer)
                out, err = capsys.readouterr()
                assert out == "\nThanks for using my parking lot program!\n"
            def test_invalid_cmd():
                lotContainer = [None]                
                # It should print an apology message for the invalid input
                process_input([invalidInput], lotContainer)
                out, err = capsys.readouterr()
                assert out == invalidResponse
            test_create_parking_lot_cmd()
            test_quit_cmd()
            test_invalid_cmd()

    def initialized_lot():
        lotContainer = [create_parking_lot(10)]
        def test_park_cmd():
            pass
    uninitialized_lot()

    




    







