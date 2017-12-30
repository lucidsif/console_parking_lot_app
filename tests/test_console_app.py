import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from console_app import (display_title_bar, display_options, process_file_input, 
process_user_input, initialize_console_app, create_parking_lot)

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
    # An uninitialized lot should print only 'create_parking_lot' and 'quit'
    lotContainer = [None]
    createParkingLotOption = '[create_parking_lot] <int slots>\n'
    quitOption = '[q] <string quit>\n'
    expectedPrintForUninitializedLot = createParkingLotOption + quitOption
    display_options(lotContainer)
    out, err = capsys.readouterr()
    assert out == expectedPrintForUninitializedLot
    # An initialized lot should print only print 'park', 'leave', 
    # 'registration_numbers_for_cars_with_color', 'slot_numbers_for_cars_with_color', 
    # 'slot_number_for_registration_number', 'status', and 'quit' options
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

    







