class create_parking_lot(object):
    def __init__(self, numOfSlots):
        self.slots = []
        for num in range(numOfSlots):
            self.slots.append(False)
    def park(self, plate, color):
        closestSlotIdx = self.find_closest_spot()        
        self.slots[closestSlotIdx] = {'plate': plate, 'color': color}
        return closestSlotIdx

    def find_closest_spot(self):
        try:
            return self.slots.index(False)
        except RuntimeError:
            return 'Sorry, parking lot is full'

    def leave(self, ticketNumber):
        self.slots[ticketNumber] = False
        return "Slot number %s is free" %(ticketNumber)