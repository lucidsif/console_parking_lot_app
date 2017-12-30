import sys, os
from mock import patch
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
        # An uninitialized lot should print only 'create_parking_lot' and 'quit'.
        lotContainer = [None]
        createParkingLotOption = '[create_parking_lot] <int slots>\n'
        expectedPrintForUninitializedLot = createParkingLotOption + quitOption
        display_options(lotContainer)
        out, err = capsys.readouterr()
        assert out == expectedPrintForUninitializedLot
    def initialized_lot():
        # An initialized lot should print only print 'park', 'leave', 
        # 'registration_numbers_for_cars_with_color', 'slot_numbers_for_cars_with_color', 
        # 'slot_number_for_registration_number', 'status', and 'quit' options.
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
    # Invoke the subtests.
    uninitialized_lot()
    initialized_lot()

def test_process_input(capsys):
    # Input commands
    park = 'park'
    leave = 'leave'
    registrationNumbersForCarsWithColor = 'registration_numbers_for_cars_with_color'
    slotNumbersForCarsWithColor= 'slot_numbers_for_cars_with_color'
    slotNumberForCarWithRegistrationNumber = 'slot_number_for_registration_number'
    status = 'status'
    createParkingLot = 'create_parking_lot'
    quitCmd = 'q'
    invalidInput = 'thisIsInvalidInput'
    # Response messages
    quitResponse = "\nThanks for using the parking lot program!"
    invalidResponse = "\nI didn't understand that input.\n\n"
    def test_uninitialized_lot():
            def test_create_parking_lot_cmd():
                lotContainer = [None]
                # A create_parking_lot command passed to process_input should call the
                # create_parking_lot() method .
                process_input([createParkingLot, 10], lotContainer)
                out, err = capsys.readouterr()    
                assert out == 'Created a parking lot with 10 slots\n'
                # It should mutate the lotContainer by replacing the None with a create_parking_lot instance.
                assert isinstance(lotContainer[0], create_parking_lot)
            def test_quit_cmd():
                lotContainer = [None]                
                # It should print a thank you message when the quit command is given.
                process_input([quitCmd], lotContainer)
                out, err = capsys.readouterr()
                assert out == "\nThanks for using my parking lot program!\n"
            def test_invalid_cmd():
                lotContainer = [None]                
                # It should print an apology message for the invalid input.
                process_input([invalidInput], lotContainer)
                out, err = capsys.readouterr()
                assert out == invalidResponse
        # Invoke the 2nd level subtests.            
            test_create_parking_lot_cmd()
            test_quit_cmd()
            test_invalid_cmd()
    def test_initialized_lot():
        # Test data.
        car1Registration = 'XAB-741'
        car1Color = 'Black'
        car2Registration = 'YUN-410'
        car2Color = 'Black'
        car3Registration = 'ZUM-400'
        car3Color = 'Red'
        lotContainer = [None]
        with capsys.disabled():
            initializedLot = create_parking_lot(10)
            initializedLot.park(car1Registration, car1Registration)
            initializedLot.park(car2Registration, car2Color)
            initializedLot.park(car3Registration, car3Color)
            lotContainer[0] = initializedLot
        def test_park_cmd():
            # It should print a message describing the slot number allocated.
            process_input([park, 'CRUD-100', 'Black'], lotContainer)
            out, err = capsys.readouterr()    
            assert out == 'Allocated slot number:3\n'
        def test_leave_cmd():
            # It should print a message describing  the slot number freed.
            process_input([leave, 0], lotContainer)
            out, err = capsys.readouterr()    
            assert out == 'Slot number 0 is free\n'
        def test_registration_numbers_for_cars_with_color_cmd():
            # It should print a list of registration numbers of cars with that color.
            process_input([registrationNumbersForCarsWithColor, 'Black'], lotContainer)
            out, err = capsys.readouterr()    
            assert out == "'YUN-410', 'CRUD-100'\n"
        def test_slot_numbers_for_cars_with_color_cmd():
            # It should print a list of slot numbers of cars with that color.
            process_input([slotNumbersForCarsWithColor, 'Black'], lotContainer)
            out, err = capsys.readouterr()    
            assert out == '1, 3\n'
        def test_slot_number_for_registration_number_cmd():
            # It should print the slot number of the car with that registration number.
            process_input([slotNumberForCarWithRegistrationNumber, 'YUN-410'], lotContainer)
            out, err = capsys.readouterr()    
            assert out == '1\n'
        def test_status_cmd():
            # It should print a list of cars in the garage with their slot number, registration number, and color.
            process_input([status], lotContainer)
            out, err = capsys.readouterr()    
            assert out == '1 YUN-410 Black\n2 ZUM-400 Red\n3 CRUD-100 Black\n'
        def test_quit_cmd():              
            # It should print a thank you message when the quit command is given.
            process_input([quitCmd], lotContainer)
            out, err = capsys.readouterr()
            assert out == "\nThanks for using my parking lot program!\n"
        def test_invalid_cmd():           
            # It should print an apology message for the invalid input.
            process_input([invalidInput], lotContainer)
            out, err = capsys.readouterr()
            assert out == invalidResponse
        # Invoke the 2nd level subtests.
        test_park_cmd()
        test_leave_cmd()
        test_registration_numbers_for_cars_with_color_cmd()
        test_slot_numbers_for_cars_with_color_cmd()
        test_slot_numbers_for_cars_with_color_cmd
        test_slot_number_for_registration_number_cmd()
        test_status_cmd()
    # Invoke the subtests.
    test_uninitialized_lot()
    test_initialized_lot()

def test_process_file_input(capsys):
    uninitializedLotContainer = [None]    
    def test_file_name_passed():
        # It should call process_input on the file if there is a filename passed to it.
        testargs = ["console_app.py", "file_inputs.txt"]
        expectedPrintOutput = ('Created a parking lot with 6 slots\n' +
        'Allocated slot number:0\n' +
        'Allocated slot number:1\n' +
        'Allocated slot number:2\n' +
        'Allocated slot number:3\n' +
        'Allocated slot number:4\n' +
        'Allocated slot number:5\n' +
        'Slot number 4 is free\n' +
        '0 KA-01-HH-1234 White\n' +
        '1 KA-01-HH-9999 White\n' +
        '2 KA-01-BB-0001 Black\n' +
        '3 KA-01-HH-7777 Red\n' +
        '5 KA-01-HH-3141 Black\n' +
        'Allocated slot number:4\n' +
        'Sorry, parking lot is full\n' +
        "'KA-01-HH-1234', 'KA-01-HH-9999', 'KA-01-P-333'\n" +
        '0, 1, 4\n' +
        '5\n' +
        'Not found\n')
        with patch.object(sys, 'argv', testargs):
            process_file_input(uninitializedLotContainer)
            out, err = capsys.readouterr()
            assert out == expectedPrintOutput
    def test_no_file_name_passed():
        testargs = ["console_app.py"]
        expectedPrintOutput = ''
        with patch.object(sys, 'argv', testargs):
            process_file_input(uninitializedLotContainer)
            out, err = capsys.readouterr()
            assert out == expectedPrintOutput
    test_file_name_passed()
    test_no_file_name_passed()

    




    







