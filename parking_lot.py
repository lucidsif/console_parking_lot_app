class create_parking_lot(object):
    def __init__(self, numOfSlots):
        self.slots = []
        for num in range(numOfSlots):
            self.slots.append(False)