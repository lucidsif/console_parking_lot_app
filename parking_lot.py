class create_parking_lot(object):
    def __init__(self, numOfSlots):
        self.slots = []
        for num in range(numOfSlots):
            self.slots.append(False)
    def park(self, registration, color):
        try:
            closestSlotIdx = self.find_closest_spot()
            self.slots[closestSlotIdx] = {'registration': registration, 'color': color}
            print("Allocated slot number:%s" %(closestSlotIdx))
            return closestSlotIdx
        except TypeError:
            return 'Sorry, parking lot is full'

    def find_closest_spot(self):
        try:
            return self.slots.index(False)
        except ValueError:
            return 'No available spots'

    def leave(self, ticketNumber):
        self.slots[ticketNumber] = False
        return "Slot number %s is free" %(ticketNumber)