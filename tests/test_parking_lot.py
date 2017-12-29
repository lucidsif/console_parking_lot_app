import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from parking_lot import create_parking_lot

def test_parking_lot_instantiation():
    lot1 = create_parking_lot(0)
    assert isinstance(lot1, create_parking_lot)

def test_parking_lot_slots():
    lot2 = create_parking_lot(100)   
    filledArr = []
    for slot in lot2.slots:
        filledArr.append(slot)
    assert isinstance(lot2.slots, list)
    assert len(lot2.slots) == 100
    assert len(lot2.slots) == len(filledArr)
    assert sorted(lot2.slots) == sorted(filledArr)

    




    



