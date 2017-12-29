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
    # the ticket should be equal to the index the vehicle is parked in
    assert ticket == 0

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

def test_leave():
    pass



    




    



