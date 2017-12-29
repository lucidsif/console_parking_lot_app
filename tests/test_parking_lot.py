import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from parking_lot import create_parking_lot

def test_parking_lot_instantiation():
    lot = create_parking_lot(0)
    # lot1 should be an instance of the parking lot class
    assert isinstance(lot, create_parking_lot)

def test_parking_lot_slots():
    lot = create_parking_lot(6)   
    expectedArr = []
    for num in range(6):
        expectedArr.append(False)
    # A parking lot instance should have a slots property that is a data type of list
    assert isinstance(lot.slots, list)
    # the number of slots in the parking lot should be equal to the number passed to the class during instantiation
    assert len(lot.slots) == 6
    # the expectedArr list should be deeply equal to the slots list of the parking lot instance
    assert len(lot.slots) == len(expectedArr)
    assert sorted(lot.slots) == sorted(expectedArr)

def test_park():
    lot = create_parking_lot(5)
    ticket = lot.park('KA-01-HH-1234', 'White')
    vehicle = lot.slots[ticket]
    # the ticket or output of park should be equal to the index the vehicle is parked in
    assert ticket == 0
    # The vehicle at the slot on the ticket should have the same registration and color as the one that was parked
    assert vehicle['registration'] is 'KA-01-HH-1234'
    assert vehicle['color'] is 'White'
    # If parking is attempted when there are no available slots, an apology message should be returned
    lot.park('JKL', 'Purple')
    lot.park('MNO', 'Gray')
    lot.park('PQR', 'Violet')
    lot.park('STU', 'Rainbow')
    assert lot.park('thisShouldNotBeParked', 'fail') == 'Sorry, parking lot is full'

def test_find_closest_spot():
    lot = create_parking_lot(5)
    assert lot.find_closest_spot() == 0
    firstTicket = lot.park('ABC', 'Blue')
    # After parking one car, the next available slot should have index of 1
    assert lot.find_closest_spot() == 1
    # After parking two additional cars (total of 3 cars), the next available slot should have index of 2
    secondTicket = lot.park('DEF', 'Red')
    thirdTicket = lot.park('GHI', 'White')
    assert lot.find_closest_spot() == 3
    # When the first car leaves, the next available slot should have index of 0
    lot.leave(firstTicket)
    assert lot.find_closest_spot() == 0
    # When there are no more available slots, it should return a string message
    lot.park('JKL', 'Purple')
    lot.park('MNO', 'Gray')
    lot.park('PQR', 'Violet')
    assert lot.find_closest_spot() == 'No available spots'

def test_leave():
    lot = create_parking_lot(5)
    firstTicket = lot.park('ABC', 'Blue')
    lot.leave(firstTicket)
    # There should be no car at a slot once it leaves
    assert lot.slots[firstTicket] is False

def test_registration_numbers_for_cars_with_color():
    lot = create_parking_lot(10)
    lot.park('JKL', 'Purple')
    lot.park('MNO', 'Gray')
    lot.park('PQR', 'Violet')
    lot.park('ZUB', 'Purple')
    lot.park('MON', 'Gray')
    ticketX = lot.park('NOM', 'Gray')
    lot.park('GREN', 'Neon')
    lot.leave(ticketX)
    lot.park('SHAR', 'Gray')

    # It should return a list of the registration numbers of all cars with the specified color
    expectedRegistrationListOfPurpleCars = ['JKL', 'ZUB']
    actualRegistrationListOfPurpleCars = lot.registration_numbers_for_cars_with_color('Purple')
    assert len(expectedRegistrationListOfPurpleCars) == len(actualRegistrationListOfPurpleCars)
    assert sorted(expectedRegistrationListOfPurpleCars) == sorted(actualRegistrationListOfPurpleCars)

    # It should only return registration numbers of the specified color of current cars in the lot
    expectedRegistrationListOfGrayCars = ['MNO', 'MON', 'SHAR']
    actualRegistrationListOfGrayCars = lot.registration_numbers_for_cars_with_color('Gray')
    assert len(expectedRegistrationListOfGrayCars) == len(actualRegistrationListOfGrayCars)
    assert sorted(expectedRegistrationListOfGrayCars) == sorted(actualRegistrationListOfGrayCars)

def test_slot_numbers_for_cars_with_color():
    lot = create_parking_lot(10)
    lot.park('JKL', 'Purple')
    lot.park('MNO', 'Gray')
    lot.park('PQR', 'Violet')
    lot.park('ZUB', 'Purple')
    lot.park('MON', 'Gray')
    ticketX = lot.park('NOM', 'Gray')
    lot.park('GREN', 'Neon')
    lot.leave(ticketX)
    lot.park('SHAR', 'Gray')

        # It should return a list of the slot numbers of all cars with the specified color
    expectedSlotListOfPurpleCars = [0, 3]
    actualSlotListOfPurpleCars = lot.slot_numbers_for_cars_with_color('Purple')
    assert len(expectedSlotListOfPurpleCars) == len(actualSlotListOfPurpleCars)
    assert sorted(expectedSlotListOfPurpleCars) == sorted(actualSlotListOfPurpleCars)

    # It should only return slot numbers of the specified color of current cars in the lot
    expectedSlotListOfGrayCars = [1, 4, 5]
    actualSlotListOfGrayCars = lot.slot_numbers_for_cars_with_color('Gray')
    assert len(expectedSlotListOfGrayCars) == len(actualSlotListOfGrayCars)
    assert sorted(expectedSlotListOfGrayCars) == sorted(actualSlotListOfGrayCars)





    




    



