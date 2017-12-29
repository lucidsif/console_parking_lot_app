import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from parking_lot import create_parking_lot

def test_parking_lot_instantiation():
    lot1 = create_parking_lot(0)
    assert isinstance(lot1, create_parking_lot)

def test_parking_lot_slots():
    lot1 = create_parking_lot(5) 
    lot2 = create_parking_lot(100)   
    assert isinstance(lot1.slots, list)    
    assert len(lot1.slots) == 5
    assert isinstance(lot2.slots, list)
    assert len(lot2.slots) == 100


    



